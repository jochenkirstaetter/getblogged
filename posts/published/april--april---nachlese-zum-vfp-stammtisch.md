---
uid: april--april---nachlese-zum-vfp-stammtisch
title: April, April - Nachlese zum VFP Stammtisch
date: 2006-04-19
status: published
type: post
description: April, April - Nachlese zum VFP Stammtisch Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab&#39;s verbockt. Laut der Website zum Stammtisch - http://speyer.dfpug.de - und meiner Erinnerungsmail sollte sich der Abend
tags:
- Community
keywords: Community
metaTitle: April, April - Nachlese zum VFP Stammtisch
metaDescription: April, April - Nachlese zum VFP Stammtisch Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab&#39;s verbockt. Laut der Website zum Stammtisch - http://speyer.dfpug.de - und meiner Erinnerungsmail sollte sich der Abend
image: ''
ogTitle: April, April - Nachlese zum VFP Stammtisch
ogDescription: Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum...
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
canonicalUrl: https://jochen.kirstaetter.name/april--april---nachlese-zum-vfp-stammtisch/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-19T10:59:51Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum...
twitterTitle: April, April - Nachlese zum VFP Stammtisch
twitterDescription: Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum...
twitterImage: 
facebookTitle: April, April - Nachlese zum VFP Stammtisch
facebookDescription: Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Ich glaube, dass sich heute (und die letzten beiden Tage) ein paar Stammtischteilnehmer vielleicht wie am 1. April vorkamen. Tut mir leid, alles meine Schuld, ich hab's verbockt. Laut der Website zum Stammtisch - [https://speyer.dfpug.de](https://speyer.dfpug.de) - und meiner Erinnerungsmail sollte sich der Abend mit dem Internet Explorer in VFP-Anwendungen beschäftigen. Nun, sollte... irgendwie habe ich es verpeilt, dass Jörg bereits im März mir zur Kenntnis gab, dass er diese Woche in Urlaub ist, und daher nicht zur Verfügung steht. Gut, alternativ hätte man dann Automation von Microsoft Winword für Druckausgaben anstreben können. Aber Moment mal, da wäre Jörg ebenfalls als Redner aktiv gewesen. Herrje, wieder nichts, okay, dann eben Plan B und das zweite Thema vom März - Dynamic-Link Libraries in VFP verwenden - nachholen.

Ihr könnt euch vielleicht vorstellen, dass wir hiermit den zweiten Satz der Thermodynamik ziemlich gut erfüllt haben. Nun, zumindest stand der Termin; wie bisher immer am 3. Mittwoch des Monats. Pünktlich um 19:30 durften wir uns im frisch renovierten (großen) Nebenraum unseres Lokals versammeln und loslegen. Zunächst wie üblich die Neuigkeiten aus der Community:

* Usergroupunterstützung durch O'Reilly und MS Press  
* Infos von CLIP und der INETA  
* Ausblick auf die Regionalleitertreffen von PASS und dFPUG

Ein paar Nachzügler trafen noch ein und dann konnten wir auch direkt mit dem Thema des heutigen Abends loslegen: Dynamic-Link Libraries (DLLs). Laut MSDN sind DLLs 'lediglich' Module mit ausgelagerten Funktionen und Daten, welche von anderen DLLs oder Anwendungen genutzt werden können. Klingt im ersten Moment sehr stark nach Prozedurenbibliotheken und APP-Projekten in Visual FoxPro, und im zweiten Augenblick hat sich auch kaum etwas geändert. Einzig der Umstand, dass DLLs in zwei verschiedenen Ausprägungen vorliegen können. Ich beleuchte Dynamic-Link Libraries hier nur im Zusammenspiel mit den Eigenheiten von VFP und nicht allgemein für andere Programmiersprachen. In VFP können DLLs über zwei unterschiedliche Wege genutzt werden:

* Declare Befehl  
* CreateObject(), NewObject() oder GetObject() Instanzierung über COM

## Declare
Über den Declare-Befehl können wir direkt auf die exportierten Funktionen einer Bibliothek zugreifen und diese in den eigenen Speicher laden. Das Ganze passiert dann In-Process und die deklarierten Funktionen stehen dem Entwickler wie normale VFP-Funktionen zur Verfügung. Man kann sich mittels des Befehls *DISPLAY DLLS* über die aktuell zur Verfügung stehenden Funktionen informieren. Hier mal ein simples Beispiel:  

```
Declare Integer Sleep In kernel32.dll ;  
Integer

Sleep(4000) && 4 Sekunden warten

Clear Dlls "Sleep"
```
  
Wir laden uns die exportierte Funktion Sleep aus der kernel32.dll in unsere Anwendung, führen sie dann mit einem Parameter (gemäß Deklaration) aus, und entfernen sie abschließend wieder. Das gleiche Verhalten wie beim Aufruf einer Funktion in einer VFP-Prozedurendatei, welche mittels Set Procedure To referenziert wurde. Der Verweis auf die DLL erfolgt normalerweise ohne Pfadangaben, kann aber auch Pfadinformationen nutzen. Ohne Pfad sucht VFP die DLL an den üblichen Stellen im Betriebssystem und verweigert erst die Ausführung, falls wirklich nichts zu finden ist. Das kann potentiell zu Problemen führen, falls unterschiedliche Versionen der gleichen DLL vorliegen. Hier gilt es dann mittels DISPLAY DLLS zu prüfen, welche physikalische Datei herangezogen wurde.

## COM-Schnittstelle
Die zweite Art der Nutzung von Dynamic-Link Libraries in VFP kann über die COM-Schnittstelle erfolgen. Hier gelten dann de facto die gleichen Regeln wie der OLE Automation. Objektreferenz auf die Klassendefinition erzeugen, Methoden mit passenden Parameter ausführen und die Rückgabewerte interpretieren. Im letzten Beitrag [.NET per COM nutzen](xref:net-per-com-nutzen) habe ich genau diesen Fall bereits ausführlicher beschrieben.

## Hilfsmittel erleichtern die Arbeit
Oftmals steht man am Anfang vor dem Problem überhaupt Informationen zur vorliegenden DLL zu erhalten. Denn entweder kennt man die Funktionen einer Bibliothek überhaupt nicht, oder es liegen zu wenige Informationen oder Dokumentation vor. Meine gegenwärtige Vorgehensweise ist die, dass ich zuerst die DLL im [Dependency Walker](https://www.dependencywalker.com) öffne und nachschaue, ob exportierte Funktionen vorliegen. Falls ja, okay, dann kann ich mit Declare arbeiten; falls nein, dann weiß ich, dass ich die DLL registrieren muss und über die COM-Schnittstelle zu gehen habe. Danach nutze ich die Fähigkeiten des Object Browser in VFP und schaue, welche Klassen samt Methoden, Eigenschaften und Ereignissen (und Interfaces) zur Verfügung stehen. Sollten die ersten Tests mittels Createobject im Command Window fehlschlagen, gint's einen kurzen Exkurs mit Suchabfrage in der Windows-Registry, um die ProgID des COM-Servers zu ermitteln. Danach lässt sich in den meisten Fällen stressfrei mit der DLL in VFP arbeiten.

## Parametertypen und Strukturen
Im Umgang mit den Funktionen bzw. Methoden einer Dynamic-Link Library wird man öfters (eigentlich immer) vor das Problem gestellt, dass man bestimmte Typen für die Parameter anzugeben hat. Die üblichen Vertreter sind hierbei *Handle* (Integer), *LptStr* (String) und dann die fieseren Strukturen. In der Onlinehilfe von VFP findet man eine kleine Übersetzungstabelle für die üblichen C/C++ Datentypen auf die gewohnten VFP-Typen. Diese solltet ihr euch ausdrucken und in der Nähe des Computers zurecht legen. Bei Strukturen hilft meistens nur der Taschenrechner. Denn Strukturen werden in VFP als String mit der entsprechenden Summe der Länge der genutzten Datentypen genutzt. Alles klar... oder? In den Solution Samples gibt es dazu übrigens ein Beispiel, ich möchte hier auch kurz eins zeigen:  

```foxpro
#DEFINE TIME_ZONE_SIZE 172
#DEFINE TIME_ZONE_ID_UNKNOWN 0
#DEFINE TIME_ZONE_ID_STANDARD 1
#DEFINE TIME_ZONE_ID_DAYLIGHT 2

*#beautify keyword_nochange
* see [https://support.microsoft.com/kb/894818/](https://support.microsoft.com/kb/894818/)
DECLARE INTEGER GetTimeZoneInformation IN kernel32.dll;
  STRING @ lpTimeZoneInformation
*#beautify

*| typedef struct _TIME_ZONE_INFORMATION {
*| LONG Bias; 0 4
*| WCHAR StandardName[ 32 ]; 4 64
*| SYSTEMTIME StandardDate; 68 16
*| LONG StandardBias; 84 4
*| WCHAR DaylightName[ 32 ]; 88 64
*| SYSTEMTIME DaylightDate; 152 16
*| LONG DaylightBias; 168 4
*| } TIME_ZONE_INFORMATION, *PTIME_ZONE_INFORMATION; total 172 bytes

LOCAL cBuffer, nResult
cBuffer = Repli(Chr(0), TIME_ZONE_SIZE)
nResult = GetTimeZoneInformation(@cBuffer)

DO CASE
  CASE nResult = TIME_ZONE_ID_STANDARD
    ? "StandardDate member"
  CASE nResult = TIME_ZONE_ID_DAYLIGHT
    ? "DaylightDate member"
  CASE nResult = TIME_ZONE_ID_UNKNOWN
    ? "The system cannot determine the current time zone"
    OTHER
    ? "The Time Zone ID is invalid"
ENDCASE
?
? "Bias (minutes between UTC and local):", buf2dword(SUBSTR(cBuffer, 1,4))
? "Standard Bias:", buf2dword(SUBSTR(cBuffer, 85,4))
? "Daylight Bias:", buf2dword(SUBSTR(cBuffer, 169,4))
?
? "Standard name:", STRTRAN(SUBSTR(cBuffer, 5,64), Chr(0),"")
? "Daylight name:", STRTRAN(SUBSTR(cBuffer, 89,64), Chr(0),"")
?
? "Standard Date:",;
  buf2word(SUBSTR(cBuffer,69,2)),;
  buf2word(SUBSTR(cBuffer,71,2)),;
  buf2word(SUBSTR(cBuffer,73,2)),;
  buf2word(SUBSTR(cBuffer,75,2)),;
  buf2word(SUBSTR(cBuffer,77,2)),;
  buf2word(SUBSTR(cBuffer,79,2))

? "Daylight Date:",;
  buf2word(SUBSTR(cBuffer,153,2)),;
  buf2word(SUBSTR(cBuffer,155,2)),;
  buf2word(SUBSTR(cBuffer,157,2)),;
  buf2word(SUBSTR(cBuffer,159,2)),;
  buf2word(SUBSTR(cBuffer,161,2)),;
  buf2word(SUBSTR(cBuffer,163,2))

FUNCTION buf2dword(lcBuffer)
  RETURN Asc(SUBSTR(lcBuffer, 1,1)) + ;
    BitLShift(Asc(SUBSTR(lcBuffer, 2,1)), 8) +;
    BitLShift(Asc(SUBSTR(lcBuffer, 3,1)), 16) +;
    BitLShift(Asc(SUBSTR(lcBuffer, 4,1)), 24)

  FUNCTION buf2word(lcBuffer)
    RETURN Asc(SUBSTR(lcBuffer, 1,1)) + ;
      Asc(SUBSTR(lcBuffer, 2,1)) * 256
```
  
Die Funktion GetTimeZoneInformation setzt sich aus unterschiedlichen Datentypen zu einer Gesamtgröße von 172 Bytes zusammen. In VFP erstellen wir daher eine Zeichenkette aus Chr(0) dieser Länge und übergeben den Wert per Referenz (@-Parameter), um als Rückgabewert die gewünschten Informationen zu erhalten. Wir müssen daher beim Zerlegen des Strings berücksichtigen, dass die Bytes entsprechend zu überführen sind.

## Was tun bei Fehlern?
Zuerst werfe ich bei Fehlern im Zusammenhang mit DLLs je nach Typ entweder den Dependency Walker oder den VFP Object Browser an, um mich zu vergewissern, dass meine Funktionsaufrufe die richtigen Parametertypen verwenden. Danach nehme ich den [FileMon von Sysinternals](https://www.sysinternals.com) um zu prüfen, ob eventuell Pfadangaben fehlerhaft sind oder ob benötigte Dateien nicht gefunden werden. Hierbei ist ein bisschen Detektivarbeit gefordert, aber man hat sehr hohe Trefferquoten zur Behebung der Fehlerursache. Es soll auch ab und zu hilfreich sein, mal in die Dokumentation zur DLL reinzuschauen (sofern vorhanden). Und falls die DLL von einem Drittanbieter stammt, kann man immer noch eine Mail versenden und einfach mal fragen.

## Weitere Informationen und Beispiele
Zunächst sollte man in VFP die Informationen zum Declare-Befehl und den referenzierten Befehlen und Artikel durchlesen. Danach bietet sich auf alle Fälle die MSDN Bibliothek an, da in den meisten Fällen mit einer der hunderten Funktionen der Windows API gearbeitet wird. Und bei Problemfällen mal die genannten Tools probieren. Hier die Links in der Übersicht:

[https://msdn.com](https://msdn.com) bzw. [https://msdn.microsoft.com](https://msdn.microsoft.com)  
[https://www.dependencywalker.com](https://www.dependencywalker.com)  
[https://www.sysinternals.com](https://www.sysinternals.com)

[https://jochen.kirstaetter.name/files/joki_ApiSamples.zip](https://jochen.kirstaetter.name/files/joki_ApiSamples.zip) (Slide und Code)  
[/NET-per-COM-nutzen](xref:net-per-com-nutzen)  
[/Spass-mit-der-MessageBox](xref:spass-mit-der-messagebox)

Der nächste Termin für den Stammtisch ist am 17. Mai 2006 und das Thema wird wahrscheinlich nicht AFP sein, sondern wird mittelfristig per Mail und Forum noch bekannt gegeben werden.  
Bis denne, JoKi