---
uid: devcon-prag-2006---day-2
title: Devcon Prag 2006 - Day 2
slug: devcon-prag-2006---day-2
date: 2006-09-12
status: published
type: post
description: Devcon Prag 2006 - Day 2 **Windows Component Services**Alle Jahre wieder vergibt Microsoft neue Namen f&#252;r vorhandene Technologien. Okay, es ist weitaus mehr als nur eine schlichte Namens&#228;nderung. Schliesslich wird damit auch angezeigt, dass Neuerungen realisiert wurden.SetComplete() beendet die Transaktion und entsorgt das COM+ Objekt im Speicher.F&#252;r Windows Component Services
tags:
- Community
keywords: Community
metaTitle: Devcon Prag 2006 - Day 2
metaDescription: Devcon Prag 2006 - Day 2 **Windows Component Services**Alle Jahre wieder vergibt Microsoft neue Namen f&#252;r vorhandene Technologien. Okay, es ist weitaus mehr als nur eine schlichte Namens&#228;nderung. Schliesslich wird damit auch angezeigt, dass Neuerungen realisiert wurden.SetComplete() beendet die Transaktion und entsorgt das COM+ Objekt im Speicher.F&#252;r Windows Component Services
image: content/images/2006/09/photo-1514994173729-9cd2e1750e35.webp
ogTitle: Devcon Prag 2006 - Day 2
ogDescription: '**Windows Component Services**Alle Jahre wieder vergibt Microsoft neue Namen für vorhandene Technologien. Okay, es ist weitaus mehr als nur eine schlichte Namensänderung. Schliesslich wird damit auch...'
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
canonicalUrl: https://jochen.kirstaetter.name/devcon-prag-2006---day-2/
imageUrl: content/images/2006/09/photo-1514994173729-9cd2e1750e35.webp
twitterImageUrl: https://images.unsplash.com/photo-1514994173729-9cd2e1750e35?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=56107f1f2476a77d6cd1e6a8d5a3672b
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2006/09/photo-1514994173729-9cd2e1750e35.webp
featured: false
publishedAt: 2006-09-12T11:27:19Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: '**Windows Component Services**Alle Jahre wieder vergibt Microsoft neue Namen für vorhandene Technologien. Okay, es ist weitaus mehr als nur eine schlichte Namensänderung. Schliesslich wird damit auch...'
twitterTitle: Devcon Prag 2006 - Day 2
twitterDescription: '**Windows Component Services**Alle Jahre wieder vergibt Microsoft neue Namen für vorhandene Technologien. Okay, es ist weitaus mehr als nur eine schlichte Namensänderung. Schliesslich wird damit auch...'
twitterImage: 
facebookTitle: Devcon Prag 2006 - Day 2
facebookDescription: '**Windows Component Services**Alle Jahre wieder vergibt Microsoft neue Namen für vorhandene Technologien. Okay, es ist weitaus mehr als nur eine schlichte Namensänderung. Schliesslich wird damit auch...'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
## Windows Component Services
Alle Jahre wieder vergibt Microsoft neue Namen für vorhandene Technologien. Okay, es ist weitaus mehr als nur eine schlichte Namensänderung. Schliesslich wird damit auch angezeigt, dass Neuerungen realisiert wurden.  
SetComplete() beendet die Transaktion und entsorgt das COM+ Objekt im Speicher.  
Für Windows Component Services gibt es zwei Ebenen der Sicherheit - deklarativ und programmatisch. Die deklarative Sicherheit wird im MMC-SnapIn realisiert und verwendet die vorhandenen Sicherheitsmöglichkeiten von Windows. Beim Erstellen von Rollen für eine Komponente empfiehlt es sich, dass man eine Benutzergruppe statt einzelner Benutzer hinzufügt. Auf diese Weise kann man sehr einfach den Zugriff von außen auf die Komponente konfigurieren. Sinnvollerweise gehen diese Einstellungen bis auf Methodenebene. Somit kann man bspw. allen Gruppen die Initialisierung gestatten, aber einzelnen Gruppen den Zugriff auf bestimmte Methoden verweigern. Zum Abfangen des COM-Fehlers, etwa bei "Zugriff verweigert", kapselt man den Aufruf in einen Try..EndTry-Block und kann stressfrei die lokale Anwendung laufen lassen.

## LINQ
Nach der anstrengenden Runde zu Distributed Applications mit COM+ und den diversen VFP Projekten samt Komponentenprogrammierung, COM+ Softwareaddons des Betriebssystems und so weiter, kommt eine kleine Entspannungsrunde mit Zukunftsaussichten von Microsoft ganz recht. Der Begriff Language INtegrated Query (LINQ) macht ja bereits seit einiger Zeit verstärkt Werbung für das kommenden .NET Framework 3.0, und die gezeigten Beispiele und Einsatzmöglichkeiten von Alan lassen auch auf coole Möglichkeiten spekulieren. Aber ganz ehrlich gibt's hier zwei Wehrmutstropfen: Es ist einiges an VFP-Knowledge in LINQ eingeflossen und die bisherigen Beispiele zeigten immer nur Abfragen (oder hat jemand schon ein Update oder Delete-Statement bzw. Aufruf einer Stored Procedure in LINQ gesehen?). Okay, es ist noch im Alpha-Status und warten wir mal ab, was noch kommen wird... dennoch ein durchwachsener Eindruck.

## XFRX - [https://www.eqeus.com/](https://www.eqeus.com/)
Als German distributor für XFRX schaue ich mir selbstverständlich die Session von Martin Haluza auf Englisch. Zum einen möchte ich mir die Neuerungen der Version 12.0 ansehen und zum anderen direkten Kontakt mit ihm pflegen, und ein wenig Smalltalk halten. Neben der Tatsache, dass ProLib Tools XFRX vertreibt und supportet, habe ich die deutsche Übersetzung der UI durchgeführt und schreibe ein wenig an einem Plugin für die Active FoxPro Pages. Was mich immer wieder fasziniert, ist die Möglichkeit, dass man in XFRX einen Report mitsamt der Daten als Datei im XFF-Format speichern und später stressfrei wiederverwenden und in die angebotenen Dokumentformate exportieren kann. In der Version 12.0 wurde verstärkt der Preview verbessert. So sind bspw. mehrere Seiten nebeneinander anzeigbar und Reports können kaskadiert werden, etwa zur Darstellung von 1:n-Relationen. Auch Hyperlinks in HTML und PDF sind direkt nutzbar.

[b]Cool Uses for ReportListeners**  
Hallo erstmal. Ich weiß ja nicht, ob sie es wussten...  
... aber Visual FoxPro 9.0 hat eine komplett überarbeitete ReportEngine. Und was man damit anstellen kann, ist schlichtweg oberhammermäßig cool. Der komplette Report mutiert de facto zu einem 'Container-Control' mit dem man beliebige Ergänzungen und VFP-Code nutzen kann. Neben den vielen Exportoptionen bietet die Klasse ReportListener nahezu unbeschränkte Möglichkeiten für die Verarbeitung von VFP-Reports - The sky is the limit! Ich warte schon extremst gespannt auf die Sessionunterlagen von Doug Henning, um intensiver mit den Beispielen zu arbeiten. Achja, auf der Website [VFP Report Listener Headquarters](https://www.reportlistener.com/) gibt's übrigens frei verfügbar nützliche Klassen für die Druckaufbereitung. Schaut euch auf alle Fälle mal die NavPane-Klasse an. Ziemlich cool und total easy in der Implementierung...

## Q&A und Fazit zur Konferenz
Jede Konferenz nimmt leider ihr Ende und ich sehe der ganzen Sache mit einem weinenden und lachenden Auge hinterher: 2006 in Prag geht zu Ende, aber 2007 wird wieder stattfinden. Und ich werde wieder da sein. Es ist wirklich schade, dass man oftmals nur im Rahmen einer Konferenz zum Treffpunkt mit VFP-Entwicklern aus anderen Nationen nutzen kann. Nun, schauen wir mal... Es hat mir persönlich auf alle Fälle wieder sehr viel Freude und Spass gebracht. Die nächsten Termine sind schon in der Planung bzw. Sichtweite:

dFPUG VFP Entwicklerkonferenz 2006 in Frankfurt  
AtoutFox 2006 in Paris \*(noch offen)\*  
Devcon Moskau 2007 \*(noch offen)\* - hier hoffe ich auf den [FoxClub.ru](https://www.foxclub.ru)

Bis dahin wird sicherlich noch sehr viel in der Fuchsszene passieren.  
Euer Harry Hirsch aka JoKi... ;-)