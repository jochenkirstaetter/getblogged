---
uid: produktreife-nhert-sich
title: Produktreife nähert sich...
date: 2006-03-25
status: published
type: post
description: Produktreife nähert sich... Nachdem ich ja bereits über Nichts ist unmöglich... geplaudert hatte, ging es heute Morgen mit den ersten Schritten der Verfeinerung weiter. Zunächst einmal war Aufräumen angesagt. Etlichen Testcode, unterschiedliche Projekte in unterschiedlichen Solutions bereinigt und so weiter...Achja, und Vereinheitlichung auf ein .NET Framework... ;-) - Irgendwie hatte
tags:
- Development
keywords: Development
metaTitle: Produktreife nähert sich...
metaDescription: Produktreife nähert sich... Nachdem ich ja bereits über Nichts ist unmöglich... geplaudert hatte, ging es heute Morgen mit den ersten Schritten der Verfeinerung weiter. Zunächst einmal war Aufräumen angesagt. Etlichen Testcode, unterschiedliche Projekte in unterschiedlichen Solutions bereinigt und so weiter...Achja, und Vereinheitlichung auf ein .NET Framework... ;-) - Irgendwie hatte
image: ''
ogTitle: Produktreife nähert sich...
ogDescription: Nachdem ich ja bereits über Nichts ist unmöglich... geplaudert hatte, ging es heute Morgen mit den ersten Schritten der Verfeinerung weiter. Zunächst einmal war Aufräumen angesagt. Etlichen Testcode...
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
canonicalUrl: https://jochen.kirstaetter.name/produktreife-nhert-sich/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-03-25T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: Nachdem ich ja bereits über Nichts ist unmöglich... geplaudert hatte, ging es heute Morgen mit den ersten Schritten der Verfeinerung weiter. Zunächst einmal war Aufräumen angesagt. Etlichen Testcode...
twitterTitle: Produktreife nähert sich...
twitterDescription: Nachdem ich ja bereits über Nichts ist unmöglich... geplaudert hatte, ging es heute Morgen mit den ersten Schritten der Verfeinerung weiter. Zunächst einmal war Aufräumen angesagt. Etlichen Testcode...
twitterImage: 
facebookTitle: Produktreife nähert sich...
facebookDescription: Nachdem ich ja bereits über Nichts ist unmöglich... geplaudert hatte, ging es heute Morgen mit den ersten Schritten der Verfeinerung weiter. Zunächst einmal war Aufräumen angesagt. Etlichen Testcode...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Nachdem ich ja bereits über [Nichts ist unmöglich...](xref:nichts-ist-unmglich "Nichts ist unmoeglich") geplaudert hatte, ging es heute Morgen mit den ersten Schritten der Verfeinerung weiter. Zunächst einmal war Aufräumen angesagt. Etlichen Testcode, unterschiedliche Projekte in unterschiedlichen Solutions bereinigt und so weiter...  
Achja, und Vereinheitlichung auf ein .NET Framework... ;-) - Irgendwie hatte ich ein heiles Chaos in meinem Entwicklungsbaum. Naja, auch nicht weiter schlimm. Neue Verzeichnisse, neue Solution, frische Projekte und dann Pi mal Daumen die einzelnen Klassendateien reingewürfelt. Die Referenzen neu gesetzt, ein paar Errormessages aus dem Weg programmiert und tada... Ein nahezu fertiges, deploybares Produkt.

Fein, es macht Spass, wenn die normale Arbeitsweise unter Visual FoxPro ebenfalls im .NET Framework gefahren werden kann. Da ich inzwischen eine kompontenorientierte Splittung meiner Codefragmente vollzogen habe, kann ich mir auch mal Gedanken zu Strong Names (SN), dem Global Assembly Cache (GAC) und den dazugehörenden Tools machen. Hehe, das theoretische Wissen habe ich ja bereits durch einiges an Literatur, nunja, mal sehen, ob es sich auch so einfach in der Realität umsetzen lässt, wie es die Werbung verspricht.

Die Aufteilung der Klassen in Assemblies war eigentlich ziemlich easy und straight forward. Ich habe aktuell drei Projekte:

- Connection Library  
- HttpHandler  
- Windows Client

Die Connection Library repräsentiert hierbei die Grundlage für die beiden anderen Projekte wie auch für künftige Clients. Und hierfür brauche ich noch den Strong Name und die Erfahrung im Umgang mit dem GAC. Ich hatte mich mal ansatzweise vor einigen Jahren damit beschäftigt, als mein Kollege Boas Probleme bei der Auslieferung seines Crypto.NET Plugins für die Active FoxPro Pages hatte, aber erstens ist das schon einige Zeit her und zweitens könnte sich ja wieder was geändert haben. Wir werden sehen...

Naja, soweit mal der aktuelle Stand der Dinge...  
Insgesamt gibt's noch ein paar Ideen, die ich auf alle Fälle umsetzen möchte:

- Konfiguration für Connection Library  
- duale Frameworkunterstützung - also 1.1 und 2.0  
- COM Interface  
- Dokumentation  
- weitere Frontends (SmartClient, andere Sprachen und so weiter...)

Achja, die ersten praktischen Experimente mit ClickOnce-Deployment sind im Zusammenspiel mit dem Windows Forms Projekt auch gelaufen... Und ich konnte den Client erfolgreich installieren. War ganz witzig...

Mehr dazu wird's potentiell während der nächsten Wochen geben.  
Bis denne, JoKi