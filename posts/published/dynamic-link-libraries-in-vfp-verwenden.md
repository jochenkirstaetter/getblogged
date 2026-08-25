---
uid: dynamic-link-libraries-in-vfp-verwenden
title: Dynamic-Link Libraries in VFP verwenden
date: 2006-04-19
status: published
type: post
description: Dynamic-Link Libraries in VFP verwenden Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen.
tags:
- Development
keywords: Development
metaTitle: Dynamic-Link Libraries in VFP verwenden
metaDescription: Dynamic-Link Libraries in VFP verwenden Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen.
image: ''
ogTitle: Dynamic-Link Libraries in VFP verwenden
ogDescription: Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum...
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
canonicalUrl: https://jochen.kirstaetter.name/dynamic-link-libraries-in-vfp-verwenden/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-19T01:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum...
twitterTitle: Dynamic-Link Libraries in VFP verwenden
twitterDescription: Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum...
twitterImage: 
facebookTitle: Dynamic-Link Libraries in VFP verwenden
facebookDescription: Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum Stammtisch - [https://speyer.dfpug.de](https://speyer.dfpug.de/) - und meiner Erinnerungsmail sollte sich der Abend mit dem Internet Explorer in VFP-Anwendungen beschäftigen. Nun, sollte... irgendwie habe ich es verpeilt, dass Jörg bereits im März mir zur Kenntnis gab, dass er diese Woche in Urlaub ist, und daher nicht zur Verfügung steht. Gut, alternativ hätte man dann Automation von Microsoft Winword für Druckausgaben anstreben können. Aber Moment mal, da wäre Jörg ebenfalls als Redner aktiv gewesen. Herrje, wieder nichts, okay, dann eben Plan B und das zweite Thema vom März - Dynamic-Link Libraries in VFP verwenden - nachholen.  
  
Ihr könnt euch vielleicht vorstellen, dass wir hiermit den zweiten Satz der Thermodynamik ziemlich gut erfüllt haben. Nun, zumindest stand der Termin; wie bisher immer am 3. Mittwoch des Monats. Pünktlich um 19:30 durften wir uns im frisch renovierten (großen) Nebenraum unseres Lokals versammeln und loslegen. Zunächst wie üblich die Neuigkeiten aus der Community:  
  
* Usergroupunterstützung durch O'Reilly und MS Press  
* Infos von CLIP und der INETA  
* Ausblick auf die Regionalleitertreffen von PASS und dFPUG  
  
Ein paar Nachzügler trafen noch ein und dann konnten wir auch direkt mit dem Thema des heutigen Abends loslegen: Dynamic-Link Libraries (DLLs). Laut MSDN sind DLLs 'lediglich' Module mit ausgelagerten Funktionen und Daten, welche von anderen DLLs oder Anwendungen genutzt werden können. Klingt im ersten Moment sehr stark nach Prozedurenbibliotheken und APP-Projekten in Visual FoxPro, und im zweiten Augenblick hat sich auch kaum etwas geändert. Einzig der Umstand, dass DLLs in zwei verschiedenen Ausprägungen vorliegen können. Ich beleuchte Dynamic-Link Libraries hier nur im Zusammenspiel mit den Eigenheiten von VFP und nicht allgemein für andere Programmiersprachen. In VFP können DLLs über zwei unterschiedliche Wege genutzt werden:  
  
* Declare Befehl  
* CreateObject(), NewObject() oder GetObject() Instanzierung über COM  
  
## Declare
Über den Declare-Befehl können wir direkt auf die exportierten Funktionen einer Bibliothek zugreifen und diese in den eigenen Speicher laden. Das Ganze passiert dann In-Process und die deklarierten Funktionen stehen dem Entwickler wie normale VFP-Funktionen zur Verfügung. Man kann sich mittels des Befehls DISPLAY DLLS über die aktuell zur Verfügung stehenden Funktionen informieren. Hier mal ein simples Beispiel:  
  
` Declare Integer Sleep In kernel32.dll ;  
Integer  
  
Sleep(4000) && 4 Sekunden warten  
  
Clear Dlls "Sleep"  
`  
  
Wir laden uns die exportierte Funktion Sleep aus der kernel32.dll in unsere Anwendung, führen sie dann mit einem Parameter (gemäß Deklaration) aus, und entfernen sie abschließend wieder. Das gleiche Verhalten wie beim Aufruf einer Funktion in einer VFP-Prozedurendatei, welche mittels Set Procedure To referenziert wurde. Der Verweis auf die DLL erfolgt normalerweise ohne Pfadangaben, kann aber auch Pfadinformationen nutzen. Ohne Pfad sucht VFP die DLL an den üblichen Stellen im Betriebssystem und verweigert erst die Ausführung, falls wirklich nichts zu finden ist. Das kann potentiell zu Problemen führen, falls unterschiedliche Versionen der gleichen DLL vorliegen. Hier gilt es dann mittels DISPLAY DLLS zu prüfen, welche physikalische Datei herangezogen wurde.  
  
## COM-Schnittstelle
Die zweite Art der Nutzung von Dynamic-Link Libraries in VFP kann über die COM-Schnittstelle erfolgen. Hier gelten dann de facto die gleichen Regeln wie der OLE Automation. Objektreferenz auf die Klassendefinition erzeugen, Methoden mit passenden Parameter ausführen und die Rückgabewerte interpretieren. Im letzten Beitrag [.NET per COM nutzen](xref:net-per-com-nutzen) habe ich genau diesen Fall bereits ausführlicher beschrieben.  
  
## Hilfsmittel erleichtern die Arbeit
Oftmals steht man am Anfang vor dem Problem überhaupt Informationen zur vorliegenden DLL zu erhalten. Denn entweder kennt man die Funktionen einer Bibliothek überhaupt nicht, oder es liegen zu wenige Informationen oder Dokumentation vor. Meine gegenwärtige Vorgehensweise ist die, dass ich zuerst die DLL im [Dependency Walker](https://www.dependencywalker.com/) öffne und nachschaue, ob exportierte Funktionen vorliegen. Falls ja, okay, dann kann ich mit Declare arbeiten; falls nein, dann weiß ich, dass ich die DLL registrieren muss und über die COM-Schnittstelle zu gehen habe. Danach nutze ich die Fähigkeiten des Object Browser in VFP und schaue, welche Klassen samt Methoden, Eigenschaften und Ereignissen (und Interfaces) zur Verfügung stehen. Sollten die ersten Tests mittels Createobject im Command Window fehlschlagen, gint's einen kurzen Exkurs mit Suchabfrage in der Windows-Registry, um die ProgID des COM-Servers zu ermitteln. Danach lässt sich in den meisten Fällen stressfrei mit der DLL in VFP arbeiten.  
  
## Parametertypen und Strukturen
Im Umgang mit den Funktionen bzw. Methoden einer Dynamic-Link Library wird man öfters (eigentlich immer) vor das Problem gestellt, dass man bestimmte Typen für die Parameter anzugeben hat. Die üblichen Vertreter sind hierbei Handle (Integer), LptStr (String) und dann die fieseren Strukturen. In der Onlinehilfe von VFP findet man eine kleine Übersetzungstabelle für die üblichen C/C++ Datentypen auf die gewohnten VFP-Typen. Diese solltet ihr euch ausdrucken und in der Nähe des Computers zurecht legen. Bei Strukturen hilft meistens nur der Taschenrechner. Denn Strukturen werden in VFP als String mit der entsprechenden Summe der Länge der genutzten Datentypen genutzt. Alles klar... oder? In den Solution Samples gibt es dazu übrigens ein Beispiel.  
  
## Was tun bei Fehlern?
Zuerst werfe ich bei Fehlern im Zusammenhang mit DLLs je nach Typ entweder den Dependency Walker oder den VFP Object Browser an, um mich zu vergewissern, dass meine Funktionsaufrufe die richtigen Parametertypen verwenden. Danach nehme ich den [FileMon von Sysinternals](https://www.sysinternals.com/) um zu prüfen, ob eventuell Pfadangaben fehlerhaft sind oder ob benötigte Dateien nicht gefunden werden. Hierbei ist ein bisschen Detektivarbeit gefordert, aber man hat sehr hohe Trefferquoten zur Behebung der Fehlerursache. Es soll auch ab und zu hilfreich sein, mal in die Dokumentation zur DLL reinzuschauen (sofern vorhanden). Und falls die DLL von einem Drittanbieter stammt, kann man immer noch eine Mail versenden und einfach mal fragen.  
  
## Weitere Informationen und Beispiele
Zunächst sollte man in VFP die Informationen zum Declare-Befehl und den referenzierten Befehlen und Artikel durchlesen. Danach bietet sich auf alle Fälle die MSDN Bibliothek an, da in den meisten Fällen mit einer der hunderten Funktionen der Windows API gearbeitet wird. Und bei Problemfällen mal die genannten Tools probieren. Hier die Links in der Übersicht:  
  
[https://msdn.com](https://msdn.com/) bzw. [https://msdn.microsoft.com](https://msdn.microsoft.com/)  
[https://www.dependencywalker.com](https://www.dependencywalker.com/)  
[https://www.sysinternals.com](https://www.sysinternals.com/)  
  
[https://jochen.kirstaetter.name/files/joki_DynamicLinkLibraries.zip](xref:dynamic-link-libraries-in-vfp-verwenden) (Slide und Code)  
[/NET-per-COM-nutzen](xref:net-per-com-nutzen)  
[/Spass-mit-der-MessageBox](xref:spass-mit-der-messagebox)  
  
Der nächste Termin für den Stammtisch ist am 17. Mai 2006 und das Thema wird wahrscheinlich nicht AFP sein, sondern wird mittelfristig per Mail und Forum noch bekannt gegeben werden.  
  
  
Bis denne, JoKi