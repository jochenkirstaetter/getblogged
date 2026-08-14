---
uid: die-checkbox-und-ihr-enter-return-verhalten
title: Die Checkbox und ihr Enter/Return-Verhalten
slug: die-checkbox-und-ihr-enter-return-verhalten
date: 2006-08-17
status: published
type: post
description: Die Checkbox und ihr Enter/Return-Verhalten **Das Problem**Heute mal wieder etwas aus der Programmierküche mit dem Fuchs. Ausgehend von einer Anforderung in einem laufenden Projekt sollte es ermöglicht werden, dass man innerhalb eines VFP Grids sowohl mit der Tab-Taste wie auch der Enter-Taste durch die Zellen navigieren kann. Nun, soweit stellt
tags:
- Development
keywords: Development
metaTitle: Die Checkbox und ihr Enter/Return-Verhalten
metaDescription: Die Checkbox und ihr Enter/Return-Verhalten **Das Problem**Heute mal wieder etwas aus der Programmierküche mit dem Fuchs. Ausgehend von einer Anforderung in einem laufenden Projekt sollte es ermöglicht werden, dass man innerhalb eines VFP Grids sowohl mit der Tab-Taste wie auch der Enter-Taste durch die Zellen navigieren kann. Nun, soweit stellt
image: ''
ogTitle: Die Checkbox und ihr Enter/Return-Verhalten
ogDescription: Heute mal wieder etwas aus der Programmierküche mit dem Fuchs. Ausgehend von einer Anforderung in einem laufenden Projekt sollte es ermöglicht werden, dass man innerhalb eines VFP Grids sowohl mit der...
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
canonicalUrl: https://jochen.kirstaetter.name/die-checkbox-und-ihr-enter-return-verhalten/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-08-17T01:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: Heute mal wieder etwas aus der Programmierküche mit dem Fuchs. Ausgehend von einer Anforderung in einem laufenden Projekt sollte es ermöglicht werden, dass man innerhalb eines VFP Grids sowohl mit der...
twitterTitle: Die Checkbox und ihr Enter/Return-Verhalten
twitterDescription: Heute mal wieder etwas aus der Programmierküche mit dem Fuchs. Ausgehend von einer Anforderung in einem laufenden Projekt sollte es ermöglicht werden, dass man innerhalb eines VFP Grids sowohl mit der...
twitterImage: 
facebookTitle: Die Checkbox und ihr Enter/Return-Verhalten
facebookDescription: Heute mal wieder etwas aus der Programmierküche mit dem Fuchs. Ausgehend von einer Anforderung in einem laufenden Projekt sollte es ermöglicht werden, dass man innerhalb eines VFP Grids sowohl mit der...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
## Das Problem

Heute mal wieder etwas aus der Programmierküche mit dem Fuchs. Ausgehend von einer Anforderung in einem laufenden Projekt sollte es ermöglicht werden, dass man innerhalb eines VFP Grids sowohl mit der Tab-Taste wie auch der Enter-Taste durch die Zellen navigieren kann. Nun, soweit stellt dies eigentlich kein Problem dar.

Interessant wird es erst im Zusammenspiel mit anderen Klassen als Control der Spalte. Etwa der Checkbox. Das normale Verhalten der Checkbox bei Tasteneingaben in Visual FoxPro sieht kurz gesagt so aus:

- Space - Änderung des Zustands
- Tab - Wechsel zum nächsten Control **ohne** Statusänderung
- Enter/Return - Wechsel zum nächsten Control **mit** Änderung des Zustands

Nun gut, damit kann man leben und das Verhalten erscheint auf den ersten Blick intuitiv. Nur... wir wollen innerhalb des Grid nur Navigieren und nicht den Zustand der Checkbox verändern.

## Die erste Idee

Jedem Fuchs wird auf Anhieb einfallen, dass die Lösung des Problems in der Überlagerung der Checkbox.KeyPress() Ereignismethode zu realisieren. Das ist auch vollkommen korrekt und okay. Mein erster Ansatz ergab sich aus einer kurzen Recherche samt Bestätigung im FoxWiki. Der Quellcode sah im ersten Ansatz so aus:

```foxpro
*====================================================================
* Erweiterung: Die Return/Enter-Taste soll keine Funktion besitzen.
* Das Problem ist, dass primär mit der Enter- neben der
* Tab-Taste in den Formularen und Grids navigiert wird.
*====================================================================
LPARAMETERS nKeyCode, nShiftAltCtrl

If (m.nKeyCode == 13 .And. InList(m.nShiftAltCtrl, 0, 1)) .Or. ;
    (m.nKeyCode == 10 .And. m.nShiftAltCtrl == 2)

  Keyboard '{TAB}'
  NoDefault
  Return
EndIf

DoDefault()
```

Wir verändern das Verhalten der Checkbox soweit, dass die Enter/Return-Taste ihre Funktionalität verliert und der Wechsel durch das Auslösen der Tab-Taste wiederhergestellt wird. Ein kurzer Test mit der erweiterten Klasse auf einem Formular funktioniert soweit tadellos. Fein...

## Das Extra - VFP Grid

Frohen Mutes wird diese Klasse nun als CurrentControl in eine Gridspalte eingebaut und getestet. Das Ergebnis ist katastrophal! Neben der Tatsache, dass der Zustand der Checkbox geändert wird, wechseln wir nicht nur in die nächste Spalte, nein, sondern in die übernächste. Na ganz toll...

Nun, was ändert sich den wirklich? Beim Steppen im Debugger ergibt sich, dass das Checkbox.Value nicht verändert wird. Soweit entspricht dies der Verwendung auf einem Formular oder innerhalb eines Containers. Aber... wir haben eine ControlSource und anscheinend verhält sich VFP in der Art, dass zwar der Wert der Checkbox unverändert bleibt, aber trotzdem die ControlSource geändert wird und aus der Aktualisierung heraus, wechselt dann die Checkbox doch ihren Wert. Interessanterweise passiert dies nicht, wenn die Checkbox mit eigener ControlSource genutzt wird.

Da ich keine Möglichkeit gefunden habe, die Wertänderung in der Column.ControlSource zu verhindern, nutze ich die 'Technik der doppelten Negation' 😎 um zum gewünschten Ergebnis zu kommen. Innerhalb des KeyPress prüfe ich auf die Existenz des Parent von der Basisklasse 'Column' und verändere den aktuellen Wert der Checkbox. Da VFP ebenfalls eine Invertierung des Value durchführt, enden wir wieder beim ursprünglichen Zustand.

Außerdem vermeiden wir das 'Drücken' der Tab-Taste, da wir ja in die nächste Spalte wechseln wollen...

## Die Lösung

Und zusammengetippt sieht die KeyPress-Methode inzwischen folgendermaßen aus:

```foxpro
*====================================================================
* Erweiterung: Die Return/Enter-Taste soll keine Funktion besitzen.
* Das Problem ist, dass primär mit der Enter- neben der
* Tab-Taste in den Formularen und Grids navigiert wird.
*====================================================================
LPARAMETERS nKeyCode, nShiftAltCtrl

With This
  Local llColumn, lcControlSource, lcVartype, luValue
  m.llColumn = .F.
  m.lcControlSource = ""
  m.lcVartype = ""
  m.luValue = 0

  If .lSkipEnter .And. ( ;
      (m.nKeyCode == 13 .And. InList(m.nShiftAltCtrl, 0, 1)) .Or. ;
      (m.nKeyCode == 10 .And. m.nShiftAltCtrl == 2) ;
      )

    m.llColumn = (Vartype(This.Parent) == T_OBJECT .And. ;
      Lower(This.Parent.BaseClass) == "column")

    *--- Falls die Checkbox ein Child einer Column ist,
    *--- müssen wir uns um die ControlSource kümmern.
    If m.llColumn
      m.lcControlSource = This.Parent.ControlSource
      m.luValue = Evaluate(m.lcControlSource)
      m.lcVartype = Vartype(m.luValue)

      .Value = ICase( ;
        m.lcVartype == T_LOGICAL, Not m.luValue, ;
        1 - m.luValue ;
        )
    Else
      *---&nbsp;Ansonsten brauchen wir den zusätzlichen TAB
      *---&nbsp;nicht auszulösen.
      Keyboard '{TAB}'
    EndIf

    NoDefault
    Return
  EndIf
EndWith

DoDefault()
```

Der Code ist in der ersten Ableitung implementiert und durch das Setzen der Checkbox.lSkipEnter kann sowohl in Ableitungen wie auch Instanzen der Checkbox das Verhalten reguliert werden.

Interessant ist wie der Fuchs wieder die ganze Sache handhabt, aber okay... es ist nachvollziehbar.

Welche Tricks und Erfahrungen habt ihr mit der Checkbox bisher gemacht?

Bis denne, JoKi