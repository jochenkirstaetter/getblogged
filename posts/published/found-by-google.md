---
uid: found-by-google
title: Found by Google
slug: found-by-google
date: 2005-04-10
status: published
type: post
description: Found by Google Die Website ist ohne Frames erstellt, der Content eingepflegt und der Launch offiziell angekündigt, aber... Was dann? Wie findet man nun eine Site? Wie bekommt man Traffic auf die Domain? Well, ein Eintrag in Suchmaschinen muss her. Und nicht nur, in einer oder zwei, sondern in
tags:
- General
keywords: General
metaTitle: Found by Google
metaDescription: Found by Google Die Website ist ohne Frames erstellt, der Content eingepflegt und der Launch offiziell angekündigt, aber... Was dann? Wie findet man nun eine Site? Wie bekommt man Traffic auf die Domain? Well, ein Eintrag in Suchmaschinen muss her. Und nicht nur, in einer oder zwei, sondern in
image: ''
ogTitle: Found by Google
ogDescription: Die Website ist ohne Frames erstellt, der Content eingepflegt und der Launch offiziell angekündigt, aber... Was dann? Wie findet man nun eine Site? Wie bekommt man Traffic auf die Domain?
layout: post
bodyClass: post-template tag-general
postClass: post tag-general
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
canonicalUrl: https://jochen.kirstaetter.name/found-by-google/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2005-04-10T00:00:00Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Die Website ist ohne Frames erstellt, der Content eingepflegt und der Launch offiziell angekündigt, aber... Was dann? Wie findet man nun eine Site? Wie bekommt man Traffic auf die Domain?
twitterTitle: Found by Google
twitterDescription: Die Website ist ohne Frames erstellt, der Content eingepflegt und der Launch offiziell angekündigt, aber... Was dann? Wie findet man nun eine Site? Wie bekommt man Traffic auf die Domain?
twitterImage: 
facebookTitle: Found by Google
facebookDescription: Die Website ist ohne Frames erstellt, der Content eingepflegt und der Launch offiziell angekündigt, aber... Was dann? Wie findet man nun eine Site? Wie bekommt man Traffic auf die Domain?
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Die Website ist **ohne Frames** erstellt, der Content eingepflegt und der Launch offiziell angekündigt, aber... Was dann? Wie findet man nun eine Site? Wie bekommt man Traffic auf die Domain?  
  
Well, ein Eintrag in Suchmaschinen muss her. Und nicht nur, in einer oder zwei, sondern in einigen... Richtig? - Meiner Meinung nach, nein. Denn IMHO ist es ausreichend, wenn man sich primär um eine Suchmaschine kümmert: Google.  
  
Und da gibt's ein bisschen was zu beachten, aber gleich mehr dazu. Ich möchte lediglich ein Live-Beispiel anführen:  
  
[https://www.google.de/search?q=FoxPro](https://www.google.de/search?q=FoxPro)  
[https://www.google.de/search?hl=de&q=FoxPro&btnG=Suche&meta=lr%3Dlang](https://www.google.de/search?hl=de&q=FoxPro&btnG=Suche&meta=lr%3Dlang)  
\_de  
[https://www.google.de/search?hl=de&q=FoxPro&btnG=Suche&meta=cr%3Dcoun](https://www.google.de/search?hl=de&q=FoxPro&btnG=Suche&meta=cr%3Dcoun)  
tryDE  
  
Es handelt sich dreimal um die gleiche Suchabfrage - nämlich "FoxPro" - mit unterschiedlichen Ausprägungen im Web, im deutschsprachigen Raum und aus Deutschland.  
  
Wie kommt man zu einem solchen Ergebnis? - Nun, die Frage ist nicht einfach zu beantworten, dennoch möchte ich meine Erfahrung dazu ein wenig offenlegen. Zu allererst ist es wichtig, dass man die **MetaTags der HTML-Dokumente** korrekt und ausreichend ausfüllt:  
meta name="description" content="..."  
meta name="abstract" content="..."&gt;  
meta name="keywords" content="..."&gt;  
meta name="modified" content="Wed, 01 Dec 2004 09:44:27 GMT+2"  
  
Dabei sind natürlich Begriffe zu wählen, die zum einen den Kernbereich des Inhalts treffen und zum anderen keinesfalls auf verwandte Begriffe verzichten (diese sind fast wichtiger)... ![icon_biggrin](https://jochen.kirstaetter.name/found-by-google/smilies/icon_biggrin.gif)  
Gut, dann natürlich eine Datei namens 'robots.txt' im Root der Site anlegen und befüllen:

# [https://www.searchengineworld.com/robots/robots_tutorial.htm](https://www.searchengineworld.com/robots/robots_tutorial.htm)  
  
User-agent: \*  
Disallow: /.svn/  
Disallow: /awstats/  
Disallow: /images/  
Disallow: /staff/  
Disallow: /svn/  
Disallow: /websvn/  
  
Achja, ein beliebter Fehler ist es, sogenannten 'nicht sichtbaren Text' in den Dokumenten zu verwenden - also schwarz auf schwarz - lasst es... Das wird erkannt und verursacht negative Faktoren.  
  
Das sind mal die grundlegenden Aspekte, damit bietet man Suchmaschinen ausreichend Basisnahrung liefert, so dass eine korrekte Indizierung der Site erfolgen kann. Aber...  
  
Das erklärt nicht, wie man auf die höheren Ergebnisränke kommt. Und nun kommt ein kleiner Kniff, den ich nachweisbar erfolgreich anwenden konnte und anwende: Die Manipulation des HTTP-Headers der Response in Bezug auf die Datumswerte der Dokumente. Hier mal ein Beispiel (auszugsweise):  
  
Date: Sun, 10 Apr 2005 08:27:28 GMT  
Expires: Mon, 11 Apr 2005 09:27:29 GMT  
X-Powered-By: AFP/3.0.579  
Last-Modified: Wed, 01 Dec 2004 09:44:27 GMT  
  
Das Expire der Seite liegt (hier 25 Std in der Zukunft), was wiederum den Suchmaschinen einen Anlass gibt - "Hmm, da könnte ich mal wieder reinschauen...". Außerdem halte ich den Zeitpunkt der letzten Änderung ebenfalls für sehr wichtig, wenn nicht sogar als den wichtigsten Aspekt einer Site. Denn mal ehrlich, was interessiert einen selbst, wenn man eine Suchmaschine benutzt? - Aktuelle Informationen oder Ressourcen zu einem bestimmten Thema. Ergo, mit einem zeitnahen Last Modifier bietet man aktuelle Informationen an, und die Suchmaschine "Hey, die Site ist aktuell, da muss sicherlich was Neues stehen." nimmt die Site entsprechend auf.  
  
Und das ist IMHO alles, was es benötigt mittel- bis langfristig sehr gute Rankings in Google und darüber in anderen Suchmaschinen zu erhalten. Von sogenannten Massensubskriptionen zu schiess-mich-tot-wievielen Suchdiensten halte ich persönlich überhaupt nichts, sondern sehe darin sogar ein Problem, das zu negativen Ergebnissen führen könnte.  
  
Wäre mal cool, zu erfahren, wie eure bisherigen Erfahrungen zu Google sind und ob meine Tipps euch in 2,3 Monaten weiterhelfen konnten.  
  
  
Bis denne, JoKi
