---
uid: net-per-com-nutzen
title: .NET per COM nutzen
slug: net-per-com-nutzen
date: 2006-04-19
status: published
type: post
description: .NET per COM nutzen Heute war wieder einmal so ein Fall der Fälle bei denen ich es geniesse, dass ich inzwischen mit mehr Programmiersprachen als mit Visual FoxPro zu tun habe.
tags:
- Development
keywords: Development
metaTitle: .NET per COM nutzen
metaDescription: .NET per COM nutzen Heute war wieder einmal so ein Fall der Fälle bei denen ich es geniesse, dass ich inzwischen mit mehr Programmiersprachen als mit Visual FoxPro zu tun habe.
image: ''
ogTitle: .NET per COM nutzen
ogDescription: Heute war wieder einmal so ein Fall der Fälle bei denen ich es geniesse, dass ich inzwischen mit mehr Programmiersprachen als mit Visual FoxPro zu tun habe. Bedingt durch ein Kundenprojekt meines...
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
canonicalUrl: https://jochen.kirstaetter.name/net-per-com-nutzen/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-19T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: Heute war wieder einmal so ein Fall der Fälle bei denen ich es geniesse, dass ich inzwischen mit mehr Programmiersprachen als mit Visual FoxPro zu tun habe. Bedingt durch ein Kundenprojekt meines...
twitterTitle: .NET per COM nutzen
twitterDescription: Heute war wieder einmal so ein Fall der Fälle bei denen ich es geniesse, dass ich inzwischen mit mehr Programmiersprachen als mit Visual FoxPro zu tun habe. Bedingt durch ein Kundenprojekt meines...
twitterImage: 
facebookTitle: .NET per COM nutzen
facebookDescription: Heute war wieder einmal so ein Fall der Fälle bei denen ich es geniesse, dass ich inzwischen mit mehr Programmiersprachen als mit Visual FoxPro zu tun habe. Bedingt durch ein Kundenprojekt meines...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Heute war wieder einmal so ein Fall der Fälle bei denen ich es geniesse, dass ich inzwischen mit mehr Programmiersprachen als mit Visual FoxPro zu tun habe. Bedingt durch ein Kundenprojekt meines Kollegen ergab sich die Aufgabenstellung, dass Funktionalitäten in einer DLL - vermutlich eine .NET Library - in die bestehende VFP-Anwendung zu integrieren sind. Nun, prinzipiell ist das eine einfache Sache. COM-Interface instanziieren und wohlfühlen.  
  
**Beispielcode vorhanden...**  
Leider stand meinem Kollegen nur Beispielcode in Visual Basic (.NET) zur Verfügung. Okay, also, dann schauen wir uns mal die DLL an. Zusätzlich zur reinen Dynamic-Link Library liegt im Verzeichnis ebenfalls eine .TLB (Type Library) Datei vor. Sehr gut, diese können wir problemlos im Object Browser von VFP einlesen und haben damit Informationen zu den Innereien der DLL an der Hand. Gut, zwei Klassen, einige Methoden und 4 Interfaces. Sieht doch schon mal gut aus. Nur... wie erhalten wir eine Objektreferenz auf diese Klassen? Probieren wir es zuerst mal mit dem Offensichtlichen:  
  
` oTest = CreateObject("DllName.KlassenName")  
`  
  
Leider Fehlschlag, der Moniker steht nicht zur Verfügung.  
  
**Windows Registry to the rescue!**  
Bewaffnet mit dem Klassennamen öffnen wir den Registrierungseditor und suchen ausgehend von der Wurzel nach der Klasse. Und der erste Treffer liefert uns auch dankenswerterweise die benötigte ProgID des COM-Servers. Wir sehen sofort, dass die Komponente leider eine eher unübliche ProgID besitzt, diese sieht nämlich sehr verdächtig nach .NET Namespacekonvention mit Firma.Produkt.Klasse aus. Okay, lassen wir uns nicht weiter dadurch von der Arbeit abhalten. Der Aufruf im Command Window von  
  
` oTest = CreateObject("Firma.Produkt.KlassenName")  
`  
  
führt direkt zum Erfolg - Auch wenn wir eine merkliche Verzögerung bzw. Zwangspause zum Laden des .NET Frameworks hinter den Kulissen feststellen können. Egal, Hauptsache wir haben eine gültige Referenz auf das Objekt und können weiterarbeiten. Leider greift das gewohnte Intellisense noch nicht, aber dafür werden potentiell auch noch eine Lösung finden.  
  
**Windows Form in VFP anzeigen**  
Die erste Überraschung folgt auch so gleich bei der weiteren Verwendung der Objektreferenz. Laut Object Model und Aufgabenstellung müssen wir eine Suchabfrage absetzen und dann auf ein entsprechendes Event reagieren. Gut, wir schauen uns die zu spezifizierenden Datentypen der Methode an und lösen die Funktion aus. Nach kurzer Pause taucht eine Windows Form mit den Trefferdatensätzen in einem DataGrid auf - coole Sache. Und da erzählt uns Ken Levy, dass das nicht möglich sei... ;-) - Gut, ich hab' dazu ebenfalls schon einen generischen COM-Server für unsere Testzwecke geschrieben. Weiter im Kontext, also einen Treffer selektieren und dann?  
Ja, dann kommt das Event ins Spiel.  
  
**Auf .NET / COM Events in VFP reagieren**  
Um auf Ereignisse von COM-Servern im Allgemeinen in Visual FoxPro reagieren zu können, ist die Funktion BindEvent() leider nicht brauchbar. Diese kann lediglich eine Bindung auf foxproeigene Objekte und auf Windows Messages erstellen. In Zusammenarbeit mit COM-Servern müssen wir eine Eventklasse des Interface des Servers erstellen - dort können wir unseren Code eintragen -, und dann verheiraten wir die beiden Objektreferenzen per EventHandler() Funktion miteinander. Das hört sich im ersten Moment wesentlich schlimmer an, als es dann tatsächlich ist. Alles eine Frage der Übung.  
Die Eventklasse des Interface erstellen wir uns per Drag&Drop über den Object Browser. Dazu öffnen wir eine leere PRG Datei und droppen dann einfach vom Object Browser das benötigte Interface unseres COM-Servers hinein. *Flupp* erscheint der komplette Code, den wir brauchen. Zusätzlich passen wir nun noch den Klassennamen und den Verweis der Implements-Anweisung auf die ProgID an und können dann in den einzelnen 'Event-Methoden' unseren Code eintragen. Wichtig, niemals die Signatur der Klasse ändern, sonst klappt die Kopplung mit dem COM-Server nicht mehr. Hier mal exemplarisch wie das aussehen könnte:  
  
` oCom = CreateObject("Firma.Produkt.KlassenName")  
oEvents = CreateObject("KlassenNameEvents")  
  
EventHandler(oCom, oEvents)  
  
Define Class KlassenNameEvents As Session OlePublic  
Implements IKlassenEvents In "Firma.Produkt.KlassenName"  
  
  
; Procedure IKlassenEvents_OnSelection&  
#40;Primary As Integer)  
* add your code here  
EndDefine  
  
`  
So in etwa dürfte das auch bei euch aussehen. Es besteht übrigens kein Unterschied, ob es sich um einen 'klassischen' COM-Server oder einen .NET-basierten handelt. COM ist COM und funktioniert gleichermaßen.  
  
**Problem erkannt, Problem gelöst**  
Nach diesem kleinen Exkurs in die Welt der COM-Server und des .NET-Frameworks fühlt sich mein Kollege wieder in der VFP-Programmierung heimisch und die Integration ist bereits im Teststadium, da alles wie gewünscht gelaufen ist.  
  
  
Bis denne, JoKi  
  
PS: Die ProgID eines COM-Servers hat übrigens erstmal nichts mit dem .NET Namespace zu tun und sollte auch einer anderen Konvention (Library.Klasse) folgen.
