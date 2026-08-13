---
uid: unexpected-error-0x8ffe2740-occurred
title: Unexpected error 0x8ffe2740 occurred
slug: unexpected-error-0x8ffe2740-occurred
date: 2005-04-15
status: published
type: post
description: "Unexpected error 0x8ffe2740 occurred Hmhmhm, da hat man noch den Sand in den Augen ereilen mich Norufe per Mobilfunk... Man könnte ja fast sagen: 'Mitten in der Nacht!'Aber soweit möchte ich nundoch nicht gehen...Tjoa, die Betreffzeile dieses Eintrags sagt es ja bereits aus. Nur... was versteckt sich hinter dieser kryptischen"
tags:
- Development
keywords: Development
metaTitle: Unexpected error 0x8ffe2740 occurred
metaDescription: "Unexpected error 0x8ffe2740 occurred Hmhmhm, da hat man noch den Sand in den Augen ereilen mich Norufe per Mobilfunk... Man könnte ja fast sagen: 'Mitten in der Nacht!'Aber soweit möchte ich nundoch nicht gehen...Tjoa, die Betreffzeile dieses Eintrags sagt es ja bereits aus. Nur... was versteckt sich hinter dieser kryptischen"
image: ''
ogTitle: Unexpected error 0x8ffe2740 occurred
ogDescription: 'Hmhmhm, da hat man noch den Sand in den Augen ereilen mich Norufe per Mobilfunk... Man könnte ja fast sagen: "Mitten in der Nacht!"Aber soweit möchte ich nundoch nicht gehen...Tjoa, die Betreffzeile...'
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/unexpected-error-0x8ffe2740-occurred/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2005-04-15T00:00:00Z
updatedAt: 2018-04-02T08:39:04Z
excerpt: 'Hmhmhm, da hat man noch den Sand in den Augen ereilen mich Norufe per Mobilfunk... Man könnte ja fast sagen: "Mitten in der Nacht!"Aber soweit möchte ich nundoch nicht gehen...Tjoa, die Betreffzeile...'
twitterTitle: Unexpected error 0x8ffe2740 occurred
twitterDescription: 'Hmhmhm, da hat man noch den Sand in den Augen ereilen mich Norufe per Mobilfunk... Man könnte ja fast sagen: "Mitten in der Nacht!"Aber soweit möchte ich nundoch nicht gehen...Tjoa, die Betreffzeile...'
twitterImage: 
facebookTitle: Unexpected error 0x8ffe2740 occurred
facebookDescription: 'Hmhmhm, da hat man noch den Sand in den Augen ereilen mich Norufe per Mobilfunk... Man könnte ja fast sagen: "Mitten in der Nacht!"Aber soweit möchte ich nundoch nicht gehen...Tjoa, die Betreffzeile...'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Hmhmhm, da hat man noch den Sand in den Augen ereilen mich Norufe per Mobilfunk... Man könnte ja fast sagen: "Mitten in der Nacht!"  
Aber soweit möchte ich nundoch nicht gehen...  
  
Tjoa, die Betreffzeile dieses Eintrags sagt es ja bereits aus. Nur... was versteckt sich hinter dieser kryptischen Meldung? Ist es ein Zeichen? Was will uns Windows damit sagen? Nun, kurzer Query bei Google und wir finden einen Hauptverdächtigen: Internet Information Services aka IIS  
  
Cool, aber was will uns die Meldung denn nun sagen? - Auch dies ist wiederum extremst simpel, wenn es weiß: Es liegt eine Doppelbelegung eines Ports vor. Im Falle des IIS dürfte es sich dabei in meisten Fällen um den Port 80 (HTTP) handeln. Mit dieser wirklich zu einfachen Ursache werfen wir einen Port-Monitor wie TcpView oder APorts an, isolieren die Anwendung und verändern die Optionen. Und fast unglaublich läuft der IIS wieder...  
  
Okay, aber wieso erzeugt Windows so eine nichts-aussagende kryptische Fehlermeldung anstatt was gescheites auszugeben? - Nun, es wäre zu einfach.  
  
Aber ich vermute, dass so etwas sicherlich auch eine der Ursachen für Communities ist. Daher bin ich mal auf weitere kryptische Meldungen gespannt... denn welche Community-Site liefert mir die Antworten?  
  
  
Bis denne, JoKi  
  
PS: Im benannten Fall war Skype der Übeltäter.
