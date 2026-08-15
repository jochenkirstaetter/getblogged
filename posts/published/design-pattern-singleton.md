---
uid: design-pattern-singleton
title: 'Design Pattern: Singleton'
slug: design-pattern-singleton
date: 2006-04-04
status: published
type: post
description: "Design Pattern: Singleton Als Konsequenz der Anwendung im Beitrag <a href='/ScriptingFileSystemObject'>Scripting.FileSystemObject</a> stelle ich euch hier die Theorie des Design Pattern Singleton (deutsch: Einzelstück) und meine interpretierte Implementierung vor. In Wikipedia ist die Definition wie folgt beschrieben:Das Einzelstück (engl. Singleton) ist ein in der Softwareentwicklung eingesetztes Entwurfsmuster und gehört zur Kategorie der"
tags:
- Development
keywords: Development
metaTitle: 'Design Pattern: Singleton'
metaDescription: "Design Pattern: Singleton Als Konsequenz der Anwendung im Beitrag <a href='/ScriptingFileSystemObject'>Scripting.FileSystemObject</a> stelle ich euch hier die Theorie des Design Pattern Singleton (deutsch: Einzelstück) und meine interpretierte Implementierung vor. In Wikipedia ist die Definition wie folgt beschrieben:Das Einzelstück (engl. Singleton) ist ein in der Softwareentwicklung eingesetztes Entwurfsmuster und gehört zur Kategorie der"
image: ''
ogTitle: 'Design Pattern: Singleton'
ogDescription: 'Als Konsequenz der Anwendung im Beitrag Scripting.FileSystemObject stelle ich euch hier die Theorie des Design Pattern Singleton (deutsch: Einzelstück) und meine interpretierte Implementierung vor. In...'
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
canonicalUrl: https://jochen.kirstaetter.name/design-pattern-singleton/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-04T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: 'Als Konsequenz der Anwendung im Beitrag Scripting.FileSystemObject stelle ich euch hier die Theorie des Design Pattern Singleton (deutsch: Einzelstück) und meine interpretierte Implementierung vor. In...'
twitterTitle: 'Design Pattern: Singleton'
twitterDescription: 'Als Konsequenz der Anwendung im Beitrag Scripting.FileSystemObject stelle ich euch hier die Theorie des Design Pattern Singleton (deutsch: Einzelstück) und meine interpretierte Implementierung vor. In...'
twitterImage: 
facebookTitle: 'Design Pattern: Singleton'
facebookDescription: 'Als Konsequenz der Anwendung im Beitrag Scripting.FileSystemObject stelle ich euch hier die Theorie des Design Pattern Singleton (deutsch: Einzelstück) und meine interpretierte Implementierung vor. In...'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Als Konsequenz der Anwendung im Beitrag [Scripting.FileSystemObject](xref:design-pattern-singleton) stelle ich euch hier die Theorie des Design Pattern Singleton (deutsch: Einzelstück) und meine interpretierte Implementierung vor. In [Wikipedia ist die Definition](https://de.wikipedia.org/wiki/Einzelst%C3%BCck_%28Entwurfsmuster%29) wie folgt beschrieben:

*Das Einzelstück (engl. Singleton) ist ein in der Softwareentwicklung eingesetztes Entwurfsmuster und gehört zur Kategorie der Erzeugungsmuster (engl. Creational Patterns). Es stellt sicher, dass zu einer Klasse nur genau ein Objekt erzeugt werden kann und ermöglicht einen globalen Zugriff auf dieses Objekt.  
[...]  
Das Einzelstück findet Verwendung, wenn  
* nur ein Objekt zu einer Klasse existieren darf und ein einfacher Zugriff auf dieses Objekt benötigt wird oder  
* wenn das einzige Objekt durch Unterklassenbildung spezialisiert werden soll.  
Anwendungsbeispiele sind:  
* Ein zentrales Protokoll-Objekt, das Ausgaben in eine Datei schreibt.  
* Druckaufträge, die zu einem Drucker gesendet werden, sollten nur in einen einzigen Puffer geschrieben werden.*

Wichtig finde ich hier, dass der Singleton die Sicherstellung der einmaligen Objekterzeugung von anderen Klassen verwaltet. Es heißt nicht zwangsläufig, dass der Singleton nur einmalig instanziiert werden kann. Wobei das natürlich das Optimum darstellen würde. Soviel zur Theorie, schauen wir uns das Pattern mal in der rauen VFP-Praxis an. Vor allem auch die Frage wo wir sowas etwas überhaupt gebrauchen könnten...

Im Beitrag [Scripting.FileSystemObject](xref:design-pattern-singleton) bin ich leicht auf das Thema Applicationservices eingegangen (nicht im Zusammenhang mit SOA), und habe für den einfachen Zugriff einen zentralen Anlaufpunkt in meiner Anwendung erzeugt, welcher mir Objektreferenzen liefert. Wichtig ist hierbei, dass der Dienst im Normalfall nur ein einziges Mal in der Anwendung existiert und dass ich mich nicht um die Erstellung des Dienstes kümmern muss. Und genau für diesen Einsatzzweck coden wir nun unser Singleton live und in Farbe...

Als Basisklasse zur Verwaltung der Objekte verwenden wir eine Collection und spendieren dieser noch ein paar Funktionen:  

```foxpro
*====================================================================
* Beispielimplementierung für Singleton Design Pattern
*====================================================================
Define Class AbstractSingleton As Collection
  *------------------------------------------------------------------
  * Liefert Objektreferenz zum spezifizierten Token
  * Falls das Objekt noch nicht vorliegt, wird es erzeugt
  * und der Collection hinzugefügt.
  *------------------------------------------------------------------
  Function GetReference(tcToken As String) As Object
    Local loReturn
    m.loReturn = .Null.

    *------------------------------------------------------------------
    * Assertions und defensive Programmierung...
    *------------------------------------------------------------------
    Assert Vartype(m.tcToken) == T_CHARACTER && "C"

    With This
      If .Exist(m.tcToken)
        m.loReturn = .Item(m.tcToken)
      Else
        m.loReturn = .createInstance(m.tcToken)
        If Vartype(m.loReturn) == T_OBJECT
          .Add(m.loReturn, Transform(m.tcToken))
        EndIf
      EndIf
    EndWith

    Return m.loReturn
  EndFunc

  *------------------------------------------------------------------
  * Diese Methode erzeugt das eigentliche Objekt,
  * welches der Singleton als Referenz zurück gibt.
  *------------------------------------------------------------------
  Protected Function createInstance(tcToken As String) As Object
  Return .Null.
EndFunc
EndDefine

*====================================================================
* Konkretisierte Ableitung für Dienste.
*====================================================================
Define Class ServiceSingleton As AbstractSingleton
  Protected Function createInstance(tcToken As String) As Object
  Local loReturn, loException, lcClass, lcLibrary
  m.loReturn = .Null.
  m.lcClass = ""
  m.lcLibrary = ""

  Try
    *--- Hier kann man beliebigen Code zur Übersetzung
    *--- des Token auf Class und ClassLibrary implementieren
    *--- Beliebte Varianten sind:
    *--- Do Case
    *--- Lookup auf Tabelle
    *--- Lookup auf XML-Konfiguration
    *--- Verwendung des Design Pattern: Factory
    If Lower(m.tcToken) == "filesystemobject"
      m.lcClass = m.tcToken
    EndIf

    m.loReturn = NewObject(m.lcClass, m.lcLibrary)
  Catch To loException
    m.loReturn = .Null.
    Assert .F. Message m.loException.Message
  EndTry

  Return m.loReturn
EndFunc
EndDefine
```


Das war's auch schon. Der Singleton schaut beim Aufruf der GetReference-Methode zuerst in seiner Collection nach, ob bereits eine Objektreferenz für das Token vorhanden ist oder nicht. Bei negativer Prüfung erzeugt der Singleton die Instanz selbst, speichert die Referenz intern und liefert sie an den Aufrufenden zurück.

Wie im Quellcode bereits kommentiert, kann die Implementierung der geschützten Methode im Prinzip beliebig unterschiedlich ausfallen. Dabei spielt es auch keine Rolle, ob man Instanzen von VFP-Klassen, COM-Servern oder etwa Web Services erzeugt. Der Singleton muss nur wissen er eine einzige Instanz produzieren kann, der Rest funktioniert dann automagical.

Im weiteren Verlauf der Verwendung braucht sich der Entwickler dann keine weiteren Gedanken mehr machen.

Leider oder zum Glück fehlt Visual FoxPro das Konzept von statischen Klassen (static). Über dieses Sprachkonstrukt wäre man sehr wohl in der Lage die Einmaligkeit einer Klasseninstanz zu gewährleisten. Hm, dabei fällt mir gerade ein, dass es seit einiger Zeit ja den Befehl AInstance() gibt. Durch Integration in die Init-Methode des Singleton können wir dann doch wiederum was in der Art wie "static" programmieren:  

```foxpro
Define Class AbstractSingleton As Collection
  *------------------------------------------------------------------
  * Sicherstellen, dass der Singleton nur einmalig existiert.
  *------------------------------------------------------------------
  Function Init() As Boolean
    Local lnCount, laInstances[1]

    m.lnCount = AInstance(m.laInstances,This.Class)
    Return (m.lnCount < 1)
  EndFunc
  *...
EndDefine
```


Nicht ganz fein, aber es funktioniert. Auf diese Weise stellen wir sicher, dass unser Singleton selbst nur einmal existiert und dass er immer nur eine Referenz von angefragten Objekten erzeugt und liefert.

Ich hoffe, dass ich euch mit dem hier gezeigten Code und den Erklärungen des Design Pattern Singleton ein wenig plausibel machen konnte.  
Bis denne, JoKi