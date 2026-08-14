---
uid: bauen-wir-uns-einen-webserver
title: Bauen wir uns einen Webserver
slug: bauen-wir-uns-einen-webserver
date: 2006-03-26
status: published
type: post
description: Bauen wir uns einen Webserver Ausgehend von zwei konkreten Vorlagen (Buch mit Codesnipplet und Eeva) ergab sich direkt die M&#246;glichkeit zur Erstellung eines lokalen Webservers. Dieser wird sozusagen 'afp-enabled' gebaut. Dies erm&#246;glicht es uns, dass wir autark ohne externen Webserver arbeiten k&#246;nnen. M&#246;gliche Anwendungsszenarien sind hierbei die Auslieferung auf CD
tags:
- Development
keywords: Development
metaTitle: Bauen wir uns einen Webserver
metaDescription: Bauen wir uns einen Webserver Ausgehend von zwei konkreten Vorlagen (Buch mit Codesnipplet und Eeva) ergab sich direkt die M&#246;glichkeit zur Erstellung eines lokalen Webservers. Dieser wird sozusagen 'afp-enabled' gebaut. Dies erm&#246;glicht es uns, dass wir autark ohne externen Webserver arbeiten k&#246;nnen. M&#246;gliche Anwendungsszenarien sind hierbei die Auslieferung auf CD
image: ''
ogTitle: Bauen wir uns einen Webserver
ogDescription: Ausgehend von zwei konkreten Vorlagen (Buch mit Codesnipplet und Eeva) ergab sich direkt die Möglichkeit zur Erstellung eines lokalen Webservers. Dieser wird sozusagen "afp-enabled" gebaut. Dies...
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
canonicalUrl: https://jochen.kirstaetter.name/bauen-wir-uns-einen-webserver/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-03-26T10:48:33Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Ausgehend von zwei konkreten Vorlagen (Buch mit Codesnipplet und Eeva) ergab sich direkt die Möglichkeit zur Erstellung eines lokalen Webservers. Dieser wird sozusagen "afp-enabled" gebaut. Dies...
twitterTitle: Bauen wir uns einen Webserver
twitterDescription: Ausgehend von zwei konkreten Vorlagen (Buch mit Codesnipplet und Eeva) ergab sich direkt die Möglichkeit zur Erstellung eines lokalen Webservers. Dieser wird sozusagen "afp-enabled" gebaut. Dies...
twitterImage: 
facebookTitle: Bauen wir uns einen Webserver
facebookDescription: Ausgehend von zwei konkreten Vorlagen (Buch mit Codesnipplet und Eeva) ergab sich direkt die Möglichkeit zur Erstellung eines lokalen Webservers. Dieser wird sozusagen "afp-enabled" gebaut. Dies...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Ausgehend von zwei konkreten Vorlagen (Buch mit Codesnipplet und Eeva) ergab sich direkt die Möglichkeit zur Erstellung eines lokalen Webservers. Dieser wird sozusagen "afp-enabled" gebaut. Dies ermöglicht es uns, dass wir autark ohne externen Webserver arbeiten können. Mögliche Anwendungsszenarien sind hierbei die Auslieferung auf CD und vorallem zum vereinfachten Entwickeln und Debuggen.

Die aktuelle Implementierung basiert auf dem Microsoft Winsock2 ActiveX Control. Dieses hat jedoch nach MSKB und einigen Onlinebeiträgen kleinere Bugs und die Limitierung auf 5 concurrent Connections. Naja, nicht weiter brutal, da man jederzeit eine andere Socketimplementierung drunter setzen könnte.

Die nächste Ausbaustufe wird die Implementierung des Webservers in .NET 1.1 und 2.0 sein. Hier liegt der rudimentäre Code in C# bereits vor. Der Ansatz basiert auf der Verwendung der System.Net.Sockets.TcpListener Klasse in Verbindung mit System.Threading - schliesslich soll der Server ja mehrere Clients zeitgleich bedienen können. Naja, eventuell gönne ich mir mal einen Blick in den QUellcode von Cassini bzw. XSP. Hier könnten sich potentiell noch Anregungen ergeben, wie man auch gleich ASP.NET integriert und per Factory Pattern sowie Plugins weitere Extension anbinden könnte... Naja, mal sehen, wie weit wir den Spass treiben wollen.

Aktuell bereitet mir die Konfiguration und die sonstigen Information wie Mimetypes, Logging, Fehlercodes und anderes ein wenig Kopfzerbrechen. Aber auch hier werden sich sicherlich coole Möglichkeiten finden. Und wenn's "nur" der Zugriff über Ole DB auf VFP Tabellen ist. Hm, dürfte wahrscheinlich die einfachste Lösung darstellen. Dadurch können beide Server (VFP und .NET) *hüstel* alle drei Server, über die identische Konfiguration und sonstigem Beiwerk gefahren werden. Spart mir Nerven und Zeit. Potentiell kann man sogar partitionieren, so dass multiple Instanzen möglich sind. Evtl. sogar mit der Option, dass sich der Webserver seinen Port selbständig im unpriviligierten Bereich sucht und bindet. Hierbei würden wir dann lediglich den letzten aktiven Port pro Implementierung irgendwo ablegen. Dies verkürzt im Normalfall den Startprozess.

[code comment="Portselektion beim Serverstart"]Start der Anwendung  
Konfig einlesen (Port, etc)  
Port prüfen  
- wenn bound, Schleife mit Randomport laufen lassen  
- neuen Port sichern  
Ausführung[/code]

Die zentrale Konfiguration könnte man entweder als DBF und/oder XML ablegen. Wahrscheinlich dürfte es am einfachsten für beide Systeme sein, wenn man eine XML-Datei eines DataSet / XmlAdapter verwendet. Nativer Zugriff auf beiden Seiten... mal testen.

Weitere Features? Aktuell noch keinen Plan...  
Bis denne, JoKi