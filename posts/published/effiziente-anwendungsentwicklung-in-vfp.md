---
uid: effiziente-anwendungsentwicklung-in-vfp
title: Effiziente Anwendungsentwicklung in VFP
slug: effiziente-anwendungsentwicklung-in-vfp
date: 2006-04-29
status: published
type: post
description: Effiziente Anwendungsentwicklung in VFP Anwendungsentwicklung, Softwaredesign, Design, Visual FoxProDen heutigen Tag habe ich f&#252;r die Korrekturlesung des deutschsprachigen Buches 'Effiziente Anwendungsentwicklung in VFP' aus dem Verlag Hentzenwerke genutzt. Eigentlich sollte der Titel bereits Anfang des Jahres erschienen sein, aber die gegenw&#228;rtige Fassung bedarf noch einiger Anpassungen. Es handelt sich bei
tags:
- Recension
keywords: Recension
metaTitle: Effiziente Anwendungsentwicklung in VFP
metaDescription: Effiziente Anwendungsentwicklung in VFP Anwendungsentwicklung, Softwaredesign, Design, Visual FoxProDen heutigen Tag habe ich f&#252;r die Korrekturlesung des deutschsprachigen Buches 'Effiziente Anwendungsentwicklung in VFP' aus dem Verlag Hentzenwerke genutzt. Eigentlich sollte der Titel bereits Anfang des Jahres erschienen sein, aber die gegenw&#228;rtige Fassung bedarf noch einiger Anpassungen. Es handelt sich bei
image: ''
ogTitle: Effiziente Anwendungsentwicklung in VFP
ogDescription: Anwendungsentwicklung, Softwaredesign, Design, Visual FoxPro
layout: post
bodyClass: post-template tag-recension
postClass: post tag-recension
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
canonicalUrl: https://jochen.kirstaetter.name/effiziente-anwendungsentwicklung-in-vfp/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-29T11:08:54Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Anwendungsentwicklung, Softwaredesign, Design, Visual FoxPro
twitterTitle: Effiziente Anwendungsentwicklung in VFP
twitterDescription: Anwendungsentwicklung, Softwaredesign, Design, Visual FoxPro
twitterImage: 
facebookTitle: Effiziente Anwendungsentwicklung in VFP
facebookDescription: Anwendungsentwicklung, Softwaredesign, Design, Visual FoxPro
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Anwendungsentwicklung, Softwaredesign, Design, Visual FoxPro

Den heutigen Tag habe ich für die Korrekturlesung des deutschsprachigen Buches "Effiziente Anwendungsentwicklung in VFP" aus dem Verlag Hentzenwerke genutzt. Eigentlich sollte der Titel bereits Anfang des Jahres erschienen sein, aber die gegenwärtige Fassung bedarf noch einiger Anpassungen. Es handelt sich bei diesem Buch übrigens um die Übersetzung und Aktualisierung des englischen Titels "Effective Techniques for Application Development with Visual FoxPro" für Visual FoxPro 9.0. Mit der stetigen Weiterentwicklung von VFP und neuen Features wie etwa aktualisierbare Cursor, CursorAdapter-Klasse und die ganzen XML-Fähigkeiten ergeben sich natürlich auch neue Bewertungen für die effiziente Anwendungsentwicklung. Das Buch umfasst derzeit 14 Kapitel und vier Anhänge verteilt auf über 370 Seiten.

Die deutschsprachige FoxPro User Group (dFPUG) hat sich für die Übersetzung und Aktualisierung des Buchtitels stark gemacht, da insbesondere in den Foren und in den Newsgruppen zu Visual FoxPro ständig wiederholend Fragen und Problemstellungen zur besseren Nutzung von VFP auftreten. Leider entsteht hier der Eindruck, dass sehr viele Entwickler unterhalb der 50% Leistungsfähigkeit von VFP arbeiten und damit viele Vorzüge und Leistungen ihrer Programmiersprache und Datenbank eben verschenken und darüberhinaus wertvolle Zeit durch die Entwicklung paralleler Funktionalitäten vergeuden.

Ich muss gestehen, dass ich durch die Arbeit mit dem Buch, den leichten Umformulierungen und der Prüfung der vorliegenden Codebeispiele selbst einen sehr guten Einblick in die Funktionsweise und Nutzung von Ansichten erhalten habe. In meinen bisherigen sieben Jahren Entwicklung unter Visual FoxPro habe ich ausschliesslich mit selbsterzeugten Cursorn und SQL PassThrough (SPT) gearbeitet. Dies liegt aber auch daran, dass wir eine eigene Datenbankabstraktionsschicht in sämtlichen Projekten einsetzen und damit einen objektorientierten Zugriff auf die Datenquellen besitzen. Dennoch bieten Views (zu deutsch Ansichten) unabhängig davon viele Vorzüge gegenüber dem direkten Zugriff auf lokale Tabellen und der alleinstehenden Arbeit mit SPT. Die CursorAdapter-Klasse erweitert diese Funktionalität sogar noch weiter, in der Hinsicht, dass eine bessere Kontrolle über die Datenmanipulation der zugrundeliegenden Datenquelle möglich ist.
