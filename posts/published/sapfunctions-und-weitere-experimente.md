---
uid: sapfunctions-und-weitere-experimente
title: SAP.Functions und weitere Experimente
slug: sapfunctions-und-weitere-experimente
date: 2006-08-24
status: published
type: post
description: In unserem laufenden Projekt steht in den nächsten Tagen die Erstellung einer Kommunikationsschnittstelle zu SAP R/3 an. Glücklicherweise kann ich hierzu auf ein paar frühe Umsetzungen von unserem Kunden zurückgreifen.
tags:
- Development
keywords: Development
metaTitle: SAP.Functions und weitere Experimente
metaDescription: In unserem laufenden Projekt steht in den nächsten Tagen die Erstellung einer Kommunikationsschnittstelle zu SAP R/3 an. Glücklicherweise kann ich hierzu auf ein paar frühe Umsetzungen von unserem Kunden zurückgreifen.
image: ''
ogTitle: SAP.Functions und weitere Experimente
ogDescription: Von SAP hat sicherlich schon jede/r Aktive in der Softwarebranche gehört oder gelesen. In unserem laufenden Projekt steht in den nächsten Tagen die Erstellung einer Kommunikationsschnittstelle zu SAP...
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
canonicalUrl: https://jochen.kirstaetter.name/sapfunctions-und-weitere-experimente/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-08-24T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: Von SAP hat sicherlich schon jede/r Aktive in der Softwarebranche gehört oder gelesen. In unserem laufenden Projekt steht in den nächsten Tagen die Erstellung einer Kommunikationsschnittstelle zu SAP...
twitterTitle: SAP.Functions und weitere Experimente
twitterDescription: Von SAP hat sicherlich schon jede/r Aktive in der Softwarebranche gehört oder gelesen. In unserem laufenden Projekt steht in den nächsten Tagen die Erstellung einer Kommunikationsschnittstelle zu SAP...
twitterImage: 
facebookTitle: SAP.Functions und weitere Experimente
facebookDescription: Von SAP hat sicherlich schon jede/r Aktive in der Softwarebranche gehört oder gelesen. In unserem laufenden Projekt steht in den nächsten Tagen die Erstellung einer Kommunikationsschnittstelle zu SAP...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
## Szenario mit SAP R/3

Von SAP hat sicherlich schon jede/r Aktive in der Softwarebranche gehört oder gelesen. In unserem laufenden Projekt steht in den nächsten Tagen die Erstellung einer Kommunikationsschnittstelle zu SAP R/3 an. Glücklicherweise kann ich hierzu auf ein paar frühe Umsetzungen von unserem Kunden zurückgreifen; spart ein wenig Zeit bei der Einarbeitung in die eigentliche Materie. Hintergrund für diese Anforderung ist u.a. das Buchen von Dokumenten in SAP aus unserer VFP-Projektentwicklung.

Ausgestattet mit dem vorhandenen, funktionierenden Code aus der Altanwendung, einigen Ideen und zwei, drei Büchern sehe ich dieser Aufgabe gegenwärtig sehr versonnen ins Auge. Meine ersten Experimente in Bezug auf Automation des SAP-Clients sehen schon ziemlich versprechend aus. Zumal ich auch durch eine vorangehende Recherche im Internet etliche Beispiele in ASP, VBScript und JavaScript finden konnte, welche meinen Lösungsansatz festigen.

## COM-Server von SAP

SAP GUI bietet als Client zu SAP R/3 nicht nur ein visuelles Frontend an. Ebenso stehen für den geneigten Fuchsbändiger einige COM Type Libraries zur Verfügung, welche problemlos in VFP instanziiert und genutzt werden können. Diese Nutzung ist vergleichbar mit der OLE-Automation von Word oder Outlook. Man benötigt lediglich die richtige Literatur und IntelliSense. Als Ausgangspunkt dient uns die Objektreferenz auf SAP.Functions. Mit dieser Instanz können wir die Verbindung zum SAP Backend aufbauen und die gewünschten Funktionen samt Eingabe- und Rückgabeparameter ausführen und auswerten.

`Define Class CSapGui As Label`  
`  oSap = .Null.`  
`  oResult = .Null.`

`  Function Logon()`  
`    Local loConn, loException, luReturn`  
`    m.loConn = .Null.`  
`    m.loException = .Null.`  
`    m.luReturn = .Null.`

`    Try`  
`      This.oSap = CreateObject("SAP.Functions")`  
`      m.loConn = This.oSap.Connection`

`      m.loConn.System = "DEV"`  
`       m.loConn.ApplicationServer = "SAPSERVER"`  
`       m.loConn.Client = "100"`  
`       m.loConn.User = "IOS"`  
`       m.loConn.Password = "FoxPro"`  
`        m.loConn.Language = "DE" `  
`       m.loConn.TraceLevel = 6`  
`       *--- Klasseneigenschaften verwenden... ;-)`

`      m.luReturn = m.loConn.Logon(0, .T.)`  
`    Catch To m.loException`  
`       Assert .F. Message "SAP-Schnittstelle nicht bereit"`  
`    EndTry`

`    Return m.luReturn`  
`  EndFunc`  
  
Sofern wir nicht aus dem Try-Catch-Block rausfliegen und der Rückgabewert des Logon positiv ausfällt, sind wir am SAP-Backend authentifiziert und können weitere Aktionen laufen lassen.



## Calls in SAP auslösen

Uns steht eine Liste der zu nutzenden Calls im SAP-Backend zur Verfügung. Interessanterweise verfügen diese über unterschiedliche Anzahl an Parametern. In Kombination mit einer Meta-Tabelle, die uns die notwendigen Daten zur einzelnen Funktion liefert, können wir mit der vorhandenen Objektreferenz direkt weiter arbeiten.

`Function Call(tcFunction As String)`  
`  Local lcFunction, loFunction, luReturn`  
`  m.lcFunction = Transform(Evl(m.tcFunction, "IosTest"))`  
`  m.loFunction = .Null.`  
`  m.luReturn = .Null.`  
`  This.oResult = .Null.`

`  m.loFunction = m.loSap.Add(m.lcFunction)`  
`  If Vartype(m.loFunction) == T_OBJECT`  
`    Select("MetaSAP")`  
`    Set Order To Sortierung Ascending`  
`    Scan For cFunction = m.lcFunction`  
`      m.loFunction.Exports(cParaName) = cParaValue`  
`    EndScan`

`    m.luReturn = m.loFunction.Call()`  
`    This.oResult = m.loFunction.Tables`

`    *--- weitere Verarbeitung des Ergebnis (Collection)`  
`    This.CallCompleted(m.lcFunction)`  
`    *--- oder: RaiseEvent(This, "CallCompleted", m.lcFunction)`  
`  EndIf`  
`EndFunc`

`Function Logoff()`  
`  This.oSap.Connection.Logoff()`  
`EndFunc`

`Function CallCompleted(tcFunction As String)`  
`  *--- virtual: Konkretisierung in Ableitung implementieren`  
`EndFunc`

Durch die Kapselung der grundsätzlichen Funktionalität in eine eigene Klasse erhalten wir sehr viel Freiheit in weiteren Nutzung. In Ableitungen können Spezialisierungen bzw. sogenannte High-Level-Methoden erstellt werden, die für den jeweiligen Anwendungsfall einfachere Möglichkeiten bieten. Beispiele hierfür wären etwa 'SapGuiKunde.Anlegen()' oder 'SapGuiRechnung.Buchen()' welche den eigentlichen Kommunikationsanteil mit dem SAP-Backend vor dem Zugriff des Entwicklers kapseln und auf diese Weise die Verwendung erheblich vereinfachen.

## Eine Frage des Betrachtungswinkels

Beim Erstellen einer generischen, wiederverwendbaren Klasse gilt es unter anderem darauf zu achten, dass die sogenannten Kernfunktionen implementiert werden. Jedoch nicht mehr. Das obige Beispiel dürfte sich gut dafür eignen. Zur weiteren Vereinfachung könnte man sogar noch eine Prozessmethode erstellen, welche den Gesamtablauf vereinfacht:

`Function Process(tcFunction As String)`  
`  With This`  
`    If .Logon()`  
`      .Call(m.tcFunction)`  
`      .Logoff()`  
`    EndIf`  
`  EndWith`  
EndFunc  
  
In den Ableitungen dieser Klasse konzentriert man sich primär auf die Verarbeitung der Rückgabewerte aus dem SAP-Backend - eventuell mit Fallunterscheidung nach Funktion - und erstellt bei Bedarf weitere Methoden für Spezialisierungen.

## Weitere Nutzung der Klasse

Durch den Verzicht auf konkrete Anforderungen innerhalb der Anwendung und der Umsetzung als neutrale Komponente sind wir spielend in der Lage die Klasse in den unterschiedlichsten Anwendungsfällen als Grundlage zu verwenden. Der aktuelle Entwurf sieht vor, dass jeweils in der Ableitung bzw. Instanz der Klasse die benötigte Lösung implementiert wird.

Ich möchte übrigens erwähnen, dass der beschriebene Quellcode übrigens die dritte Revision der Klasse ist, da ich mit steigendem Wissen über die SAP.Functions direkt den bereits geschriebenen Code dem Refactoring - also 'Wegwerfen und neu schreiben' 😎 - unterworfen habe. Ich möchte euch dazu ermahnen, dass noch kein Meister vom Himmel gefallen ist und ebenso ermuntern neue Ideen nicht sausen zu lassen, nur weil euer Code bereits im Einsatz ist.  
Bis denne, JoKi