---
uid: rss-validation
title: RSS Validation
date: 2005-07-10
status: published
type: post
description: RSS Validation Endlich mal wieder ein wenig Zeit f&#252;r die Entwicklung meines HTML Plugin f&#252;r Active FoxPro Pages...Als Quintessenz dessen konnte ich ein paar Korrekturen an der CursorToRss() Methode realisieren, die es erm&#246;glicht direkt aus einer Tabelle einen g&#252;ltigen RSS 2.0 Feed zu erzeugen.Zur Kontrolle habe ich mir einen Onlinevalidator
tags:
- Development
keywords: Development
metaTitle: RSS Validation
metaDescription: RSS Validation Endlich mal wieder ein wenig Zeit f&#252;r die Entwicklung meines HTML Plugin f&#252;r Active FoxPro Pages...Als Quintessenz dessen konnte ich ein paar Korrekturen an der CursorToRss() Methode realisieren, die es erm&#246;glicht direkt aus einer Tabelle einen g&#252;ltigen RSS 2.0 Feed zu erzeugen.Zur Kontrolle habe ich mir einen Onlinevalidator
image: ''
ogTitle: RSS Validation
ogDescription: Endlich mal wieder ein wenig Zeit für die Entwicklung meines HTML Plugin für Active FoxPro Pages...Als Quintessenz dessen konnte ich ein paar Korrekturen an der CursorToRss() Methode realisieren, die...
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
canonicalUrl: https://jochen.kirstaetter.name/rss-validation/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2005-07-10T22:00:00Z
updatedAt: 2018-04-02T08:38:31Z
excerpt: Endlich mal wieder ein wenig Zeit für die Entwicklung meines HTML Plugin für Active FoxPro Pages...Als Quintessenz dessen konnte ich ein paar Korrekturen an der CursorToRss() Methode realisieren, die...
twitterTitle: RSS Validation
twitterDescription: Endlich mal wieder ein wenig Zeit für die Entwicklung meines HTML Plugin für Active FoxPro Pages...Als Quintessenz dessen konnte ich ein paar Korrekturen an der CursorToRss() Methode realisieren, die...
twitterImage: 
facebookTitle: RSS Validation
facebookDescription: Endlich mal wieder ein wenig Zeit für die Entwicklung meines HTML Plugin für Active FoxPro Pages...Als Quintessenz dessen konnte ich ein paar Korrekturen an der CursorToRss() Methode realisieren, die...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Endlich mal wieder ein wenig Zeit für die Entwicklung meines HTML Plugin für Active FoxPro Pages...  
  
Als Quintessenz dessen konnte ich ein paar Korrekturen an der CursorToRss() Methode realisieren, die es ermöglicht direkt aus einer Tabelle einen gültigen RSS 2.0 Feed zu erzeugen.  
  
Zur Kontrolle habe ich mir einen Onlinevalidator herangezogen, und das Ergebnis ist inzwischen zufriedenstellend:  
  
[https://www.feedvalidator.org/check.cgi?url=http%3A%2F%2Fwww.afpwi](https://www.feedvalidator.org/check.cgi?url=http%3A%2F%2Fwww.afpwi)  
ki.de%2Fafpwiki.afp  
  
Damit können nun auch Nutzer des AfpWiki von diesen Anpassungen ihre Vorteile ziehen. Also, Subversion-Client anwerfen und aktuelle Version ziehen.