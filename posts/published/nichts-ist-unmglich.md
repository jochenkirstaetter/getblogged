---
uid: nichts-ist-unmglich
title: Nichts ist unmöglich...
slug: nichts-ist-unmglich
date: 2010-01-24
status: published
type: post
description: 'Durch das Verständnis des grundsätzlichen Aufbaus von ASP.NET und dessen Ablaufsequenz ergaben sich mehrere Ansätze. Dennoch habe ich mich in Bezug auf 2.0 für die Entwicklung eines HttpHandlers entschieden. Das Grundkonzept dabei ist ziemlich easy: Man nehme das Interface IHttpHandler und code ein paar Zeilen hinein, passe die Web.config noch ein wenig an und voilá: Funktioniert.'
tags:
- Development
keywords: Development
metaTitle: Nichts ist unmöglich...
metaDescription: 'Durch das Verständnis des grundsätzlichen Aufbaus von ASP.NET und dessen Ablaufsequenz ergaben sich mehrere Ansätze. Dennoch habe ich mich in Bezug auf 2.0 für die Entwicklung eines HttpHandlers entschieden. Das Grundkonzept dabei ist ziemlich easy: Man nehme das Interface IHttpHandler und code ein paar Zeilen hinein, passe die Web.config noch ein wenig an und voilá: Funktioniert.'
image: ''
ogTitle: Nichts ist unmöglich...
ogDescription: '...wenn man einer Idee Leben einhaucht und die Chance nutzt, diese zu realisieren. Ähnlich wie bei der Active FoxPro Pages 3.0 IntelliSense Extension (AFP3IE) schwirrte mir seit Monaten die...'
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
canonicalUrl: https://jochen.kirstaetter.name/nichts-ist-unmglich/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2010-01-24T09:14:11Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: '...wenn man einer Idee Leben einhaucht und die Chance nutzt, diese zu realisieren. Ähnlich wie bei der Active FoxPro Pages 3.0 IntelliSense Extension (AFP3IE) schwirrte mir seit Monaten die...'
twitterTitle: Nichts ist unmöglich...
twitterDescription: '...wenn man einer Idee Leben einhaucht und die Chance nutzt, diese zu realisieren. Ähnlich wie bei der Active FoxPro Pages 3.0 IntelliSense Extension (AFP3IE) schwirrte mir seit Monaten die...'
twitterImage: 
facebookTitle: Nichts ist unmöglich...
facebookDescription: '...wenn man einer Idee Leben einhaucht und die Chance nutzt, diese zu realisieren. Ähnlich wie bei der Active FoxPro Pages 3.0 IntelliSense Extension (AFP3IE) schwirrte mir seit Monaten die...'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
...wenn man einer Idee Leben einhaucht und die Chance nutzt, diese zu realisieren. Ähnlich wie bei der Active FoxPro Pages 3.0 IntelliSense Extension (AFP3IE) schwirrte mir seit Monaten die Vorstellung durch den Kopf, dass man die Kommunikation zwischen Webserver und der AFP Core Engine auch über andere Wege als die ISAPI realisieren müsste / könnte.  
Mein ursprünglicher Ansatz dabei galt der Erstellung eines Dynamic Shared Object (DSO) für den Apache Webserver. Mangels Kenntnisse und Fähigkeiten in C++ habe ich diesen Ansatz jedoch frühzeitig auf Eis gelegt. Also... falls ein ambitionierter C++-Coder mit Wissen zur DSO-Erstellung hier lesen sollte, bitte melden.  
Well, parallel zur Entstehung der Idee hatte ich mir bereits einiges Wissen über das .NET Framework und insbesondere C# - egal ob System.Windows.Forms oder System.Web - angeeignet. Und darin lag auch der Schlüssel zur ersten Implementierung der Lösung. Glücklicherweise stehen mir als Regionalleiter der dFPUG und damit als Mitglied der INETA die Buchzuwendungen der letzten Quartale zur Verfügung. Und das Wälzen in eben dieser Literatur verlieh Flügel. Insbesondere die folgenden Bücher waren extremst lehrreich:  
  
- C# Essentials  
- Visual C# .NET Programmier-Rezepte  
- Introducing ASP.NET 2.0  
- ASP.NET 2.0 - Step by step  
  
Durch das Verständnis des grundsätzlichen Aufbaus von ASP.NET und dessen Ablaufsequenz ergaben sich mehrere Ansätze. Dennoch habe ich mich in Bezug auf 2.0 für die Entwicklung eines HttpHandlers entschieden. Das Grundkonzept dabei ist ziemlich easy: Man nehme das Interface IHttpHandler und code ein paar Zeilen hinein, passe die Web.config noch ein wenig an und voilá: Funktioniert.  
  
Okay, ganz so easy war's dann doch wieder nicht. Denn... Schliesslich muss ja auch noch eine Kommunikation mit der AFP Core Engine erfolgen. Und das brachte mir doch einige schlaflose Nächte... Inzwischen ist auch hier Erfolg zu verzeichnen. Die Pflichtübung ist sozusagen erfüllt, jetzt beginnt die Kür. Was damit wiederum heißt: Verfeinerung, Stabilisierung und Dokumentation.  
Interessanterweise konnte ich die Umsetzung zuerst innerhalb der Programmierung einer Windows.Forms Anwendung realisieren. Was mich damit dann wiederum zu dem Schluß bringt, dass künftig die Verschmelzung der AFP Core Engine mit anderen Programmiersprachen kaum mehr Probleme bereiten dürfte. Nein, eher sogar im Gegenteil, da mit den jetzigen Erfahrungen die Implementierung von weiteren Clients sehr einfach von der Hand gehen dürfte.  
  
  
Bis denne, JoKi  
  
Achja, nur so als informativen Hinweis: Ich verwende kein COM-Interop, da wir bei der AFP-Entwicklung explizit auf das COM-Interface aus den unterschiedlichsten Gründen verzichtet haben.
