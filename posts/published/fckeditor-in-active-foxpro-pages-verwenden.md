---
uid: fckeditor-in-active-foxpro-pages-verwenden
title: FCKeditor in Active FoxPro Pages verwenden
slug: fckeditor-in-active-foxpro-pages-verwenden
date: 2006-04-11
status: published
type: post
description: FCKeditor in Active FoxPro Pages verwenden **Download und AFP Beispiele**Dank der Bereitstellung der Klassendefinition und Beispiele von S&#246;nke Freitag ist die Integration des FCKeditor in Active FoxPro Pages eines wahres Heimspiel. Das Beispiel selbst ist als AFP Applikation (*.afpa) aufgesetzt und zeigt wie man in einem Dokument den FCKeditor integriert
tags:
- Development
keywords: Development
metaTitle: FCKeditor in Active FoxPro Pages verwenden
metaDescription: FCKeditor in Active FoxPro Pages verwenden **Download und AFP Beispiele**Dank der Bereitstellung der Klassendefinition und Beispiele von S&#246;nke Freitag ist die Integration des FCKeditor in Active FoxPro Pages eines wahres Heimspiel. Das Beispiel selbst ist als AFP Applikation (*.afpa) aufgesetzt und zeigt wie man in einem Dokument den FCKeditor integriert
image: ''
ogTitle: FCKeditor in Active FoxPro Pages verwenden
ogDescription: '**Download und AFP Beispiele**Dank der Bereitstellung der Klassendefinition und Beispiele von Sönke Freitag ist die Integration des FCKeditor in Active FoxPro Pages eines wahres Heimspiel. Das...'
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
canonicalUrl: https://jochen.kirstaetter.name/fckeditor-in-active-foxpro-pages-verwenden/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-11T10:57:28Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: '**Download und AFP Beispiele**Dank der Bereitstellung der Klassendefinition und Beispiele von Sönke Freitag ist die Integration des FCKeditor in Active FoxPro Pages eines wahres Heimspiel. Das...'
twitterTitle: FCKeditor in Active FoxPro Pages verwenden
twitterDescription: '**Download und AFP Beispiele**Dank der Bereitstellung der Klassendefinition und Beispiele von Sönke Freitag ist die Integration des FCKeditor in Active FoxPro Pages eines wahres Heimspiel. Das...'
twitterImage: 
facebookTitle: FCKeditor in Active FoxPro Pages verwenden
facebookDescription: '**Download und AFP Beispiele**Dank der Bereitstellung der Klassendefinition und Beispiele von Sönke Freitag ist die Integration des FCKeditor in Active FoxPro Pages eines wahres Heimspiel. Das...'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
## Download und AFP Beispiele
Dank der Bereitstellung der Klassendefinition und Beispiele von Sönke Freitag ist die Integration des [FCKeditor](https://www.fckeditor.net/) in Active FoxPro Pages eines wahres Heimspiel. Das Beispiel selbst ist als AFP Applikation (\*.afpa) aufgesetzt und zeigt wie man in einem Dokument den FCKeditor integriert und anwendet, während im zweiten Beispiel die Verarbeitung des erstellten Text in einer Übersicht gelistet wird. Absolut ausreichend für den ersten Einstieg in die Materie.  
Es war lediglich eine kleine Anpassung durchzuführen: Die Pfadkorrektur auf den Basispfad für die eigentliche Funktionalität des FCKeditors. Ich führe dies jedoch auf meine atypische Speicherung des Archivs zurück.

## Was nun?
Motiviert durch diesen positiven ersten Eindruck habe ich mir ein bisschen den Quellcode angesehen und siehe da - eine Klassendefinition und einen kleineren Codeblock - und fertig. Nun, mangelnde Beispiele habe ich sicherlich keine und mein 'erstes Opfer' ist in den meisten Fällen das AfpWiki. Der aktuelle Editor kann sicherlich ein Face-Lifting gebrauchen, also wieso nicht FCKeditor. ;-)

## Integration in AfpWiki
Gedacht, getan... Hm, es sind noch kleinere Anpassungen am Beispielcode von Sönke durchzuführen, damit es wirklich reibungslos klappt. Keine Sorge, ich werde die Patches direkt an ihn per Mail schicken. In der Hoffnung, dass mit dem nächsten Release des Editors auch die veränderten AFP-Dokumente dabei sind. Meine erste Empfehlung ist, dass man die VFP Klassendefinition in eine eigene Prozedurendatei umsiedelt und diese neue Datei wiederum per INCLUDE-Statement in die eigene, bestehende AFP Anwendung integriert:  
`\*!<[INCLUDE: "fck.code"]>`  
Ich verwende hier exemplarisch die Endung .code, da es in der AFP so üblich für Prozedurendateien ist. Es spricht aber auch überhaupt nichts dagegen, dass man die VFP übliche Endung .prg verwendet. Das ist lediglich eine persönliche Geschmackssache, der AFP ist es gleichgültig.

Nach der Integration der Klassendefinition werden die beiden Beispieldokumente (\*.afp) ins AfpWiki assimiliert:  

```foxpro
<%
sBasePath="./FckEditor/" && Change this to your local path

lcText=[This is some <strong>sample text</strong>. You are using ]
lcText=lcText+[<a href='https://www.fckeditor.net/'>FCKeditor</a>.]

oFCKeditor = CREATEOBJECT("FCKeditor")
oFCKeditor.fckeditor("FCKeditor1")
oFCKeditor.BasePath = sBasePath
oFCKeditor.cValue = lcText

Response.Write( oFCKeditor.Create() )
%>
```
  
Nach einer anfänglichen Wehr - wer kommt auch auf die Idee, Variablennamen gleich Feldnamen des aktiven Alias zu setzen, und diesen auch noch 'html' zu nennen? - präsentierte sich der FCKeditor im gewohnten Bild im Layout des AfpWiki. Soviel zum Thema AFP debuggen und Master Pages ;-)

## Optisches Finetuning
Die weiteren Schritte umfassen nun lediglich noch das Customizing und Skinning für die Optik des AfpWiki, welche aber individuell jede/r selbst abstimmen kann. Weiterhin werde ich in der applikationsweiten Konfiguration *afpwiki.afpa* noch ein paar Kontroloptionen für die Bearbeitung von Topics im Allgemeinen und dann editorspezifisch im Detail einrichten. Schliesslich habe ich nur wenig Interesse, dass beim Upgrade des FCKeditors mein eigener Code entsorgt werden würde.

## Fazit
Zusammenfassend lässt sich sagen, dass die mitgelieferten AFP-Beispiele des FCKeditors mit einer eventuellen Anpassung des Basispfades direkt funktionieren und die Integration in eigene AFP-Anwendungen wirklich nur eine Sache von Minuten ist.

Viel Spass bei der Verwendung des FCKeditors und bis denne, JoKi