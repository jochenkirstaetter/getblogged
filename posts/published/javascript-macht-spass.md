---
uid: javascript-macht-spass
title: JavaScript macht Spass
date: 2004-07-13
status: published
type: post
description: JavaScript macht Spass Vielleicht kennt ihr auch das Problem...Man hat eine brauchbare GUI in HTML server-seitig mittels einer Skriptsprache wie die Active FoxPro Pages - http://www.afpages.de - zusammengesetzt und die Kommunikation zwischen Client und Server harmoniert auch sehr gut, aber irgendwie bleibt das Gefühl, daß noch etwas fehlt.Nun, so ging
tags:
- Development
keywords: Development
metaTitle: JavaScript macht Spass
metaDescription: JavaScript macht Spass Vielleicht kennt ihr auch das Problem...Man hat eine brauchbare GUI in HTML server-seitig mittels einer Skriptsprache wie die Active FoxPro Pages - http://www.afpages.de - zusammengesetzt und die Kommunikation zwischen Client und Server harmoniert auch sehr gut, aber irgendwie bleibt das Gefühl, daß noch etwas fehlt.Nun, so ging
image: content/images/2004/07/photo-1517180102446-f3ece451e9d8.webp
ogImage: content/images/2004/07/photo-1517180102446-f3ece451e9d8-og.webp
ogTitle: JavaScript macht Spass
ogDescription: Vielleicht kennt ihr auch das Problem...
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
canonicalUrl: https://jochen.kirstaetter.name/javascript-macht-spass/
imageUrl: content/images/2004/07/photo-1517180102446-f3ece451e9d8.webp
twitterImageUrl: https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=014a8fb0191be5641c1be5b55e747076
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2004/07/photo-1517180102446-f3ece451e9d8.webp
featured: false
publishedAt: 2004-07-13T23:00:00Z
updatedAt: 2018-10-23T05:18:58Z
excerpt: Vielleicht kennt ihr auch das Problem...
twitterTitle: JavaScript macht Spass
twitterDescription: Vielleicht kennt ihr auch das Problem...
twitterImage: 
facebookTitle: JavaScript macht Spass
facebookDescription: Vielleicht kennt ihr auch das Problem...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
Vielleicht kennt ihr auch das Problem...

Man hat eine brauchbare GUI in HTML server-seitig mittels einer Skriptsprache wie die Active FoxPro Pages - [https://www.afpages.de](https://www.afpages.de) - zusammengesetzt und die Kommunikation zwischen Client und Server harmoniert auch sehr gut, aber irgendwie bleibt das Gefühl, daß noch etwas fehlt.

Nun, so ging es mir auch bei der Programmierung einer externen Website... Es handelt sich um eine Überarbeitung, die noch im Gange ist. Aber die primären Lebensfunktionen der Site sind vorhanden, es gibt ausreichend Content, aber... wie schon gesagt, es fehlt was.

Okay, die einzige Möglichkeit der Site mehr Leben und Interaktion mit dem Benutzer einzuhauchen besteht darin, daß man auf eine client-seitige Skriptsprache zurückgreift und darin kräftig programmiert. Als mögliche Kandidaten kommen max. 3 Kandidaten in Frage:

- JavaScript - der Platzhirsch
- JScript - die Sparversion von Microsoft
- VBScript - das Sicherheitsrisiko

Irgendwie fällt alles unter den Begriff ECMAScript, aber nagelt mich nicht über das Was und Wie fest. Nun denn, die Entscheidung ist sehr eindeutig zu Gunsten JavaScript ausgefallen, da die anderen keine echte Alternative darstellen und extremst an das Document Object Modell (DOM) des Internet Explorer gebunden sind.

JavaScript bietet aufgrund der Specs des W3C zudem alle Optionen für eine saubere, browserübergreifende Implementierung der gewünschten Funktionalität - und es läuft in allen Browsern... Ja, I know - Ausnahmen bestätigen die Regel und schimpfen sich Konqueror und Safari. Sorry, guys!

Aber wieder zurück zum Geschehen und der Idee: Mehr Interaktion mit dem Benutzer. Nun im konkreten Fall ging es um eine Wiki-GUI, deren server-seitige Engine bereits sehr ausgereift ist. Nach einer kurzen Analyse ergibt sich das Szenario, daß jede Seite durch einen Begriff bzw. durch das WikiWord eindeutig auffindbar ist. Okay, kleiner Suchdialog und fertig.  
Sofern dieser omnipräsent ist... In diesem Fall ist aber nicht so. Also kam mir die Idee eines 'versteckten' Suchdialogs.

Wir erinnern uns, das WikiWord ist entscheidend!

Die aktuelle Implementierung in JavaScript gestattet es, durch Doppelklick auf das aktuelle WikiWord die GUI auf eine 'Suchmaske' umzuschalten, welche durch Bestätigen mit Enter ausgelöst oder durch Klick irgendwo hin wieder geschlossen wird.

Einfach, aber praktisch, oder? Und Dank JavaScript funktioniert es in den meisten Browsern. 😎

Achja, noch eine kleine Anmerkung, es ist äußerst hilfreich mit den Browser aus der Mozilla-Familie zu testen, da diese sowohl eine JavaScript-Konsole als auch einen DOM Inspector bereitstellen. Was IMHO wesentlich mehr Vorteile als ein stupider Fehlerhinweis vom IE bietet. Aber das sei jeder/m selbst überlassen.  
Keep on coding! Bis denne, JoKi