---
uid: anmerkungen-zum-decorator
title: Anmerkungen zum Decorator Design Pattern
slug: anmerkungen-zum-decorator
date: 2006-11-01
status: published
type: post
description: 'Anmerkungen zum Decorator Anscheinend bedarf es der regelm&#228;&#223;igen Wiederholung von Themen, die man im t&#228;glichen Einsatz als Entwickler gebrauchen k&#246;nnte. Wiederholung vertieft das Wissen und schadet sicherlich nicht. Die nachfolgenden Anmerkungen beziehen sich auf meinen Artikel zum [url=/Design-Pattern-Decorator]Design Pattern: Decorator[/url]. Es empfiehlt sich den Beitrag kurz durchzugehen, sofern der Decorator'
tags:
- Community
keywords: Community
metaTitle: Anmerkungen zum Decorator Design Pattern
metaDescription: 'Anmerkungen zum Decorator Anscheinend bedarf es der regelm&#228;&#223;igen Wiederholung von Themen, die man im t&#228;glichen Einsatz als Entwickler gebrauchen k&#246;nnte. Wiederholung vertieft das Wissen und schadet sicherlich nicht. Die nachfolgenden Anmerkungen beziehen sich auf meinen Artikel zum [url=/Design-Pattern-Decorator]Design Pattern: Decorator[/url]. Es empfiehlt sich den Beitrag kurz durchzugehen, sofern der Decorator'
image: ''
ogTitle: Anmerkungen zum Decorator Design Pattern
ogDescription: Anscheinend bedarf es der regelmäßigen Wiederholung von Themen, die man im täglichen Einsatz als Entwickler gebrauchen könnte. Wiederholung vertieft das Wissen und schadet sicherlich nicht. Die...
layout: post
bodyClass: post-template tag-community
postClass: post tag-community
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
canonicalUrl: https://jochen.kirstaetter.name/anmerkungen-zum-decorator/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-11-01T13:01:59Z
updatedAt: 2023-09-18T00:55:51Z
excerpt: Anscheinend bedarf es der regelmäßigen Wiederholung von Themen, die man im täglichen Einsatz als Entwickler gebrauchen könnte. Wiederholung vertieft das Wissen und schadet sicherlich nicht. Die...
twitterTitle: Anmerkungen zum Decorator Design Pattern
twitterDescription: Anscheinend bedarf es der regelmäßigen Wiederholung von Themen, die man im täglichen Einsatz als Entwickler gebrauchen könnte. Wiederholung vertieft das Wissen und schadet sicherlich nicht. Die...
twitterImage: 
facebookTitle: Anmerkungen zum Decorator Design Pattern
facebookDescription: Anscheinend bedarf es der regelmäßigen Wiederholung von Themen, die man im täglichen Einsatz als Entwickler gebrauchen könnte. Wiederholung vertieft das Wissen und schadet sicherlich nicht. Die...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Anscheinend bedarf es der regelmäßigen Wiederholung von Themen, die man im täglichen Einsatz als Entwickler gebrauchen könnte. Wiederholung vertieft das Wissen und schadet sicherlich nicht. Die nachfolgenden Anmerkungen beziehen sich auf meinen Artikel zum [url=/Design-Pattern-Decorator]Design Pattern: Decorator[/url]. Es empfiehlt sich den Beitrag kurz durchzugehen, sofern der Decorator nicht geläufig sein sollte.

Den Auslöser für diesen Blogeintrag liefert mal wieder eine Unterhaltung im [Forum der dFPUG](https://forum.dfpug.de). Dort wurde sinngemäß das Problem formuliert wie man gemeinsame Funktionalität zweier unterschiedlich abgeleiteter Klassen ohne Codedopplung umsetzen könnte, aber dennoch die sonstigen PEMs der Hierarchie erhalten kann. Da es in Visual FoxPro das Konzept der Mehrfachvererbung - Stichwort partial class in C# - leider nicht gibt, sehen die Alternativen zur Umsetzung ein wenig anders aus:

[ulist]  
Code-Dopplung (wollen wir ja nicht)  
Funktionalität in aggregierte Klasse auslagern (Zugriff auf Eigenschaften/Methoden erschwert)  
Funktionalität durch Klasse vorschalten (Decorator)  
[/ulist]

Sofern ich den [Original-Thread](https://forum.dfpug.de/threads.afp?msgid=694197&complete=ON&sec=51&tid=191434) korrekt verstanden habe, erscheint mir die Anwendung des Decorator an sinnvollsten, da wir hier entsprechende Funktionalität ohne Code-Dopplung erreichen können.

Wir lagern also die 'gemeinsame' Methode für die Klassen in unterschiedlichen Ableitungshierarchien in eine eigene Klasse aus, und wenden das Decorator Design Pattern an. Ich versuche es mal mit einem 'konstruierten' Code-Beispiel zu verdeutlichen:  
[code]\*====================================================================  
\* Anwendung des Decorator Design Pattern für die 'Simulation' von  
\* Mehrfachvererbung.  
\* Decorator-Klasse stammt aus dem Blogartikel zum Design Pattern:  
\* [/Design-Pattern-Decorator](xref:design-pattern-decorator)  
\*====================================================================  
Clear  
Set Procedure To Decorator.prg Additive

oKatze = CreateObject("DemoDecorator", CreateObject("Katze"))  
oBambus = CreateObject("DemoDecorator", CreateObject("Bambus"))

? "Katze:"  
? oKatze.Futtern()  
? oKatze.Wachsen()  
? oKatze.Futtern()  
?  
? "Bambus:"  
? oBambus.Wachsen()  
? oBambus.Wachsen()  
? oBambus.Wachsen()  
? oBambus.Wachsen()  
? oBambus.Bluehen()

\*------------------------------------------------------------------  
\* Decorator mit der ausgelagerten Funktion für beide Klassen  
\* der unterschiedlichen Ableitungshierachien.  
\*------------------------------------------------------------------  
Define Class DemoDecorator As Decorator Of "Decorator.prg"  
Function Wachsen()  
If Vartype(This.oDecorated) == "O"  
\*... gleiches Verhalten für beliebige Objektreferenz.  
Return "Höher, und immer höher..."  
EndIf  
EndFunc  
EndDefine

\*------------------------------------------------------------------  
\* Eine Klasse der ersten Ableitungshierarchie  
\* (vereinfachte Darstellung - As &lt;ParentClass&gt; kann beliebig sein.  
\*------------------------------------------------------------------  
Define Class Katze As Custom && As CSaeugetier  
Function Futtern()  
Return "Satt..."  
EndFunc  
EndDefine

\*------------------------------------------------------------------  
\* Eine Klasse der zweiten Ableitungshierarchie  
\*------------------------------------------------------------------  
Define Class Bambus As Custom && As CPflanze  
Function Bluehen()  
Return "Volle Pracht erreicht."  
EndFunc  
EndDefine  
[/code]  
Das Ergebnis entspricht nach meinem Verständnis der formulierten Anforderung im Forum-Beitrag.

Im weiteren Verlauf kamen noch einige Ideen und Fragen auf:

\*Das greift für alles? Für Properties und Methoden?\*  
Nach meinem VFP-Wissen, ja. Sämtliche Zugriffe von außen auf die Objektreferenz werden zuerst in This\_Access geleitet. Die dortige Fallunterscheidung muss immer ein Objekt zurückliefern. Dieses könnte ehrlich gesagt auch zur Laufzeit dynamisch aggregiert sein, oder auf irgendeine Objektreferenz zeigen. Hauptsache der Rückgabetyp ist ein Objekt.

\*Mit Deiner Decorator-Klasse müßte man das eigentlich 2stufig anlegen, auch das ginge ja, da THIS\_ACCESS dann kaskadiert. (...) Das verschmelzen der beiden Objekte zu einem ist also nur von außen gesehen perfekt. Es fehlt doch aber eigentlich nur eine oDecorator\_Access Methode, die nochmal dass gleiche macht, oder seh ich das falsch?  
\*  
Nun, ich hatte es im ursprünglichen Artikel zum Decorator nicht probiert. Der nachfolgende Code zeigt, dass eine solche Kaskadierung leider nicht möglich ist:  
[code]\*====================================================================  
\* (Nicht-)Kaskadierung von mehreren Decorator Design Pattern.  
\*====================================================================  
Clear  
Set Procedure To Decorator.prg Additive  
Set Procedure To Decorator\_Demo.prg Additive

oKatze = CreateObject("DemoDecorator", CreateObject("Katze"))  
oBambus = CreateObject("BambusDecorator", oKatze)  
oSpatz = CreateObject("VogelDecorator", oBambus)

? oSpatz.Wachsen()  
? oSpatz.Wachsen()  
? oSpatz.Bluehen()  
? oSpatz.Futtern() && Problem!  
? oSpatz.Fliegen()

\*------------------------------------------------------------------  
\* Kaskadierender Decorator  
\* Decorator-Klasse stammt aus dem Blogartikel zum Design Pattern:  
\* [/Design-Pattern-Decorator](xref:design-pattern-decorator)  
\*------------------------------------------------------------------  
Define Class CascadeDecorator As Decorator Of "Decorator.prg"  
Function THIS\_ACCESS( tcMember As String ) As Object;  
HelpString "Ermöglicht den geswitchten Zugriff auf das eigene bzw. zu dekorierende Objekt."  
Local loReturn

If Pemstatus(This, Upper( tcMember ), 5 )  
m.loReturn = This  
Else  
m.loReturn = This.oDecorated  
If Not PemStatus(m.loReturn, Upper( tcMember ), 5 )  
m.loReturn = m.loReturn.oDecorated  
\* m.loReturn = m.loReturn.oDecorated.&tcMember.  
EndIf  
EndIf  
  
Return m.loReturn  
Endfunc

Function Wachsen()  
If Vartype(This.oDecorated) == "O"  
\*... gleiches Verhalten für beliebige Objektreferenz.  
Return "Höher, und immer höher..."  
EndIf  
EndFunc  
EndDefine

\*------------------------------------------------------------------  
\* Äußerer Decorator  
\*------------------------------------------------------------------  
Define Class VogelDecorator As CascadeDecorator  
Function Fliegen()  
Return "Über den Wolken..."  
EndFunc  
EndDefine

\*------------------------------------------------------------------  
\* Eine Klasse der zweiten Ableitungshierarchie  
\* Muss nun selbst als Decorator fungieren.  
\*------------------------------------------------------------------  
Define Class BambusDecorator As CascadeDecorator && As CPflanze  
Function Bluehen()  
Return "Volle Pracht erreicht."  
EndFunc  
EndDefine

\*------------------------------------------------------------------  
\* Eine Klasse der ersten Ableitungshierarchie  
\* (vereinfachte Darstellung - As &lt;ParentClass&gt; kann beliebig sein.  
\*------------------------------------------------------------------  
Define Class Katze As Custom && As CSaeugetier  
Function Futtern()  
Return "Satt..."  
EndFunc  
EndDefine  
[/code]  
Die Begrenzung wird durch den Parameter an die jeweilige Access-Methode limitiert. Bisher konnte ich lediglich eine Verkettung über maximal 2 Stufen erreichen, danach gibt's Probleme durch den Rückgabewert.

Es stellt sich sicherlich auch die generelle Frage, welchen Sinn diese Kaskadierung haben sollte. Ich finde, dass im Falle einer hierarchischen Abhängigkeit ein anderes Design Pattern interessanter sein dürfte: Chain Of Responsibility.

Falls es doch jemand gelingen sollte, eine bessere Lösung in Bezug zur Kaskadierung auszutüfteln, bitte ich um Feedback, da es mich trotz meiner bisherigen Bemühungen auf alle Fälle interessiert.  
Bis denne, JoKi
