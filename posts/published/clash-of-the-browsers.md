---
uid: clash-of-the-browsers
title: Clash of the browsers
slug: clash-of-the-browsers
date: 2005-03-13
status: published
type: post
description: Clash of the browsers Es ist immer wieder ern&#252;chternd, wenn man mit JavaScript das magere HTML-Frontend aufpeppen m&#246;chte. Nunja, heute ging&#39;s um Resizing von Frames... Wie Frames? - Ja, ich kann die Teile &#252;berhaupt nicht abhaben, aber manchmal geht&#39;s dann halt doch nicht anders. Und genau so einen Fall habe
tags:
- General
keywords: General
metaTitle: Clash of the browsers
metaDescription: Clash of the browsers Es ist immer wieder ern&#252;chternd, wenn man mit JavaScript das magere HTML-Frontend aufpeppen m&#246;chte. Nunja, heute ging&#39;s um Resizing von Frames... Wie Frames? - Ja, ich kann die Teile &#252;berhaupt nicht abhaben, aber manchmal geht&#39;s dann halt doch nicht anders. Und genau so einen Fall habe
image: ''
ogTitle: Clash of the browsers
ogDescription: Es ist immer wieder ernüchternd, wenn man mit JavaScript das magere HTML-Frontend aufpeppen möchte. Nunja, heute ging's um Resizing von Frames... Wie Frames? - Ja, ich kann die Teile überhaupt nicht...
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
authorImage: content/images/2018/10/JoKi_StAubin_100px.webp
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/clash-of-the-browsers/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2005-03-13T23:00:00Z
updatedAt: 2018-04-02T08:38:31Z
excerpt: Es ist immer wieder ernüchternd, wenn man mit JavaScript das magere HTML-Frontend aufpeppen möchte. Nunja, heute ging's um Resizing von Frames... Wie Frames? - Ja, ich kann die Teile überhaupt nicht...
twitterTitle: Clash of the browsers
twitterDescription: Es ist immer wieder ernüchternd, wenn man mit JavaScript das magere HTML-Frontend aufpeppen möchte. Nunja, heute ging's um Resizing von Frames... Wie Frames? - Ja, ich kann die Teile überhaupt nicht...
twitterImage: 
facebookTitle: Clash of the browsers
facebookDescription: Es ist immer wieder ernüchternd, wenn man mit JavaScript das magere HTML-Frontend aufpeppen möchte. Nunja, heute ging's um Resizing von Frames... Wie Frames? - Ja, ich kann die Teile überhaupt nicht...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Es ist immer wieder ernüchternd, wenn man mit JavaScript das magere HTML-Frontend aufpeppen möchte. Nunja, heute ging's um Resizing von Frames... Wie Frames? - Ja, ich kann die Teile überhaupt nicht abhaben, aber manchmal geht's dann halt doch nicht anders. Und genau so einen Fall habe ich gerade (oder immer noch).  
  
Okay, die optische Politur muss her, denn eine Verschmelzung zwischen Active FoxPro Pages und PHP soll zumindest auf den ersten Blick einigermaßen unsichtbar sein bzw. bleiben. Nein, nicht um AFP zu pushen, sondern ausschliesslich der Usability und Optik wegen. Zudem sind IFrames für solch einen Zweck einigermaßen zu gebrauchen.  
  
Well, was gilt es zu beachten? - zunächst einmal, dass potentiell der gewünschte Content erscheint. Dann gestaltet es sich weiterhin als interessant, dass der IFrame gefälligst ohne Scrollbar angezeigt wird... Und hier beginnen die Probleme.  
  
Die Breite ist noch einigermaßen easy zu kontrollieren, aber die Höhe des IFrame; da wird's schon ein klein wenig schwieriger. Oder zumindest kommt es mir so vor. Nun denn. Basierend auf einer interessanten Vorlage habe ich mich wieder in die Tiefen von JavaScript und Browser DOMs getraut, und wie zu erwarten auch gleich mal wieder einen auf den Deckel bekommen.  
  
Hier mal den aktuellen Code der Implementierung, damit klarer wird, wovon ich überhaupt spreche:  
  

```
  
function resizeFrame(objectID) {  
var e;  
var domFrame = findDOM(objectID);  
var domFrameStyle = findDOM(objectID,1);  
var domFrameDoc = (window.navigator.appName.toLowerCase().indexOf("netscape") > -1) ? domFrame.contentWindow.document : domFrame.document  
var fheight = 0;  
  
try {  
// Get absolute height of document inside the frame.  
fheight = domFrameDoc.body.scrollHeight;  
} catch(e) {  
window.status = "Exception: " + e.description;  
fheight = 1000;  
}  
domFrame.height = fheight;  
domFrameStyle.display = 'block';  
}  
```
  
  
Spannenderweise muss mit einem Try-Catch gearbeitet werden, da FireFox den Zugriff mit einer Exception quittiert. Und darin liegt auch die Sache ein wenig begraben. Ich hab's ebenfalls mittels Statusabfrage von document.readyState probiert, aber auch dann sieht's nicht besser aus.  
  
More to come...  
  
  
Bis denne, JoKi