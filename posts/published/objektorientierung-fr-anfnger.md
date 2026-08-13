---
uid: objektorientierung-fr-anfnger
title: Objektorientierung für Anfänger...
slug: objektorientierung-fr-anfnger
date: 2006-03-20
status: published
type: post
description: Objektorientierung für Anfänger... Nach dem wir die Grundkonzepte und die wesentlichen Unterschiede sowie Vor- und potentiellen Nachteile der beiden Entwicklungssysteme .NET (C# und VB) und VFP durchgegangen sind, sehen wir uns nun einmal an, wie sich Programmierung im .NET Framework 'anfühlt'. Please fasten your seat belts, we are ready to
tags:
- Development
keywords: Development
metaTitle: Objektorientierung für Anfänger...
metaDescription: Objektorientierung für Anfänger... Nach dem wir die Grundkonzepte und die wesentlichen Unterschiede sowie Vor- und potentiellen Nachteile der beiden Entwicklungssysteme .NET (C# und VB) und VFP durchgegangen sind, sehen wir uns nun einmal an, wie sich Programmierung im .NET Framework 'anfühlt'. Please fasten your seat belts, we are ready to
image: ''
ogTitle: Objektorientierung für Anfänger...
ogDescription: Nach dem wir die Grundkonzepte und die wesentlichen Unterschiede sowie Vor- und potentiellen Nachteile der beiden Entwicklungssysteme .NET (C# und VB) und VFP durchgegangen sind, sehen wir uns nun...
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
canonicalUrl: https://jochen.kirstaetter.name/objektorientierung-fr-anfnger/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-03-20T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: Nach dem wir die Grundkonzepte und die wesentlichen Unterschiede sowie Vor- und potentiellen Nachteile der beiden Entwicklungssysteme .NET (C# und VB) und VFP durchgegangen sind, sehen wir uns nun...
twitterTitle: Objektorientierung für Anfänger...
twitterDescription: Nach dem wir die Grundkonzepte und die wesentlichen Unterschiede sowie Vor- und potentiellen Nachteile der beiden Entwicklungssysteme .NET (C# und VB) und VFP durchgegangen sind, sehen wir uns nun...
twitterImage: 
facebookTitle: Objektorientierung für Anfänger...
facebookDescription: Nach dem wir die Grundkonzepte und die wesentlichen Unterschiede sowie Vor- und potentiellen Nachteile der beiden Entwicklungssysteme .NET (C# und VB) und VFP durchgegangen sind, sehen wir uns nun...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Nach dem wir die Grundkonzepte und die wesentlichen Unterschiede sowie Vor- und potentiellen Nachteile der beiden Entwicklungssysteme .NET (C# und VB) und VFP durchgegangen sind, sehen wir uns nun einmal an, wie sich Programmierung im .NET Framework "anfühlt". Please fasten your seat belts, we are ready to take off...

Als IDE setzen wir Visual Studio 2005 ein - was auch sonst? ;-) - und erzeugen sozusagen unsere erste Solution. Als erstes Projekt schauen wir uns das wichtigste für einen VFP-Entwickler an: Den Zugriff auf die Daten.  
Da es keine direkte Datenbindung in .NET gibt, aber potentiell mit .NET 3.0 in Form von LINQ nachgereicht werden wird, erstellen wir als zuerst eine Bibliothek, die den Datenzugriff möglichst transparent gestaltet. Da wir wissen, dass es mehr als SQL Server als Datenbankserver gibt, verwenden wir auch direkt die Interfaces statt der Klassen und legen munter los. Nach einigen klärenden Fragen und Antworten haben wir schon einmal eine lauffähige Komponente. Okay, aber aktuell nutzt uns das noch nicht wirklich viel... Wir wollen auch was sehen.

Gesagt, getan. Als nächsten erstellen wir eine Webanwendung, die unsere Komponente nutzt, um die Datensätze zu holen und im Browser auszugeben. Ahhh, nett, dass Visual Studio seinen eigenen Webserver - übrigens nicht Cassini - mitbringt und damit das Ausführen und Debuggen ohne IIS ermöglicht. Wirklich nettes Feature, muss man schon sagen.

So nun erstellen wir eine Windows Forms Anwendung und nutzen, oh Wunder, dabei wieder die Datenkomponente. Nett, zusammenstecken und funktioniert. Klar, dass das bei simplen Beispielen auf eine Tabelle noch keine Kopfschmerzen bereitet. Und gleich der nächste Gimmick: ClickOnce-Deployment. Schliesslich gilt es ja nicht nur die Anwendung zu schreiben, sondern diese soll ja auch mal beim Kunden auf dem System landen und frisch ausgeführt werden. Die Einstellungsmöglichkeiten im Visual Studio zu ClickOnce sind ausreichend für das grundsätzliche Deployment. Für die durchschnittlichen VFP-Projekte ist sozusagen alles dabei. Nett, aber wer sich mit professionellen Installerprodukten beschäftigt, vermisst auf den ersten Blick doch das ein oder andere Feature. Nunja, mal irgendwann genauer mit der Materie beschäftigen und berichten.

Well, Datenzugriff, Webanwendung, Windows Anwendung... Achja, SmartClient fehlt noch. Auch hier eine simple Sache. Datenkomponente verknüpfen, den Designer anwerfen, zwei, drei Controls auf die Form werfen, bisschen Code dazwischen kleben und im Emulator laufen lassen. Wer hätte es gedacht, fertig ist die erste SmartClient-Anwendung. Tjoa, liebe Leute, dass ist der Grund wieso man Komponenten schreiben sollte...

Alright, wir haben inzwischen den Tagesabschluß erreicht und werden dem Abendessen fröhnen. Für mich war am heutigen Tag bis auf den coolen Trick mit den DataServices-Klassen in Kombination mit Stored Procedures kaum was Neues dabei. Dennoch ölt die Wiederholung die richtige Verdrahtung in den eigenen Hirnwindungen und dient gleichermaßen als Überprüfung des bereits Gelernten. Keine Überraschungen feststellbar.  
So, nun aber doch mal was futtern... Bis denne, JoKi
