---
uid: ein-knigreich-fr-eine-bernachtung
title: Ein Königreich für eine Übernachtung
slug: ein-knigreich-fr-eine-bernachtung
date: 2006-09-08
status: published
type: post
description: Ein Königreich für eine Übernachtung **Kein Zimmer mehr frei...**So ging es mir von Donnerstag auf Freitag. Auf Grund einer nicht abgesprochenen Annahme war nicht ganz klar, wieviele Nächte für den Workshop gebucht werden sollten. Nunja, und da kam dann noch Murphy's Law mit ins Spiel. Denn selbst eine Verlängerung des
tags:
- General
keywords: General
metaTitle: Ein Königreich für eine Übernachtung
metaDescription: Ein Königreich für eine Übernachtung **Kein Zimmer mehr frei...**So ging es mir von Donnerstag auf Freitag. Auf Grund einer nicht abgesprochenen Annahme war nicht ganz klar, wieviele Nächte für den Workshop gebucht werden sollten. Nunja, und da kam dann noch Murphy's Law mit ins Spiel. Denn selbst eine Verlängerung des
image: ''
ogTitle: Ein Königreich für eine Übernachtung
ogDescription: So ging es mir von Donnerstag auf Freitag. Auf Grund einer nicht abgesprochenen Annahme war nicht ganz klar, wieviele Nächte für den Workshop gebucht werden sollten. Nunja, und da kam dann noch...
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
canonicalUrl: https://jochen.kirstaetter.name/ein-knigreich-fr-eine-bernachtung/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-09-08T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: So ging es mir von Donnerstag auf Freitag. Auf Grund einer nicht abgesprochenen Annahme war nicht ganz klar, wieviele Nächte für den Workshop gebucht werden sollten. Nunja, und da kam dann noch...
twitterTitle: Ein Königreich für eine Übernachtung
twitterDescription: So ging es mir von Donnerstag auf Freitag. Auf Grund einer nicht abgesprochenen Annahme war nicht ganz klar, wieviele Nächte für den Workshop gebucht werden sollten. Nunja, und da kam dann noch...
twitterImage: 
facebookTitle: Ein Königreich für eine Übernachtung
facebookDescription: So ging es mir von Donnerstag auf Freitag. Auf Grund einer nicht abgesprochenen Annahme war nicht ganz klar, wieviele Nächte für den Workshop gebucht werden sollten. Nunja, und da kam dann noch...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

## Kein Zimmer mehr frei...

So ging es mir von Donnerstag auf Freitag. Auf Grund einer nicht abgesprochenen Annahme war nicht ganz klar, wieviele Nächte für den Workshop gebucht werden sollten. Nunja, und da kam dann noch Murphy's Law mit ins Spiel. Denn selbst eine Verlängerung des Aufenthalts im Hotel war nicht machbar, da komplett ausgebucht. Hm, okay, in der Nacht noch einen Hilfeaufruf per Mail an die Kollegen zuhause abgeschickt und mal abwarten was passiert. Starten wir den Tag mit Frühstück und dann in den Endspurt des AFP Workshops. Heute wenden wir das Wissen der bisherigen zwei Tage konkret in einer Prototypanwendung an. Wir wollen eine Kombination aus Code Review, Refactoring und Vermittlung von Best Practices umsetzen. Ganz im Sinne des Kunden, der seine AFP Webanwendung sauber und leicht implementieren möchte. Hier gilt es auch Augenmerk auf die Erweiterbarkeit und Wartbarkeit zu legen.

## Murphy's Law

Oder wieso funktionieren die Internet Information Services auf einmal nicht mehr? Zur Sichtung des Prototypen erstellen wir ein neues Entwicklungsverzeichnis, konfigurieren eine neue virtuelle Site im IIS und wollen den ersten Aufruf der Anwendung durchführen. Könnte ja sein, dass noch weitere Einstellungen vorzunehmen sind. Nun, dann ging's los... HTML und Grafiken werden aufgerufen, aber keine AFP-Dokumente. Nun, im ControlCenter wird ersichtlich, dass die Requests vom IIS nicht in der AFP ankommen. Okay, Prüfung der Eigenschaften, kein Erfolg... hm, dann das bewährte Hausmittel bei Windows: Reboot

Und ja, nach dieser kurzen Zwangspause sind wir wieder im Boot und können weiterarbeiten. Na also, sieht soweit schon mal gut aus. Und von den Teilnehmern kommen auch die ersten Anregungen und Ideen zur Veränderung. Okay, dann mal die Arme hochkrempeln und die Applikation zerlegt. Dazu splitten wir die vorhandenen AFP-Dokumente in ihre Bestandteile:

- HTML-Vorlagen und -Bausteine,
- CSS-Formatvorlagen,
- JavaScript,
- AFP-Anwendung und
- CodeBehind zur Auslagerung der genutzten Funktionalität.

Einiges wandeln wir bereits in Klassen um. Und so bringen wir auch noch die restlichen Stunden des Tages unter den Hut.

## Übernachtung gesichert

Puuh, keine Notwendigkeit die Bahnhofsmission zu beehren. Und besser konnte es nicht werden. Direkt ein Hotel am Flughafen. Also, immerhin die Möglichkeit ein wenig auszuschlafen, zu frühstücken und dann frisch und erholt nach Prag fliegen. Nur... welches Hotel und welcher Flughafen. Es ist nicht gerade hilfreich, wenn Buchungsadresse und Internetinformationen zum Hotel voneinander abweichen und der Lageplan ebenfalls nicht passt. Nunja, erstmal zum Berliner Hbf, von dort aus mal weiterschauen... Nach einem kurzen Anruf beim Hotel war die Lage geklärt und die Anfahrt gesichert. Gut, nichts wie hin... Relaxen und evtl. abends wieder in die Innenstadt.

Bis denne, JoKi
