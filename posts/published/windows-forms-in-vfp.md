---
uid: windows-forms-in-vfp
title: Windows Forms in VFP
slug: windows-forms-in-vfp
date: 2006-04-26
status: published
type: post
description: Eigentlich hatte ich aus einer reinen Spiellaune heraus bereits Ende letzten Jahres ein wenig mit der Möglichkeit experimentiert, ob man .NET Windows Forms ebenfalls in Visual FoxPro verwenden könnte oder nicht.
tags:
- Development
keywords: Development
metaTitle: Windows Forms in VFP
metaDescription: Eigentlich hatte ich aus einer reinen Spiellaune heraus bereits Ende letzten Jahres ein wenig mit der Möglichkeit experimentiert, ob man .NET Windows Forms ebenfalls in Visual FoxPro verwenden könnte oder nicht.
image: ''
ogTitle: Windows Forms in VFP
ogDescription: WinForm, COM Interop, Threading
layout: post
bodyClass: post-template tag-development
postClass: post tag-development
isPost: true
isPage: false
isDraft: false
isScheduled: false
isTagPage: false
isTagsIndexPage: false
isAuthorPage: false
isHome: false
author: Jochen Kirstätter
authorTwitter: '@jkirstaetter'
authorFacebook: https://facebook.com/jochen.kirstaetter
website: ''
location: ''
authorImage: content/images/2018/10/JoKi_StAubin_100px.webp
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/windows-forms-in-vfp/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-26T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: WinForm, COM Interop, Threading
twitterTitle: Windows Forms in VFP
twitterDescription: WinForm, COM Interop, Threading
twitterImage: 
facebookTitle: Windows Forms in VFP
facebookDescription: WinForm, COM Interop, Threading
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
WinForm, COM Interop, Threading

\*\*Ursache und Wirkung\*\*  
Eigentlich hatte ich aus einer reinen Spiellaune heraus bereits Ende letzten Jahres ein wenig mit der Möglichkeit experimentiert, ob man .NET Windows Forms ebenfalls in Visual FoxPro verwenden könnte oder nicht. Bei den vorlaufenden Recherchen fand ich unter anderem den sehr informativen Beitrag von Rick Strahl zu diesem Thema. Mein Lösungsansatz basiert so ziemlich auf seinem Artikel. Dennoch habe ich ein paar Modifikationen vorgenommen. Die erneute, intensivere Beschäftigung mit diesem Thema begründet sich durch ein, zwei Threads in der Microsoft Newsgruppe mpdf zu diesem Thema. Ein geschätzter Kollege hatte einige Fragen und Probleme bei der Realisierung seiner Lösung. Primärer Auslöser war die Frage, ob man eine WinForm innerhalb des VFP-Screens ausführen könnte oder nicht. Gleich eins vorweg: Es funktioniert!

\*\*Die beteiligten Technologien\*\*  
Die verwendeten Technologien zur Ausführung von WinForms in Visual FoxPro (oder jeder anderen Programmiersprache) sehen wie folgt aus:

\* .NET Framework 1.1 oder 2.0  
\* Visual FoxPro (oder beliebig)  
\* Windows API

Ich werde nachfolgend die einzelnen Schritte beschreiben und versuchen zu erläutern. Zum Nachvollziehen der Codebeispiele könnt ihr den [COM Proxy for .NET](xref:windows-forms-in-vfp) verwenden. Die Dynamic-Link Library liegt für das .NET Framework 1.1 und 2.0 vor.

\*\*.NET Framework 1.1 oder 2.0\*\*  
Zur Umsetzung habe ich mir in Visual Studio ein neues Projekt vom Typ Class Library erstellt und eine neue Windows Form hinzugefügt. Diese Form habe ich gemäß den Anweisungen von Rick COM-fähig modifiziert. Das bedeutet unter anderem, dass wir das ProgId-Attribut vergeben, Threading integrieren und ein Interface erstellen.  
[code]using System;  
using System.Threading;  
using System.Windows.Forms;  
using System.Runtime.InteropServices;

namespace ProLib.Net.Components  
{  
[ClassInterface(ClassInterfaceType.AutoDual)]  
[ComSourceInterfaces( typeof(IWinFormEvents) )]  
[ProgId("ProLib.WinForm")]  
public class WinForm : Form  
{  
private WinForm threadForm = null;

public WinForm RunForm()  
{  
// create an instance on this thread that  
// we can pass back to the caller.  
this.threadForm = new WinForm();

// create thread and bind to initial method of form.  
Thread thread = new Thread( new ThreadStart( this.RunThread ));  
thread.SetApartmentState(ApartmentState.STA);  
thread.Start();

return this.threadForm;  
}

[ComVisible(false)]  
public void RunThread()  
{  
// show the current form in a thread.  
this.threadForm.Show();  
Application.Run();  
}

private void WinForm\_Closing(object sender, System.ComponentModel.CancelEventArgs e)  
{  
Application.ExitThread();  
}  
}

[InterfaceType(ComInterfaceType.InterfaceIsIDispatch)]  
public interface IWinFormEvents  
{  
// [DispId(1)]  
void Closing();  
}  
}  
[/code]  
Das ist das eigentliche Grundgerüst. In den Projekteigenschaften noch hinterlegt, dass wir \*Register for COM interop\* wollen und kompilieren.  
\*Anmerkung:\* Es steht euch frei, hier weiteren Code zu implementieren. Dieser Artikel zeigt lediglich proof-of-concept. 😎

\*\*Visual FoxPro\*\*  
Nach der Registrierung des COM-Servers (erfolgt beim Kompilieren automatisch) können wir die Tests in VFP starten. Meine Empfehlung: Zuerst interaktiv im Command Window probieren:  
[code]oCom = CreateObject("ProLib.WinForm")  
oForm = oCom.RunForm()  
[/code]  
Nach Ausführung der Zeilen erscheint eine WinForm auf dem Desktop. Diese Form kann frei bewegt werden und entspricht damit (in etwa) dem gewohnten Verhalten von instanziierten COM-Servern, wie etwa \*Word.Application\*. Weiterhin ist die Form nicht-modal, d.h. dass in VFP weiterer Code ausgeführt wird. Und in der Tat können wir beliebig weitere Eingaben in VFP absetzen und die Form problemlos fernsteuern:  
[code]oForm.Left = 150  
oForm.Top = 200  
[/code]

\*\*Windows API\*\*  
Damit wir die WinForm nun in die Grenzen des VFP-Hauptfenster transferieren können, benötigen wir die Fähigkeiten der Windows 32 API. Dort wird uns eine Funktion namens SetParent() zur Verfügung gestellt. Diese Funktion ermöglicht es, dass man zwei Handles in Relation zueinander setzen kann. Man vergibt lediglich ChildHandle und ParentHandle und die Funktion kümmert sich um die Neuanordnung.  
[code]\*#beautify keyword\_nochange  
\* see [https://support.microsoft.com/kb/894818/](https://support.microsoft.com/kb/894818/)

Declare Integer SetParent in Win32API ;  
Integer, Integer  
\*#beautify

\* WinForm bound to VFP main screen.  
SetParent(oForm.Handle, \_VFP.hWnd)

\* WinForm back on desktop.  
SetParent(oForm.Handle, 0)  
[/code]  
Danach kann man die Windows Form nur noch innerhalb der Abmessungen des VFP-Hauptfenster anordnen. Das entspricht FoxPro-Forms mit der Eigenschaft \*Desktop=.F.\* und \*ShowWindow=0\*. Das ParentHandle 0 repräsentiert den Desktop.

\*\*Ereignisse der WinForm an VFP melden\*\*  
Aktuell bietet der COM-Server noch keine Ereignisse. Diese können aber problemlos per Delegates und Publizierung in der Type Library realisiert werden. Der Artikel [.NET per COM nutzen](xref:net-per-com-nutzen) schneidet das Thema bereits an.

\*\*Ausblick\*\*  
Ausgehend von dem Grundgerüst der WinForm per COM sind sicherlich viele weitere Szenarien denkbar. Eine Möglichkeit ist sicherlich, dass man den COM-Server zum Starten der Windows Forms als andere Klasse definiert und mit einer Forms-Collection samt Indexer ausstattet. Dadurch erreichen wir eine bessere Referenz- und Threadkontrolle innerhalb der .NET Komponente. Im nächsten Schritt würde man die Klasse in einen FormManager konvertieren und per Reflexion die Fähigkeit integrieren, beliebige Windows Forms zu starten. Eine nette Vorstellung, oder?

\*\*Ressourcen\*\*  
[Passing objects between FoxPro and .NET COM Components](https://www.west-wind.com/presentations/dotnetfromVfp/DotNetFromVfp_ComplexObjects.asp)[/url]  
[Handling .NET Events in Visual FoxPro via COM Interop](https://www.west-wind.com/presentations/dotnetfromVfp/DotNetFromVfp_EventHandling.asp)  
[Creating Multi-threaded .NET components for COM Interop with Visual FoxPro](https://www.west-wind.com/presentations/dotnetfromVfp/DotNetFromVfp_MultiThreading.asp)

Bis denne, JoKi
