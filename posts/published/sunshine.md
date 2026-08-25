---
uid: sunshine
title: 'Sunshine (Codename: Moonwalk)'
date: 2009-12-14
status: published
type: post
description: Ein zur Erfassung von Daten sportlicher Aktivitäten und später irgendwann einmal auch statistische Auswertungen. Wow, noch eine Software im Sinne eines 'Personaltrainers'. Hast du nicht gesehen... Well, ja, irgendwie in der Art soll es etwas werden, aber vielleicht auch mehr. Der Ausgang dieses Projektes ist offen...
tags:
- Projects
keywords: Projects
metaTitle: 'Sunshine (Codename: Moonwalk)'
metaDescription: Ein zur Erfassung von Daten sportlicher Aktivitäten und später irgendwann einmal auch statistische Auswertungen. Wow, noch eine Software im Sinne eines 'Personaltrainers'. Hast du nicht gesehen... Well, ja, irgendwie in der Art soll es etwas werden, aber vielleicht auch mehr. Der Ausgang dieses Projektes ist offen...
image: ''
ogTitle: 'Sunshine (Codename: Moonwalk)'
ogDescription: Ein zur Erfassung von Daten sportlicher Aktivitäten und später irgendwann einmal auch statistische Auswertungen. Wow, noch eine Software im Sinne eines 'Personaltrainers'. Hast du nicht gesehen...
layout: post
bodyClass: post-template tag-projects
postClass: post tag-projects
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
canonicalUrl: https://jochen.kirstaetter.name/sunshine/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2009-12-14T09:05:14Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Ein zur Erfassung von Daten sportlicher Aktivitäten und später irgendwann einmal auch statistische Auswertungen. Wow, noch eine Software im Sinne eines 'Personaltrainers'. Hast du nicht gesehen...
twitterTitle: 'Sunshine (Codename: Moonwalk)'
twitterDescription: Ein zur Erfassung von Daten sportlicher Aktivitäten und später irgendwann einmal auch statistische Auswertungen. Wow, noch eine Software im Sinne eines 'Personaltrainers'. Hast du nicht gesehen...
twitterImage: 
facebookTitle: 'Sunshine (Codename: Moonwalk)'
facebookDescription: Ein zur Erfassung von Daten sportlicher Aktivitäten und später irgendwann einmal auch statistische Auswertungen. Wow, noch eine Software im Sinne eines 'Personaltrainers'. Hast du nicht gesehen...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
## Project: Sunshine

Ein zur Erfassung von Daten sportlicher Aktivitäten und später irgendwann einmal auch statistische Auswertungen. Wow, noch eine Software im Sinne eines 'Personaltrainers'. Hast du nicht gesehen... Well, ja, irgendwie in der Art soll es etwas werden, aber vielleicht auch mehr. Der Ausgang dieses Projektes ist offen...

Das Interessante an diesem Projekt wird jedoch die Herangehensweise der Entwicklung sein. Denn obwohl oder gerade weil es in Visual FoxPro realisiert wird, möchte ich mit diesem Projekt ein persönliches Experiment angehen. Und zwar werde ich entgegen meiner üblichen Vorgehensweise diese Anwendung mal rein aus der Sicht des Anwenders aufbauen. Also, was sehe ich? Wie funktioniert es und wie fühlt es sich an. Ich meine, dass man solch eine Vorgehensweise 'Top-Down-Design' nennt, lasse mich aber gerne eines Besseren belehren.

Okay, also ausgehend vom Grundsatz **Hauptsache, es sieht gut aus!** schreibe ich aktuell an der Gesamtoberfläche und an den visuellen Komponenten. Und in der Tat sieht die Software bereits schon ein wenig stylisch aus. Anbei mal ein Screenshot:

{vsig}sunshine{/vsig}

Und damit sind wir sicherlich auch beim ersten Problem des Abends... Entwickler sind keine Designer, und wirklich gut aussehende Grafiken, Icons und Pictures sind auch in den Weiten des Internets schwer zu bekommen, zumindest wenn man sehr genaue Vorstellungen für das Gesamtbild der Anwendung hat. Falls sich also jemand oder auch mehrere Grafiker/Designer bereit erklären möchten, dem Projekt ein wenig was beizusteuern. Gerne, schreibt mir eine Mail, skypt mich an, etc...

Bei der Betrachtung der technischen Details möchte ich für die Entwicklung des Projekts folgende Rahmenpunkte abstecken:

- [Visual FoxPro 9.0 Service Pack 2](https://msdn.com/vfoxpro/)  
- [Acodey Komponentenbibliothek](https://www.acodey.de) - die eigentliche Power im Projekt  
- [GDIPlusX](https://www.codeplex.com/) aus dem VFPX Community Projekt  
- freie Grafiken und Icons  
- [unzählige Blogartikel](https://weblogs.foxite.com) mit Ideen, Anregungen und Lösungen

Das Datenbankdesign werde ich erst zu einem späteren Zeitpunkt angehen, denn aktuell schwirren meine Gedanken noch viel zu sehr durch den Kopf. Das wird sich mit der Zeit legen und dann folgt das ERM. Die Entscheidung für eine bestimmte Datenbank obliegt mir Dank Komponenten aus Acodey nicht. Dennoch wird der VFP DBC als erster Storage zum Einsatz kommen. Für die Ausgabe von Auswertungen werde ich in diesem Projekt auf die Fähigkeiten der VFP 9.0 Reportengine zurückgreifen.