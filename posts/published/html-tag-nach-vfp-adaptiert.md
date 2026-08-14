---
uid: html-tag-nach-vfp-adaptiert
title: HTML-Tag nach VFP adaptiert
slug: html-tag-nach-vfp-adaptiert
date: 2006-09-19
status: published
type: post
description: HTML-Tag nach VFP adaptiert Ja, es gibt auch Situationen in denen man nicht nur immer von Desktop auf Web trimmt, sondern auch mal den umgekehrten Weg einschl&#228;gt. Der folgende Beitrag nimmt den HTML-Tag **fieldset** als Grundlage und wir erstellen eine Shape-Klasse mit vergleichbarer Funktionalit&#228;t. Das HTML-Element fieldset stellt einen Rahmen
tags:
- Development
keywords: Development
metaTitle: HTML-Tag nach VFP adaptiert
metaDescription: HTML-Tag nach VFP adaptiert Ja, es gibt auch Situationen in denen man nicht nur immer von Desktop auf Web trimmt, sondern auch mal den umgekehrten Weg einschl&#228;gt. Der folgende Beitrag nimmt den HTML-Tag **fieldset** als Grundlage und wir erstellen eine Shape-Klasse mit vergleichbarer Funktionalit&#228;t. Das HTML-Element fieldset stellt einen Rahmen
image: ''
ogTitle: HTML-Tag nach VFP adaptiert
ogDescription: Ja, es gibt auch Situationen in denen man nicht nur immer von Desktop auf Web trimmt, sondern auch mal den umgekehrten Weg einschlägt. Der folgende Beitrag nimmt den HTML-Tag fieldset als Grundlage...
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
canonicalUrl: https://jochen.kirstaetter.name/html-tag-nach-vfp-adaptiert/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-09-19T10:08:58Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Ja, es gibt auch Situationen in denen man nicht nur immer von Desktop auf Web trimmt, sondern auch mal den umgekehrten Weg einschlägt. Der folgende Beitrag nimmt den HTML-Tag fieldset als Grundlage...
twitterTitle: HTML-Tag nach VFP adaptiert
twitterDescription: Ja, es gibt auch Situationen in denen man nicht nur immer von Desktop auf Web trimmt, sondern auch mal den umgekehrten Weg einschlägt. Der folgende Beitrag nimmt den HTML-Tag fieldset als Grundlage...
twitterImage: 
facebookTitle: HTML-Tag nach VFP adaptiert
facebookDescription: Ja, es gibt auch Situationen in denen man nicht nur immer von Desktop auf Web trimmt, sondern auch mal den umgekehrten Weg einschlägt. Der folgende Beitrag nimmt den HTML-Tag fieldset als Grundlage...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Ja, es gibt auch Situationen in denen man nicht nur immer von Desktop auf Web trimmt, sondern auch mal den umgekehrten Weg einschlägt. Der folgende Beitrag nimmt den HTML-Tag **fieldset** als Grundlage und wir erstellen eine Shape-Klasse mit vergleichbarer Funktionalität. Das HTML-Element fieldset stellt einen Rahmen mit optionaler Überschrift dar. Mit den Controls Shape und Label (optional noch Container) können wir das ebenfalls in VFP realisieren. Hier zunächst mal der HTML-Code für ein fieldset:

```
<fieldset id="Restore">
<legend>Datenbank wiederherstellen</legend>
<p>...</p>
</fieldset>
```

Das Element **legend** ist für die Beschriftung verantwortlich und repräsentiert unsere Labelklasse.

## Shape - die spartanische Variante

Der erste Lösungsansatz ist sehr einfach gehalten: Wir erzeugen uns eine Shape-Klasse, die eigenständig ein zugehöriges Label instanziiert und positioniert:

```foxpro
*======================================================================
* Fieldset-Shape
* Erzeugt bei der Initialisierung ein Label zur Beschriftung des Shapes
* und positioniert es.
*======================================================================
Define Class FieldSet As Shape
  cCaption = ""
  cPrefixLabel = "lbl"
  nOffsetTop = -7
  nOffsetLeft = 5
  lUseLabel = .T.  && Readonly @ Runtime ;-)
  MemberClass = ""
  MemberClassLibrary = ""
  Protected oLegend
  oLegend = .Null.

  *------------------------------------------------------------------
  * Initialisierung und (optionale) Erstellung der Beschriftung.
  *------------------------------------------------------------------
  Function Init() As Boolean
    DoDefault()
    If This.lUseLabel
      This.createLabel()
    EndIf
  EndFunc

  *------------------------------------------------------------------
  * Label instanziieren und positionieren.
  *------------------------------------------------------------------
  Protected Function createLabel() As VOID
  With This
    If Vartype(.cCaption) == "C"
      .oLegend = NewObject(Evl(.MemberClass, "Label"), .MemberClassLibrary)
      If Vartype(.oLegend) == "O"
        With .oLegend As Label
          .Name = This.cPrefixLabel + This.Name
          .BackColor = Thisform.BackColor
          .BackStyle = 1
          .Anchor = 0
          .Left = This.Left + This.nOffsetLeft
          .Top = This.Top + This.nOffsetTop
          .Anchor = Bitclear(Bitclear(This.Anchor, 2), 3)
          .ZOrder(0)
        EndWith
        This.cCaption = This.cCaption
      EndIf
    EndIf
  EndWith
EndFunc

*------------------------------------------------------------------
* Nachträgliche Änderungen der Caption gestatten.
* Dies ermöglicht auch das Aus-/Einblenden des Controls.
*------------------------------------------------------------------
Function cCaption_Assign(tcValue As String)
  With This
    If Vartype(.oLegend) == "O"
      .oLegend.Caption = m.tcValue
      .oLegend.Visible = Not Empty(m.tcValue)
    EndIf
    .cCaption = m.tcValue
  EndWith
EndFunc

*------------------------------------------------------------------
* Schreibschutz für This.lUseLabel implementieren.
*------------------------------------------------------------------
Function lUseLabel_Assign(tlValue As Boolean)
  Error 1740, "lUseLabel"
EndFunc

*------------------------------------------------------------------
* Objektreferenz sauber auflösen und Label entsorgen.
*------------------------------------------------------------------
Function Destroy() As Boolean
  With This
    If Vartype(.oLegend) == "O"
      .oLegend = .Null.
    EndIf
  EndWith
EndFunc
EndDefine
```

Der gezeigte VFP-Quellcode dürfte weitestgehend selbsterklärend sein. Wenn in der Designzeit dem Shape die Caption gestattet wird, so wird zur Laufzeit ein Labelobjekt aus der angegebenen Klasse erzeugt und als Referenz gespeichert.

Das Label erhält den gleichen Namen wie das Shape jedoch mit frei wählbarem Prefix, da wir eindeutige Objektnamen benötigen. Sofern bei der Initialisierung noch keine Beschriftung angegeben sein sollte, wird das Label noch nicht angezeigt. Die Caption kann zu jedem beliebigen späteren Zeitpunkt gesetzt (und damit eingeblendet) und wieder ausgeblendet werden.

Zur Vermeidung von hängenden Referenzen und daraus resultierenden C0005-Fehlern (samt Komplettabsturz) tragen wir dafür Sorge, dass das Label ebenfalls sauber bei der Zerstörung des Shapes entfernt wird.

Wichtig ist hierbei ebenfalls, dass wir die Eigenschaft lUseLabel zur Laufzeit mit einem Schreibschutz versehen. Schliesslich soll der Entwickler sich bereits in der Entwicklungsumgebung entscheiden, ob eine Beschriftung erforderlich sein könnte oder nicht.

Bis denne, JoKi

PS: Die fehlenden Assign-Methoden für weitere Eigenschaften sind Hausaufgabe... 😁