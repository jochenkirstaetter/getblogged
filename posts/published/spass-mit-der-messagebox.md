---
uid: spass-mit-der-messagebox
title: Spass mit der MessageBox()
slug: spass-mit-der-messagebox
date: 2010-01-24
status: published
type: post
description: Verwendung von Aufrufen in der Windows 32 API zur Erweiterung nativer Funktionen in Visual FoxPro. Darstellung einer Alternative für die MessageBox().
tags:
- Development
keywords: Development
metaTitle: Spass mit der MessageBox()
metaDescription: Verwendung von Aufrufen in der Windows 32 API zur Erweiterung nativer Funktionen in Visual FoxPro. Darstellung einer Alternative für die MessageBox().
image: ''
ogTitle: Spass mit der MessageBox()
ogDescription: Dieser Artikel beschreibt die Verwendung von Aufrufen in der Windows 32 API zur Erweiterung nativer Funktionen in Visual FoxPro. Konkret wird eine Alternative für die MessageBox() dargestellt. Ich...
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/spass-mit-der-messagebox/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2010-01-24T06:10:44Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Dieser Artikel beschreibt die Verwendung von Aufrufen in der Windows 32 API zur Erweiterung nativer Funktionen in Visual FoxPro. Konkret wird eine Alternative für die MessageBox() dargestellt. Ich...
twitterTitle: Spass mit der MessageBox()
twitterDescription: Dieser Artikel beschreibt die Verwendung von Aufrufen in der Windows 32 API zur Erweiterung nativer Funktionen in Visual FoxPro. Konkret wird eine Alternative für die MessageBox() dargestellt. Ich...
twitterImage: 
facebookTitle: Spass mit der MessageBox()
facebookDescription: Dieser Artikel beschreibt die Verwendung von Aufrufen in der Windows 32 API zur Erweiterung nativer Funktionen in Visual FoxPro. Konkret wird eine Alternative für die MessageBox() dargestellt. Ich...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Dieser Artikel beschreibt die Verwendung von Aufrufen in der Windows 32 API zur Erweiterung nativer Funktionen in Visual FoxPro. Konkret wird eine Alternative für die MessageBox() dargestellt. Ich hoffe, dass ihr mit der vorgestellten Lösung ein bisschen was anfangen könnt. Also, lasst uns Spass mit der MessageBox() haben...  
  
Im Gegensatz zu vielen anderen Ausgaben in Visual FoxPro ist die Darstellung der MessageBox()-Funktion kein VFP-internes Konstrukt, sondern geht auf die API-Funktionen des Betriebssystems. Damit haben wir ebenfalls die gleichen Möglichkeiten und können die MessageBox()-Funktion ein wenig verschönern bzw. erweitern.  
  
Nehmen wir folgendes Szenario: Der Anwender hat eine Aktion ausgelöst, die ihn über den gegenwärtigen Zustand und weitere Aktionsmöglichkeiten informiert. Leider kann das manchmal nicht ausreichend genug sein und der Anwender ist sich nicht im Klaren, was die eigentliche Ursache und welche Konsequenzen seine Eingabe nach sich ziehen können. Wir als Entwickler wollen den Informationsgehalt der MessageBox-Ausgabe aber nicht überfrachten. Folglich stehen wir in einem Dilemma...  
  
Schauen wir uns die MessageBox()-Funktion ein wenig genauer an.  
  
[code]MessageBox(eMessageText, nDialogBoxType, cTitleBarText, nTimeout)[/code]  
  
Mit der VFP-Version 8.0 wurde der Timeout vorgestellt. Ein nettes Features für kurzzeitige Einblendungen, ohne dass der Anwender selbst aktiv werden muss. Außerdem kann der eMessageText einen beliebigen Typ annehmen. Diese Funktionalität wollen wir selbstverständlich erhalten.  
  
Die Windows 32 API bietet in der user32.dll die zugehörigen Calls für die Erzeugung der MessageBox an. Konkret gibt es dort insgesamt fünf unterschiedliche Ausprägungen - ohne Timeout, für ANSI und für Unicode. Interessanterweise gibt es auch noch eine versteckte Funktionalität: Ein vierter Buttontyp!  
  
Dabei handelt es sich um den Hilfe-Button. Dieser wird über den Dezimalwert 16384 aktiviert. Leider können wir diese Funktionalität nicht direkt mit der vorhandenen MessageBox()-Funktion in VFP nutzen. Daher erstellen wir uns eine eigene Funktion, die diese Aufgabe übernimmt. Hierfür nutzen wir die API-Funktion MessageBoxA:  
  
[code]\*#beautify keyword\_nochange  
\* see https://support.microsoft.com/kb/894818/  
Declare Integer MessageBoxA In user32 As MessageBoxA;  
Integer, String, ;  
String, Integer  
\*#beautify[/code]  
  
Leider ist das Interface der beiden Methoden nicht identisch. Aber auch nicht schlimm, erstellen wir uns eine eigene Funktion, die diesem Umstand gerecht wird:  
  
[code]Function MessageBoxHelp(eMessageText, nDialogBoxType, cTitleBarText, nTimeout)  
Return MessageBoxA(\_VFP.HWnd, eMessageText, cTitleBarText, nDialogBoxType)  
EndFunc[/code]  
  
Amn.: In den Beispielen wird der Einfachheit wegen absichtlich auf Eingabevalidierung verzichtet. Diese sind im Download implementiert.  
  
Damit haben wir zunächst einmal wieder den Zustand bis VFP 8.0 - ohne Timeoutfähigkeit; dazu später mehr. Okay, wenn wir nun unsere Funktion aufrufen, erhalten wir immer am rechten Rand den Hilfe-Button:  
  
[code]? MessageBoxHelp("Text",0+16384,"MessageBox")[/code]  
Cool, oder? ;-)  
So, leider gibt's hier nun den ersten Haken. Das Auslösen der Schaltfläche 'Hilfe' schliesst weder den Dialog noch gibt es einen Rückgabewert. Tja, wie weiter... BindEvent() steht uns geduldig beiseite und hilft uns aus diesem Problemchen. Das Auslösen der Hilfe erfolgt über eine Windows-Message und diese können wir seit Visual FoxPro 9.0 sauber einfangen und auswerten. Wir erstellen uns einen Delegate dessen Methode wir per BindEvent() an die auftretende Windows-Message binden:  
  
[code]#Define WM\_HELP 0x0053  
  
oWM = CreateObject("WindowsMessage")  
BindEvent(0, WM\_HELP, oWM, "OnHelp")  
  
Define Class WindowsMessage As Relation  
Procedure OnHelp(nHWND As Number, nMessage As Number, nParameters1 As Number, nParameters2 As Number) As Integer  
? "Hilfe wurde ausgelöst!"  
EndProc  
EndDefine[/code]  
  
Bei Verwendung dieser Klasse bietet es sich wahrscheinlich an, dass man diese als Singleton entweder ans globale Applikationsobjekt, \_VFP oder an \_Screen aggregiert. Dadurch wird gewährleistet, dass uns das Objekt jederzeit zur Verfügung steht.  
  
Selbstverständlich kann auch die Standardschaltfläche auf die Hilfe gelegt werden. Dazu addieren wir lediglich den Wert 768 zum DialogBoxType und geniessen den Anblick.  
  
So weit, so gut... Wir wollen aber unseren Timeout wieder haben, oder? Auch hier offeriert uns die Windows 32 API entsprechende Calls: MessageBoxTimeoutA für ANSI-Ausgaben und MessageBoxTimeoutW für Unicode. Da VFP nicht so besonders gut mit Unicode kann, nehmen wir die ANSI-Variante und ergänzen unseren Declare-Bereich um die folgenden Zeilen:  
  
[code]\*#beautify keyword\_nochange  
\* see https://support.microsoft.com/kb/894818/  
Declare Integer MessageBoxTimeoutA In User32 As MessageBoxTimeoutA ;  
Integer, String, ;  
String, Integer, ;  
Integer, Integer  
\*#beautify[/code]  
  
Da wir bereits unsere eigene Funktion MessageBoxHelp haben, ergänzen wir diese lediglich um eine Kondition zur Überprüfung der Anzahl der Parameter:  
  
[code]Function MessageBoxHelp(eMessageText, nDialogBoxType, cTitleBarText, nTimeout)  
Local liResponse  
If Pcount() &lt; 4  
m.liResponse = MessageBoxA(\_VFP.HWnd, eMessageText, cTitleBarText, nDialogBoxType)  
Else  
m.liResponse = MessageBoxTimeoutA(\_VFP.HWnd, eMessageText, cTitleBarText, nDialogBoxType, 0, nTimeout)  
m.liResponse = Iif(m.liResponse &gt; 7, -1, m.liResponse)  
EndIf  
Return m.liResponse  
EndFunc[/code]  
  
Und schon können wir wieder wie gewohnt den Timeout-Parameter nutzen. Gut, schauen wir uns weitere Möglichkeiten zum Tunen der MessageBox an.  
  
Ein Feature, dass mir besonders in anderen Skript- und Programmiersprachen gefällt, ist die Möglichkeit zur Verwendung von sogenannten Escape-Sequenzen für die gebräuchlichsten Steuerzeichen, wie etwa Tabulator, Carriage Return oder Line Feed zur Gestaltung des Aufbaus einer Ausgabe. Dabei werden anstelle der Ausgabe von Chr()-Anweisungen einfach die zugehörigen Escape-Sequenzen in den Ausgabetext eingetragen. Diese werden vor der eigentlichen Ausgabe dann interpretiert und erzeugen das gleiche Ergebnis.  
  
[code]\* VFP-Variante.  
MessageBox("Das ist ein formatierter Text mit" + Chr(13) + "Zeilenumbruch und einem" + Chr(9) + "Tabulator.")  
  
\* Andere Programmiersprachen  
MessageBoxHelp("Das ist ein formatierter Text mit\nZeilenumbruch und einem\tTabulator.")[/code]  
Selbstverständlich wollen wir diese Funktionalität ebenfalls in unserer MessageBox haben. Wir sind doch alle faule Programmierer, oder etwa nicht? ;-)  
  
Wir nehmen erneut unsere Funktion MessageBoxHelp und führen vor dem Aufruf der API-Funktion ein, zwei Zeichenkettenersetzungen durch:  
  
[code]Function MessageBoxHelp(eMessageText, nDialogBoxType, cTitleBarText, nTimeout)  
Local liResponse  
eMessageText = Strtran(Transform(eMessageText), "\n", Chr(13)+Chr(10), 1, -1, 1+2)  
eMessageText = Strtran(eMessageText, "\r", Chr(13)+Chr(10), 1, -1, 1+2)  
eMessageText = Strtran(eMessageText, "\t", Chr(9), 1, -1, 1+2)  
If Pcount() &lt; 4  
m.liResponse = MessageBoxA(\_VFP.HWnd, eMessageText, cTitleBarText, nDialogBoxType)  
Else  
m.liResponse = MessageBoxTimeoutA(\_VFP.HWnd, eMessageText, cTitleBarText, nDialogBoxType, 0, nTimeout)  
m.liResponse = Iif(m.liResponse &gt; 7, -1, m.liResponse)  
Endif  
Return m.liResponse  
EndFunc[/code]  
Und schon macht die zweite Code-Zeile im vorherigen Abschnitt gleich mehr Spass. Es ist sicherlich Geschmackssache, ob man lieber mit oder ohne Escape-Sequenzen arbeiten möchte. Insofern ist es euch selbst überlassen, ob ihr dieses Feature nutzen wollt oder nicht. Ich spare mir liebend gern unnötige Tipparbeit, und nach einiger Zeit gewöhnt man sich sehr schnell an die Backslashe innerhalb der Texte.  
  
So, wir sind damit auch schon ziemlich am Ende des Artikels. Die neu erstellte Funktion MessageBoxHelp an sich bietet ja schon einige Schmankerl mehr als die MessageBox()-Funktion, die uns Visual FoxPro anbietet. Dennoch kann ich mir vorstellen, dass keiner von euch - inklusive mir - großes Interesse hat jetzt seinen gesamten Code zu durchforsten, um den Aufruf zu ändern. Glücklicherweise sind wir ja bewandernd in den Fähigkeiten von Visual FoxPro und haben uns in der Onlinehilfe den Abschnitt über Präprozessoranweisungen durchgelesen. Die neu erzeugte Methode MessageBoxHelp hat ganz bewusst die identische Schnittstelle wie die originale Funktion. Und bedingt durch diese Tatsache benötigen wir lediglich eine einzige Zeile, um alle Funktionsaufrufe zu 'verbessern':  
  
[code]#Define MessageBox MessageBoxHelp[/code]  
Okay, das war's nun mit Späßen mit der MessageBox(). Den kompletten Quellcode mit Konstantendefinitionen und der Eingabevalidierung könnt ihr euch [als Download ziehen](https://jochen.kirstaetter.name/spass-mit-der-messagebox/files/joki_MessageBoxHelp.zip).  
  
  
Bis denne, JoKi  
  
PS: Die Erweiterung der MessageBoxHelp könnte noch TextMerge() und ExecScript einschliessen. Aber wir wollen ja nicht übertreiben... :-)
