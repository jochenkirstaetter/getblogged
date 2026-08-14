---
uid: kommentar-zu-parameterobjekte
title: Kommentar zu 'Parameterobjekte'
slug: kommentar-zu-parameterobjekte
date: 2006-08-25
status: published
type: post
description: "Kommentar zu 'Parameterobjekte' Grundlage für diesen Beitrag liefert der Blogeintrag von Olaf Doschke: [url=http://blog.dfpug.de/?dnr=2212&amp;id=48]Parameterobjekte[/url] vom 10.06.2006 hier der vollständige Kommentar zu seinem Artikel und meiner 'Weltansicht' zu diesem Sachverhalt: Hallo Olaf, ich finde, dass es ein guter Artikel ist.Wir nutzen das Konzept von Parameter-/Transferobjekten bereits seit Jahren. Dein Ansatz mit"
tags:
- Development
keywords: Development
metaTitle: Kommentar zu 'Parameterobjekte'
metaDescription: "Kommentar zu 'Parameterobjekte' Grundlage für diesen Beitrag liefert der Blogeintrag von Olaf Doschke: [url=http://blog.dfpug.de/?dnr=2212&amp;id=48]Parameterobjekte[/url] vom 10.06.2006 hier der vollständige Kommentar zu seinem Artikel und meiner 'Weltansicht' zu diesem Sachverhalt: Hallo Olaf, ich finde, dass es ein guter Artikel ist.Wir nutzen das Konzept von Parameter-/Transferobjekten bereits seit Jahren. Dein Ansatz mit"
image: ''
ogTitle: Kommentar zu 'Parameterobjekte'
ogDescription: 'Grundlage für diesen Beitrag liefert der Blogeintrag von Olaf Doschke:'
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
canonicalUrl: https://jochen.kirstaetter.name/kommentar-zu-parameterobjekte/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-08-25T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: 'Grundlage für diesen Beitrag liefert der Blogeintrag von Olaf Doschke:'
twitterTitle: Kommentar zu 'Parameterobjekte'
twitterDescription: 'Grundlage für diesen Beitrag liefert der Blogeintrag von Olaf Doschke:'
twitterImage: 
facebookTitle: Kommentar zu 'Parameterobjekte'
facebookDescription: 'Grundlage für diesen Beitrag liefert der Blogeintrag von Olaf Doschke:'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Grundlage für diesen Beitrag liefert der Blogeintrag von Olaf Doschke:

[Parameterobjekte](http://blog.dfpug.de/?dnr=2212&id=48) vom 10.06.2006

hier der vollständige Kommentar zu seinem Artikel und meiner 'Weltansicht' zu diesem Sachverhalt:

Hallo Olaf,

ich finde, dass es ein guter Artikel ist.  
Wir nutzen das Konzept von Parameter-/Transferobjekten bereits seit Jahren. Dein Ansatz mit den semikolon-separierten Werten (SSV) finde ich soweit auch gut. Bleibt nur die folgende Frage: Wieso Semikolon und nicht Kommata?

Eine weitere Frage, oder besser gesagt ein konzeptioneller Gedankengang, geht dahin, dass ich mich frage, wieso der Aufbau der Klasse in den Aufruf der Funktion per Parameter zu erfolgen hat. Der Hintergrund dabei ist, dass man innerhalb eines Projektes eigentlich eine definierte Anzahl von Transferobjekten besitzt, welche auch eine konstante Schnittstelle besitzen sollten. Mein Problem mit deiner Objektdeklaration beim Aufruf geht in die Richtung der Wartbarkeit des Codes. Vom Ansatz her hätte ich das Interface der Funktion in etwa so aufgebaut:

```
Function CreateParameterObject(tcToken As String, tcProperties As String, tcTypes As String, tcValues As String) As Object
```

Über die Namensgebung brauchen nicht zu sprechen... Bei mir würde die Funktion 'GetParameter()' lauten. Die Idee für den Token zielt dahin, dass ich nun innerhalb der Case-Anweisungen ebenfalls eine Art Factory Design Pattern nutzen kann, welches Zugriff auf fertigdefinierte Klassendefinitionen ermöglicht. Diese könnten etwa in einer MetaTabelle(cToken, cProperties, cTypes, cValues) hinterlegt sein. Damit verbessert sich meiner Ansicht nach die Lesbarkeit und vereinfacht sich die Codepflege. Durch die Verwendung von Konstanten kann sich der Informationsgehalt weiter erhöhen. Hier mal ein wenig Beispielcode:

```
Local loPosition
m.loPosition = CreateParameterObject("Position")
m.loPosition.Left = 100
m.loPosition.Top = 120
```

Die weiteren Konstellationen sind identisch mit deinem aktuellen Entwurf, sofern der erste Parameter leer bleibt. Also, etwa so:

```
lo = CreateParameterObject("","iX;iY","I;I","20;100")
? lo.iX, lo.iY
```

Eine Kombination wäre sicherlich auch denkbar:

```
#Define PARAMETER_POSITION  "Position"
lo = CreateParameterObject(PARAMETER_POSITION,"","","20;100")
? lo.iX, lo.iY
```

In diesem Fall stammen die Informationen zu Eigenschaften und deren Typ aus der Tokenbeschreibung.

Hm, was mir noch aufgefallen ist... Was spricht gegen den Fall 'Pcount() == 0'? In dieser Situation verweigert deine gezeigte Implementierung die Rückgabe eines Empty-Objekts, dass übrigens bereits erzeugt wurde...  
So, jetzt bin ich doch bei der genaueren Betrachtung deines Codes und ziemlich neugierig, ob deiner Entscheidungsgrundlagen. Es ist nämlich sehr interessant darüber zu philosophieren. In deiner Routine nutzt du drei Arrays zur Abbildung der drei Stringparameter in Kombination mit dem Alines()-Statements. Die Möglichkeit zur Definition des Delimiters in Alines() ist wirklich sehr praktisch. Dennoch würde ich in diesem Fall auf die Konvertierung von String nach Array verzichten und direkt mit den vorhandenen VFP-Funktionen GetWordCount() und GetWordNum() arbeiten:

```
For lnIndex = 1 To GetWordCount(tcProperties, ";")
    AddProperty(loObject, GetWordNum(tcProperties, lnIndex, ";"))
EndFor
```

Es ist reine Neugier, wieso du mit Arrays arbeitest. Interessiert mich wirklich sehr. Ich denke, dass ich mal beide Varianten auf Performance (Anzahl der Durchläufe in konstanter Zeitspanne) prüfen werde.  
Bis denne, JoKi
