---
uid: design-pattern-decorator
title: 'Design Pattern: Decorator'
slug: design-pattern-decorator
date: 2005-12-03
status: published
type: post
description: 'Mmal wieder einen technischen Eintrag zu den Möglichkeiten der Umsetzung von Design Patterns in Visual FoxPro. Der Eintrag erläutert die Implementierung des Decorator (deutsch: Dekorierer).'
tags:
- Development
keywords: Development
metaTitle: 'Design Pattern: Decorator'
metaDescription: 'Mmal wieder einen technischen Eintrag zu den Möglichkeiten der Umsetzung von Design Patterns in Visual FoxPro. Der Eintrag erläutert die Implementierung des Decorator (deutsch: Dekorierer).'
image: ''
ogTitle: 'Design Pattern: Decorator'
ogDescription: 'Okay, heute mal wieder einen technischen Eintrag zu den Möglichkeiten der Umsetzung von Design Patterns in Visual FoxPro. Der Eintrag erläutert die Implementierung des Decorator (deutsch: Dekorierer)...'
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
canonicalUrl: https://jochen.kirstaetter.name/design-pattern-decorator/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2005-12-03T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: 'Okay, heute mal wieder einen technischen Eintrag zu den Möglichkeiten der Umsetzung von Design Patterns in Visual FoxPro. Der Eintrag erläutert die Implementierung des Decorator (deutsch: Dekorierer)...'
twitterTitle: 'Design Pattern: Decorator'
twitterDescription: 'Okay, heute mal wieder einen technischen Eintrag zu den Möglichkeiten der Umsetzung von Design Patterns in Visual FoxPro. Der Eintrag erläutert die Implementierung des Decorator (deutsch: Dekorierer)...'
twitterImage: 
facebookTitle: 'Design Pattern: Decorator'
facebookDescription: 'Okay, heute mal wieder einen technischen Eintrag zu den Möglichkeiten der Umsetzung von Design Patterns in Visual FoxPro. Der Eintrag erläutert die Implementierung des Decorator (deutsch: Dekorierer)...'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Okay, heute mal wieder einen technischen Eintrag zu den Möglichkeiten der Umsetzung von Design Patterns in Visual FoxPro. Der Eintrag erläutert die Implementierung des Decorator (deutsch: Dekorierer). Schauen wir uns zuerst die [Definition von Wikipedia](https://de.wikipedia.org/wiki/Dekorierer) an:

*Die Instanz eines Dekorierers wird vor die zu dekorierende Klasse geschaltet. Der Dekorierer hat die gleiche Schnittstelle wie die zu dekorierende Klasse. Aufrufe an den Dekorierer werden dann verändert oder unverändert weitergeleitet (Delegation), oder sie werden komplett in Eigenregie verarbeitet. Der Dekorierer ist dabei "unsichtbar", da der Aufrufende gar nicht mitbekommt, dass ein Dekorierer vorgeschaltet ist.*

VFP bietet hier einen interessanten Lösungsansatz über die '\_Access'-Funktionalität an. Es handelt sich dabei im eigentlichen Sinne um einen 'get'-Mechanismus, wie man es beispielsweise von Java respektive C# kennt. In VFP kann man nun eine Funktion namens 'This\_Access' schreiben, welche permanent bei einem Zugriff auf das Objekt evaluiert wird. Es handelt sich dabei um einen impliziten Mechanismus, der ideal für das Decorator Design Pattern geeignet ist. Wichtig ist, dass man immer bei This\_Access ein Objekt als Rückgabetyp liefert. Schliesslich würde 'This' immer einem Objekt entsprechen. Nun, unter Berücksichtigung dieser Annahmen implementieren wir mal einen ersten Entwurf für den Decorator:  
[code]\*==========================================================================  
Define Class Decorator As Session OlePublic  
\*==========================================================================  
DataSession = 1  
\*--- Die Eigenschaft des Dekorierten kann, muss aber nicht, auf  
\*--- Protected gesetzt werden. Es kommt ganz darauf an, ob man  
\*--- dem Interface den Zugriff auf das 'interne' Objekt gestattet  
\*--- oder nicht. Bei den OLEClass-Klassen von VFP steht das Decorated-  
\*--- Objekt in der Eigenschaft This.Object zur Verfügung.  
\*--- Protected oDecorated  
oDecorated = .Null.

\*--- Wir bieten zwar die Möglichkeit an, dass das dekorierte Objekt  
\*--- direkt bei der Instanzierung aggregiert bzw. referenziert werden  
\*--- kann; müssen jedoch berücksichtigen, dass das COM-Interface keine  
\*--- Parameters akkzeptiert. Daher gibt's additiv die Methode  
\*--- This.SetDecorated() zur Erfüllung der gleichen Aufgabe.  
Function Init( toDecorated As Object ) As Boolean  
This.oDecorated = toDecorated  
Endfunc

Function Destroy() As Boolean  
This.oDecorated = .Null.  
Endfunc

\*--- Setzt das zu dekorierende Objekt zur Laufzeit. Über diese  
\*--- Methode können auch multiple Objekte geswitched werden. Wir  
\*--- haben also die Möglichkeit zum 'Recycling' des Decorators.  
Function SetDecorated( toDecorated As Object ) As VOID ;  
HelpString "Setzt das zu dekorierende Objekt des Decorator. Diese Methode muss bei COM-Zugriff genutzt werden."  
This.oDecorated = .Null.  
This.oDecorated = toDecorated  
Endfunc

\*--- Eigentliche Funktionalität des Decorators. Über die VFP-Funktionalität  
\*--- von "\_Access" kann der selektive Zugriff auf den Decorator bzw. dessen  
\*--- zu dekorierendes Objekt reguliert werden. Die Arbeitsweise sieht so aus,  
\*--- Zugriffe wie etwa 'This.Width' je nach Existenz der Eigenschaft 'Width'  
\*--- zuerst am Decorator getestet werden und dann an das interne Objekt geleitet  
\*--- werden.  
Function THIS\_ACCESS( tcMember As String ) As Object;  
HelpString "Ermöglicht den geswitchten Zugriff auf das eigene bzw. zu dekorierende Objekt."  
If Pemstatus(This, Upper( tcMember ), 5 )  
Return This  
Else  
Return This.oDecorated  
Endif  
Endfunc  
Enddefine  
[/code]  
Sieht doch schon recht vernünftig und brauchbar aus, oder? Effektiv ist unser Decorator damit vollständig implementiert und wir können uns neuen Ufern zuwenden... 😎

Wichtig bei der obigen Implementierung ist, dass die Eigenheiten des COM-Interface direkt berücksichtigt werden. Ich nenne es mal ein Dual-Interface für VFP-internen Nutzen und COM-Nutzen. Selbstverständlich kann man das COM-Interface noch mittels entsprechender \_COMATTRIB-Definitionen vernünftig ausformulieren, aber diesen Task überlasse ich euch als Hausaufgaben.

So, wozu kann man den Decorator überhaupt nutzen?  
Nun, die Einsatzmöglichkeiten sind vielfältig. Dennoch wird der Decorator vorrangig zur Erweiterung von Objekten genutzt, sofern keine Ableitungen gebildet werden können. Das ist gerade im Zusammenhang mit ActiveX-Controls (siehe auch VFP OleClass und OleClassBound) sowie Klassen dritter Anbieter interessant. Aber auch zur Erweiterung von Standard-Objekten in VFP eignet sich der Decorator hervorragend. Ich möchte euch mal exemplarisch die Nutzung mit dem Scatter-Objekt zeigen.

Also, das Scatter-Objekt zur objektbasierten Repräsenz eines Datensatz hat ja schon einige Vorzüge, aber IMHO fehlt etwas extrem wichtiges: Methoden.  
Das Scatter-Objekt besitzt lediglich Eigenschaften gemäß den Feldern des genutzten Alias, aber keinerlei Methoden. Und hier kommt nun das Decorator-Ppattern ins Spiel. Statt der direkten Verwendung des Aufruf  
[code]Scatter Memo Name loScatter[/code]  
Nutzt man eine Ableitung des Decorator mit der gleichen respektive erweiterten Funktionalität. Hier zunächst mal die Klassendefinition des 'ScatterDecorator':  
[code]\*==========================================================================  
Define Class ScatterDecorator As Decorator  
\*==========================================================================  
Procedure Scatter  
Scatter Name This.oDecorated Memo  
EndProc

Procedure Gather  
Gather Name This.oDecorated Memo  
EndProc  
EndDefine  
[/code]  
That's all folks. Einfach eine Ableitung unserer abstrakten Decorator-Klasse und Methoden für die beiden Befehle Scatter und Gather erzeugt. Bereits jetzt haben wir eine identische Repräsentanz eines nativen Scatter-Objekts in einem Decorator - das Interface ist identisch!

Okay, aber welchen echten Nutzen haben wir über diesen Weg? Ganz einfach... Unsere Klasse ScatterDecorator können wir beliebig mit weiteren Methoden erweitern. Ich nutze beispielsweise gerne eine Methode namens 'This.IsNew', die mir direkt Auskunft darüber gibt, ob ein Datensatz einen bestimmten Zustand inne hat. Oder denkbar wären weitere Informationen über die Tabellenstruktur, auf der das ScatterDecorator-Objekt basiert: This.TableAlias(), This.PrimaryKey(), This.Copy, This.Blank(), This.Next(), This.Previous(), etc...

Ich hoffe, dass die Idee rübergekommen ist.

Schauen wir uns nun mal die ScatterDecorator-Klasse im Einsatz an:  
[code]\*==========================================================================  
\* Sample for ScatterDecorator  
\*==========================================================================  
Use (Home(0) + "foxcode.dbf")  
Locate For Abbrev = "SCAN"

oRec = Createobject('ScatterDecorator')  
oRec.Scatter()  
Wait Window oRec.Data && This works fine!

Scatter Name oScatter  
Wait Window oScatter.Data

Dimension myArr[3]  
myArr[1] = Createobject('ScatterDecorator')  
myArr[1].Scatter  
Wait Window myArr[1].Data && This fails with "Property 'MemoField' is not found"  
oRec2 = myArr[1]  
Wait Window oRec2.Data && This works fine!  
[/code]  
Wie ihr sehen könnt, besteht keinerlei Unterschied zwischen den Ausgaben von oRec.Data und oScatter.Data. Der Decorator leitet die Aufrufe direkt durch und produziert daher das gleiche Resultat. Kleiner Nebeneffekt: Man spart sich die ganzen Optionen des Scatter-Befehls - 😁 - Diese sind in der Klassendefintion des Decorators hinterlegt.

Achja, nur so als Anregung... Ist doch ziemlich cool, wenn man dem Empty-Objekt ebenfalls Methoden verpassen kann, oder? Ich kann mir ehrlich gesagt nicht vorstellen, dass ihr bisher noch nie in die Situation gelaufen seid, dass man zwar ein Empty-Objekt nutzen will, sofern es Methoden besitzen würde... Oder? Auch hier ist das Decorator Design Pattern optimal geeignet:  
[code]\*==========================================================================  
Define Class EmptyDecorator As Decorator  
\*==========================================================================  
\*--- Überlagerung der Init-Methode, da wir direkt mit einem  
\*--- Empty-Objekt als dekoriertem Objekt starten wollen. Falls  
\*--- also kein Objekt reinkommt, erzeugen wir uns selbst eins.  
Function Init( toDecorated As Object ) As Boolean  
Local loDecorated  
m.loDecorated = m.toDecorated

If Pcount() == 0 Or Not Vartype( m.loDecorated ) == 'O'  
m.loDecorated = CreateObject("Empty")  
EndIf  
Return Dodefault( m.loDecorated )  
EndFunc

Function IsValid() As Boolean  
\* Irgendwelche Prüfungen...  
EndFunc

Function AddProperty( tcMember As String, tuValue As Variant ) As Boolean  
Return AddProperty( This, tcMember, tuValue )  
EndFunc  
[/code]  
Die Implementierung für einen EmptyDecorator ist sicherlich kontextspezifisch. Dennoch ergeben sich über diesen Ansatz weitere Freiheitsgrade in der Programmierung und vorallem effizienteren Nutzung von 'leeren' Objekten. Und man umgeht eine leidige Unzulänglichkeit von VFP: Aktuell ist keine Ableitung von Empty möglich:  
[code]\*==========================================================================  
Define Class Transfer As Empty  
\*==========================================================================  
[/code]  
Das ist leider nicht möglich, aber bei der Nutzung des EmptyDecorator kommen wir dennoch in den gewünschten Bereich:  
[code]\*==========================================================================  
Define Class Transfer As EmptyDecorator  
\*==========================================================================  
[/code]  
Yeah, let's rock the code...

Ich hoffe, dass ich euch eine Idee über den theoretischen Aufbau, die Implementierung und den technischen Nutzen des Decorators in diesem Artikel vermitteln konnte. Mein Fazit in diesem Zusammenhang ist, dass dieses Pattern immens Vorteile bringen kann und bereits integrierter Bestandteil von Visual FoxPro - OleClass und OleBoundClass - ist. Sobald man also ActiveX-Controls in seinem Projekt benutzt, verwendet man bereits einen Decorator. 😎

Über ein bisschen Feedback würde ich gerne freuen. Für welchen Einsatzzweck nutzt ihr einen Decorator oder würdet ihn nutzen?  
Bis denne, JoKi

PS: Ich muss die Klassen noch ein wenig ausformulieren, aber dann stehen diese als Attachment hier zur Verfügung.
