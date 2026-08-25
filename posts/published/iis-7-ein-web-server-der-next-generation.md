---
uid: iis-7-ein-web-server-der-next-generation
title: "\"IIS 7 - Ein Web-Server der 'Next Generation'?\""
date: 2006-04-27
status: published
type: post
description: Der Stratege denkt an Web 2.0, der Entwickler vielleicht an AJAX, Webservices, etc. Schön wäre dabei natürlich auch einen Web-Server zu haben, welcher mit der Entwicklung Schritt halten kann.
tags:
- Development
keywords: Development
metaTitle: "\"IIS 7 - Ein Web-Server der 'Next Generation'?\""
metaDescription: Der Stratege denkt an Web 2.0, der Entwickler vielleicht an AJAX, Webservices, etc. Schön wäre dabei natürlich auch einen Web-Server zu haben, welcher mit der Entwicklung Schritt halten kann.
image: ''
ogTitle: "\"IIS 7 - Ein Web-Server der 'Next Generation'?\""
ogDescription: Es wird interessant werden...
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
canonicalUrl: https://jochen.kirstaetter.name/iis-7-ein-web-server-der-next-generation/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-27T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: Es wird interessant werden...
twitterTitle: "\"IIS 7 - Ein Web-Server der 'Next Generation'?\""
twitterDescription: Es wird interessant werden...
twitterImage: 
facebookTitle: "\"IIS 7 - Ein Web-Server der 'Next Generation'?\""
facebookDescription: Es wird interessant werden...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Es wird interessant werden...

\*Der Stratege denkt an Web 2.0, der Entwickler vielleicht an AJAX, Webservices, etc.  
Schön wäre dabei natürlich auch einen Web-Server zu haben, welcher mit der Entwicklung Schritt halten kann. Ist IIS 7 die richtige Antwort für Sie? Bilden Sie sich Ihre eigene Meinung.\*

## Anflug
Am Dienstag Abend ging's mal wieder auf Achse. Dieses Mal nach Stuttgart auf einen Microsoft TechTalk zum IIS 7.0. Stuggi, klar, dass wir auch einen kleinen Schwenk über Wendlingen machen und den Tiger abholen. Schliesslich gilt es wieder als 'DreamTeam' vertreten zu sein. Zusammen mit Willi liefen wir dann wetter- und verkehrsbedingt ein wenig verspätet im Novotel in Stuttgart Stammheim und genossen den informativen Beitrag von Bernhard Frank.

## IIS 7 ist neu
Klar, das ergibt sich ja bereits implizit, da Windows Vista bzw. Longhorn Server aktuell in der Betaphase sind. Dennoch sind die Umbaumaßnahmen im IIS und die Modularisierung wirklich interessant gelöst worden. Aus den bisher unabhängigen Eventhandlings im Webserver und der ASP.NET Umgebung wurde eins. Weiterhin ist das Konzept für ISAPI Filter und ISAPI Extensions vollständig dem Refactoring zu Gute gefallen. Die Details und massigen Featurelisten werden sicherlich auf den offiziellen Produktseiten zu finden sein, ich spare mir u.a. aus Platzgründen die Wiederholung 🙂

## ISAPI und andere Schnittstellen
Interessant ist auf alle Fälle die Option, dass weiterhin bestehende ISAPI Extensions wie beispielsweise [Active FoxPro Pages](https://www.afpages.de) direkt nutzbar sein werden, und dass weitere Schnittstellen für die Entwicklung von Server-Addons bereitstehen. Dies wurde auch eindrucksvoll anhand von verschiedenen ISAPI Filter per IHttpModule Schnittstelle gezeigt. Für die Implementierung von ISAPI Extension empfiehlt sich die Verwendung der IHttpHandler-Klasse. Was übrigens in keinster Weise auf den IIS 7 speziell ausgelegt ist. Man kann bereits seit einiger Zeit im .NET Framework eigene HttpModule und HttpHandler schreiben und im IIS 5.x bzw. IIS 6 nutzen. Das Neue dabei ist, dass dies nun global und applikationsspezifisch konfiguriert und genutzt werden kann. Achja, neben den .NET Interfaces IHttpModule und IHttpHandler gibt's die nahezu identische API für native Programmierung, etwa C oder C++, in Form von CHttpModule und CHttpHandler.

## Monolithische Konfiguration
Neben den sehr hohen Ähnlichkeiten zu den Dynamic Shared Objects (DSO) des Apache kamen wir dennoch in der Pause zu einem Punkt, der weiterhin im IIS nach meinem Verständnis unzureichend gelöst ist und wurde. Die XML-Konfiguration für den Webserver bzw. die Website ist weiterhin monolithisch und gestattet es nicht, dass man die Konfiguration über mehrere Dateien splitten und nutzen kann. Das ist wirklich schade.  
Sicher taucht nun die Frage auf, wozu man das brauchen sollte... Nun, ganz einfach. Wir nehmen mal eine ASP.NET Anwendung eines Drittanbieters, exemplarisch DotNetNuke oder eben sonstwas. Die gängigen Einstellungen werden in der *web.config* hinterlegt und genutzt. Vielleicht eben auch individuelle Vorlieben und so. Im Falle eines Upgrade der Software mit Erweiterungen und/oder Korrekturen an der grundsätzlichen Konfiguration laufen wir in ein Problem hinein. Zwar nur ein leichtes, aber auf Dauer und steigende Häufigkeit wird es sicherlich zur Nervensäge. Hier bietet der Apache mit der **Include-Direktive** ganz erhebliche Vorteile.

## Tolle Demos und runde Sache
Insgesamt bleibt bei mir der Eindruck zurück, dass das IIS-Developerteam weiter ihre Hausaufgaben gemacht haben und dem Riesenmonster IIS in der siebten Version sehr stark die Federn gestutzt haben. Bereits mit dem IIS 6 und den verschärften Sicherheitseinstellungen stieg die Gunst, aber mit der neuen Modularisierung, der Entrümpelung der Architektur und den vereinfachten Programmierschnittstellen wird der Microsoft Webserver interessanter.

## Active FoxPro Pages
Ehrlich gesagt, bin ich persönlich noch nicht dazu gekommen AFP im IIS 7 zu testen. Dennoch sind die bisherigen Aussagen von Microsofties und IIS-Experten eintönig, dass bestehende ISAPIs problemlos funktionieren werden. Beruhigend zu wissen. Dennoch werde ich eventuell die nächste Zeit mal für einen ausführlicheren Test unter Windows Vista Beta nutzen und berichten. Und wie ich schon sagte, die IHttpHandler-Klasse kann man schon länger nutzen... Hier wird es sicherlich auch noch Neuigkeiten geben.  
Bis denne, JoKi