---
uid: vfp-stammtisch-stuttgartherrenberg
title: VFP Stammtisch - Stuttgart/Herrenberg
slug: vfp-stammtisch-stuttgartherrenberg
date: 2005-07-15
status: published
type: post
description: VFP Stammtisch - Stuttgart/Herrenberg On the road again...Einmal im Jahr sollte es sein, und auch dieses Mal hat es wieder geklappt. Leider mit einem kleinen Nebeneffekt von einer halben Stunde Verspätung, aber es gibt wahrscheinlich schlimmeres. Trotzdem meine Entschuldigung an die Teilnehmer gestern, dass wir nicht wie ausgemacht ab 19:30
tags:
- Community
keywords: Community
metaTitle: VFP Stammtisch - Stuttgart/Herrenberg
metaDescription: VFP Stammtisch - Stuttgart/Herrenberg On the road again...Einmal im Jahr sollte es sein, und auch dieses Mal hat es wieder geklappt. Leider mit einem kleinen Nebeneffekt von einer halben Stunde Verspätung, aber es gibt wahrscheinlich schlimmeres. Trotzdem meine Entschuldigung an die Teilnehmer gestern, dass wir nicht wie ausgemacht ab 19:30
image: ''
ogTitle: VFP Stammtisch - Stuttgart/Herrenberg
ogDescription: On the road again...Einmal im Jahr sollte es sein, und auch dieses Mal hat es wieder geklappt. Leider mit einem kleinen Nebeneffekt von einer halben Stunde Verspätung, aber es gibt wahrscheinlich...
layout: post
bodyClass: post-template tag-community
postClass: post tag-community
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
canonicalUrl: https://jochen.kirstaetter.name/vfp-stammtisch-stuttgartherrenberg/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2005-07-15T00:00:00Z
updatedAt: 2018-04-02T08:39:04Z
excerpt: On the road again...Einmal im Jahr sollte es sein, und auch dieses Mal hat es wieder geklappt. Leider mit einem kleinen Nebeneffekt von einer halben Stunde Verspätung, aber es gibt wahrscheinlich...
twitterTitle: VFP Stammtisch - Stuttgart/Herrenberg
twitterDescription: On the road again...Einmal im Jahr sollte es sein, und auch dieses Mal hat es wieder geklappt. Leider mit einem kleinen Nebeneffekt von einer halben Stunde Verspätung, aber es gibt wahrscheinlich...
twitterImage: 
facebookTitle: VFP Stammtisch - Stuttgart/Herrenberg
facebookDescription: On the road again...Einmal im Jahr sollte es sein, und auch dieses Mal hat es wieder geklappt. Leider mit einem kleinen Nebeneffekt von einer halben Stunde Verspätung, aber es gibt wahrscheinlich...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
On the road again...  
  
Einmal im Jahr sollte es sein, und auch dieses Mal hat es wieder geklappt. Leider mit einem kleinen Nebeneffekt von einer halben Stunde Verspätung, aber es gibt wahrscheinlich schlimmeres. Trotzdem meine Entschuldigung an die Teilnehmer gestern, dass wir nicht wie ausgemacht ab 19:30 starten konnten.  
  
17:30, Kaiserslautern - das wöchentliche DVD-Backup unserer Quellcodeverwaltung lässt auf sich warten. Ein Vorgang, der normally in 15 Minuten durch ist, zieht sich auf bereits mehr als 40 Minuten... *grummel*  
  
Nachdem wir - Thomas und meiner Einer - endlich in der Volkshochschule Herrenberg eingetroffen waren, gab Armin noch kurz die aktuellen Infos aus der Community wider und versuchte das ein oder andere Buch unter den Anwesenden 'los' zu bekommen. Es scheint, als habe unsere Idee mit der 'Usergroup-Bibliothek' Schule gemacht. Sehr erfreulich... Ich konnte in dieser Zeit gemütlich den Laptop vorbereiten und die Slides starten.  
  
20:10, Herrenberg - Beamer und Laptop sind einsatzbereit, es kann losgehen. Das Thema des Abends waren 'Additive Datenbank zu Visual FoxPro - MSDE, MS SQL Server, MySQL'. Zuerst gab's einen Überblick, auf welche Fähigkeiten man bei der Wahl eines Datenbankmanagementsystem (DBMS) achten sollte. Im weiteren Verlauf nahmen wir uns den unterschiedlichen Feldtypen - Char, Text, Array, DateTime, etc - an. Fazit dabei ist eigentlich, dass man das ERM möglichst auf einfache Feldtypen reduzieren sollte. Als Beispiel könnte man Datetime in Integer wandeln und mit Sekunden seit Zeitpunkt X arbeiten; siehe Unix-Time mit Sekunden seit 1.1.1970...  
  
20:43, Herrenberg - Beamer genehmigt sich eine Auszeit. Scheint, als ob das Thema zu heiß für die Kiste ist. - Aber... no problem. Ausgerüstet mit Whiteboard und Stift geht's locker weiter. Tsss, Beamer, wer braucht denn schon einen Beamer zur Präsentation?  
Nach zwei, drei Minütchen besinnt sich die Kiste eines Besseren und wir switchen wieder auf Laptop zurück.  
  
Nach so vielen Vorüberlegungen schauen wir uns die Möglichkeiten des Zugriffs von VFP auf die unterschiedlichen Datenquellen an. Und hier sind die ersten 'Hürden' zu beachten, denn schliesslich entfernen wir uns langsam vom einfachen 'Use' in Richtung anderer Möglichkeiten. Hier sei SQL PassThrough (SPT), CursorAdapter oder ADO-Recordset nur erwähnt, aber ihr dürftet sicherlich ein Bild davon bekommen.  
  
20:58, Herrenberg - ein weiterer Schwächeanfall des Beamers ist zu verzeichnen. Inzwischen ist es zwar ein wenig kühler geworden, aber das scheint das Gerätchen schlichtweg nicht zu interessieren. Naja, nicht weiter schlimm, wir wollten gerade über die Eigenheiten einiger ausgewählter DBMS, insbesondere deren Limits, sprechen. Zu VFP gab's wenig zu sagen. - Ansonsten, hatte ich MSDE, MS SQL Server 2000 und 2005, MySQL 4.x, PostgreSQL 7.x bzw. 8.0 notiert. Das dürften potentiell die häufigsten Kandidaten als Ergänzung zu Visual FoxPro darstellen. Achja, das Sessionhandling der Active FoxPro Pages unterstützt diese Server...  
  
21:07, Herrenberg - Totalausfall des Beamer? - Hm, okay, es wäre eh angenehm, wenn wir 'ne kurze Pause einlegen würden. Gesagt, getan.  
  
Abschliessend haben wir noch ein wenig allgemein über ein paar Möglichkeiten aber auch Stolperfallen gesprochen, und schliesslich den Abend mit den Online-Ressourcen  
  
[https://msdn.com/vfoxpro](https://msdn.com/vfoxpro)  
[https://msdn.com/sql](https://msdn.com/sql)  
[https://www.mysql.org](https://www.mysql.org)  
[https://www.postgresql.org](https://www.postgresql.org)  
[https://www.sqlite.org](https://www.sqlite.org)  
[https://www.connectionstrings.com](https://www.connectionstrings.com)  
[https://openacs.org/philosophy/why-not-mysql.html](https://openacs.org/philosophy/why-not-mysql.html)  
  
offiziell beendet. Erfreulicherweise hatten wir die ganze Zeit dezente Musik. Schliesslich ist an diesem Wochenende Sommerfest in Herrenberg.  
  
Dementsprechend haben wir uns abschliessend noch ein wenig ins festliche Treiben begeben. Bei starker Musik, heißen Pizzen und kühlen Getränke hatten wi noch ausreichend Gelegenheit miteinander über diversen Community-Stuff zu sprechen. Es wr wieder einmal richtig toll.  
  
Mein Dank geht hier an alle Teilnehmer von gestern Abend - Danke, es hat wieder einmal Spass gemacht!  
  
01:30, Winnweiler - Endlich schlafen... Gute Nacht.
