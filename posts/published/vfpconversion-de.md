---
uid: vfpconversion-de
title: VFPConversion.de
slug: vfpconversion-de
date: 2006-03-20
status: published
type: post
description: VFPConversion.de Neben der Kl&#228;rung der philosophischen Frage, ob ein VFP-Entwickler sich mit dem .NET Framework besch&#228;ftigen sollte oder nicht, gibt der zweit&#228;gige Workshop zu VFPConversion zun&#228;chst einen guten &#220;berblick &#252;ber die Vor- und Nachteile der beiden unabh&#228;ngigen Entwicklungssysteme aus dem Hause Microsoft.Die Anreise wurde bereits auf den Vortag abends geplant
tags:
- Community
keywords: Community
metaTitle: VFPConversion.de
metaDescription: VFPConversion.de Neben der Kl&#228;rung der philosophischen Frage, ob ein VFP-Entwickler sich mit dem .NET Framework besch&#228;ftigen sollte oder nicht, gibt der zweit&#228;gige Workshop zu VFPConversion zun&#228;chst einen guten &#220;berblick &#252;ber die Vor- und Nachteile der beiden unabh&#228;ngigen Entwicklungssysteme aus dem Hause Microsoft.Die Anreise wurde bereits auf den Vortag abends geplant
image: ''
ogTitle: VFPConversion.de
ogDescription: Neben der Klärung der philosophischen Frage, ob ein VFP-Entwickler sich mit dem .NET Framework beschäftigen sollte oder nicht, gibt der zweitägige Workshop zu VFPConversion zunächst einen guten...
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/vfpconversion-de/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-03-20T11:42:37Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Neben der Klärung der philosophischen Frage, ob ein VFP-Entwickler sich mit dem .NET Framework beschäftigen sollte oder nicht, gibt der zweitägige Workshop zu VFPConversion zunächst einen guten...
twitterTitle: VFPConversion.de
twitterDescription: Neben der Klärung der philosophischen Frage, ob ein VFP-Entwickler sich mit dem .NET Framework beschäftigen sollte oder nicht, gibt der zweitägige Workshop zu VFPConversion zunächst einen guten...
twitterImage: 
facebookTitle: VFPConversion.de
facebookDescription: Neben der Klärung der philosophischen Frage, ob ein VFP-Entwickler sich mit dem .NET Framework beschäftigen sollte oder nicht, gibt der zweitägige Workshop zu VFPConversion zunächst einen guten...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Neben der Klärung der philosophischen Frage, ob ein VFP-Entwickler sich mit dem .NET Framework beschäftigen sollte oder nicht, gibt der zweitägige Workshop zu VFPConversion zunächst einen guten Überblick über die Vor- und Nachteile der beiden unabhängigen Entwicklungssysteme aus dem Hause Microsoft.

Die Anreise wurde bereits auf den Vortag abends geplant und so konnten wir auch ganz locker mit einem Frühstück den heutigen Tag starten. Als Redner geben heute wOOdy, Markus und Gerhard die Unterschiede zum Besten. Als Einstieg gab's einen kurzen Statusbericht zu Visual\_FoxPro und dessen Zukunft. Keine Sorge, diese sieht für die nächsten Jahre auf alle Fälle positiv aus. Zum einen läuft VFP auf den kommenden Betriebssystemen wie etwa Windows Vista und zum anderen besteht ein Produktsupport bis zum Jahr 2014, der von Microsoft zugesichert ist. Ergänzend dazu hat VFP eine sehr starke und vor allem aktive Community, die alle Weichen stellt und alternative Lösungen anstreben wird, dass das Produkt weiterhin stark am Markt bleibt. Hier sind nur mal einige genannt: [deutschsprachige Foxpro User Group](https://www.dfpug.de) (dFPUG), die Programminitiative unter dem Codenamen [SednaX](https://www.sednax.com), welche künftig unter VFPX firmieren wird, sowie [FoxWiki](https://fox.wikis.com).

Im nächsten Spielzug zeigte Markus zunächst einmal den grundsätzlichen Aufbau des .NET Konzeptes. Ja, Konzept, denn das Framework und dessen Komponenten sind im eigentlichen Sinne lediglich Bausteine eines größeren Bildes.  
Das Fundament bildet in diesem Zusammenhang die Common Language Runtime (CLR), welche bildhaft als "virtueller Prozessor" verstanden werden kann. Sie bildet sozusagen die Basis bzw. den Sandkasten zum Ausführen des Code. Durch Einstellungen in Bezug auf Rechte, Zugriffe und Richtlinien formt die CLR die Arbeitsumgebung einer .NET Applikation.  
Darauf aufsetzend ist die Intermediate Language (IL) aktiv, welche sozusagen den kompilierten Code der bekannten .NET Programmiersprachen repräsentiert. Der IL-Code wird dann innerhalb der CLR ausgeführt und ist damit der eigentliche Motor.  
Die nächste Stufe des Konzepts steht in Form der Base Class Libraries (BCL) zur Verfügung. Hierbei handelt es sich um, hm, sagen wir mal zwei Mengen von Klassen. Wir haben zum einen die grundsätzlichen "Basisklassen" und "Datentypen" wie etwa String, Integer, Datetime, etc. und zum anderen die komplexeren Klassendefinitionen wie etwa ArrayList, Form, etc.  
Erst jetzt kommt die Qual der Wahl für den Entwickler in Bezug auf die Programmiersprache, in der man sich austoben bzw. verwirklichen möchte. Da alle .NET Programmiersprachen de facto auf den vorher genannten Bausteinen aufsetzen und letztendlich durch den sprachbezogenen Compiler in IL-Code konvertiert werden, stellt sich letztendlich nur die Geschmacksfrage. Der Rest ist Seife... ;-) C# und VB.NET sind dabei zwar die bekanntesten Vertreter jedoch gibt es gegenwärtig über 50 unterschiedliche Programmiersprache, die eigenständig in IL-Code übersetzen können. Leider(?) gehört Visual\_FoxPro nicht dazu. Meine persönliche Favoriten sind C# (auch weil Großteile der BCL in C# geschrieben sind) und IronPython. Prinzipiell macht es keinen technischen Unterschied in welcher .NET Sprache die Aufgabe gelöst. Auch die Performance zwischen den unterschiedlichen Sprachen ist uninteressant, da letztendlich immer IL-Code produziert und ausgeführt wird.  
Da wir uns nun für einen Dialekt entschieden haben, steht uns die nächste Entscheidung ins Haus: Welche Entwicklungsumgebung? Die bekannteste und wahrscheinlich auch teuerste Variante ist sicherlich Visual Studio 2005, mal abgesehen von den kostenfreien Express-Editionen. Alternativ gibt's noch SharpDevelop und andere. Für Puristen steht selbstverständlich Notepad zur Verfügung. Also auch wiederum alles nur eine Frage der persönlichen Vorlieben, Anforderungen und der Größe des Geldbeutels. Ich möchte hier noch einmal explizit auf die kostenfreien Express-Editionen von Visual Studio 2005 hinweisen. Hierbei handelt es sich um funktionsreduzierte Entwicklungsumgebungen für eine Sprache. Primär sind die Express-Editionen für Schüler, Studenten und Hobbyprogrammierer angedacht, jedoch spricht nichts gegen die professionelle Verwendung.

Fliessend sind wir in die Gegenüberstellung der sprachlichen Differenzen zwischen Visual\_FoxPro und Visual\_Basic.Net übergegangen. Anhand kleinerer Demos zeigte Markus, wie man sehr leicht mit den Assistenten vom Visual Studio 2005 eine WinForms- oder Konsolenanwendung geschrieben. Spassigerweise gleich in voller Breitseite, da er in seinem Hauptprojekt in VB.Net eine neu erstellte C#-Referenz eingebunden hat. Auch hier die Live-Demonstration im Debugger, dass die unterschiedlichen .Net-Dialekte miteinander genutzt werden können.

Okay, genug für die erste Häfte des Tages: Mittagessen...

Ein wenig vollgestopft und leicht schläfrig, hm, sorry aber der Nachtisch in Form von Mousse au Vanille und Götterspeise mit Vanillecreme war einfach zu verlockend. Well, wir werden aktiv an der Diskussion dran bleiben und die Müdigkeit ein wenig mit dem Schreiben dieses Blogeintrags vertreiben. Hm, das erinnert mich spontan an Instant-Blogging ;-) Ich berichte euch während die Gegenwart läuft...

Inzwischen ist Gerhard am Drücker und "wiederholt" quasi einen Teil der Session von heute morgen - nur zum Aufzeigen der Ähnlichkeiten und Unterschiede zwischen Visual\_FoxPro und C#. Eigentlich noch wenig Neues im Großen und Ganzen.
