---
uid: devcon-prag-2006---day-1
title: Devcon Prag 2006 - Day 1
slug: devcon-prag-2006---day-1
date: 2006-09-11
status: published
type: post
description: Devcon Prag 2006 - Day 1 Nach einer kurzen Nacht, etwa 5 Std oder so und einem kurzen Fr&#252;hst&#252;ck ging&#39;s sofort zur Registrierung f&#252;r die heute startende VFP-Konferenz in Prag. Gl&#252;cklicherweise lief bis jetzt alles sehr relaxed ab.**Keynote**A tribute to community and everything connects - ich denke, dass d&#252;rfte die
tags:
- Community
keywords: Community
metaTitle: Devcon Prag 2006 - Day 1
metaDescription: Devcon Prag 2006 - Day 1 Nach einer kurzen Nacht, etwa 5 Std oder so und einem kurzen Fr&#252;hst&#252;ck ging&#39;s sofort zur Registrierung f&#252;r die heute startende VFP-Konferenz in Prag. Gl&#252;cklicherweise lief bis jetzt alles sehr relaxed ab.**Keynote**A tribute to community and everything connects - ich denke, dass d&#252;rfte die
image: content/images/2006/09/photo-1504723433512-1f76737fa834.webp
ogTitle: Devcon Prag 2006 - Day 1
ogDescription: Nach einer kurzen Nacht, etwa 5 Std oder so und einem kurzen Frühstück ging's sofort zur Registrierung für die heute startende VFP-Konferenz in Prag. Glücklicherweise lief bis jetzt alles sehr relaxed...
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
canonicalUrl: https://jochen.kirstaetter.name/devcon-prag-2006---day-1/
imageUrl: content/images/2006/09/photo-1504723433512-1f76737fa834.webp
twitterImageUrl: https://images.unsplash.com/photo-1504723433512-1f76737fa834?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=bc80d5d8a1ba76751da069a216d82d61
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2006/09/photo-1504723433512-1f76737fa834.webp
featured: false
publishedAt: 2006-09-11T11:24:53Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Nach einer kurzen Nacht, etwa 5 Std oder so und einem kurzen Frühstück ging's sofort zur Registrierung für die heute startende VFP-Konferenz in Prag. Glücklicherweise lief bis jetzt alles sehr relaxed...
twitterTitle: Devcon Prag 2006 - Day 1
twitterDescription: Nach einer kurzen Nacht, etwa 5 Std oder so und einem kurzen Frühstück ging's sofort zur Registrierung für die heute startende VFP-Konferenz in Prag. Glücklicherweise lief bis jetzt alles sehr relaxed...
twitterImage: 
facebookTitle: Devcon Prag 2006 - Day 1
facebookDescription: Nach einer kurzen Nacht, etwa 5 Std oder so und einem kurzen Frühstück ging's sofort zur Registrierung für die heute startende VFP-Konferenz in Prag. Glücklicherweise lief bis jetzt alles sehr relaxed...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
Nach einer kurzen Nacht, etwa 5 Std oder so und einem kurzen Frühstück ging's sofort zur Registrierung für die heute startende [VFP-Konferenz in Prag](https://www.daquas.cz/fox/devcon2006an/). Glücklicherweise lief bis jetzt alles sehr relaxed ab.

\*\*Keynote\*\*  
A tribute to community and everything connects - ich denke, dass dürfte die beste Beschreibung der Keynote sein. Mit dem obligatorischen Gedenken an Drew und Brent Speedie startete YAG seine Premiere in Prag. Und das obwohl er bereits seit nunmehr 4 Jahren eingeladen wurde. Tja, gut Ding will Weil haben. Alan brachte im Laufe der nächsten zwei Stunden viele Details und Infos aus den Aktivitäten der Community - etwa die Videos von Kevin Ragsdale, die anstehenden Entwicklungen von Sedna, die CodePlex Entwicklungsplattform und eines der Projekte: VFPX (aka SednaX).  
Am interessantesten waren sicherlich die Erweiterungen und Möglichkeiten, welche durch das Service Pack 2 und Sedna uns VFP-Codern gegeben werden wird. Hierunter fallen weitere Verbesserungen für das Reporting System von VFP; etwa dynamische Eigenschaften und Rotation für Reportobjekte. Selbstverständlich mit den entsprechenden visuellen Buildern.

\*\*Understanding Windows Communication & Presentation Foundations\*\*  
WCF (aka Indigo) ist die Summe aus System Messaging, WSE, Remote Messaging, ...  
Vereinheitliche Kommunikationsmöglichkeiten über mehrere Wege und Zusammenfassung der API der unterschiedlichen Technologien in eine einzige API.  
Service Oriented Architecture (SOA)  
Interop mit anderen Systemen wie etwa Java möglich  
Es gibt hierbei diverse Hosts wie etwa WAS, WPF, .EXE, NT Service oder COM+  
Das Messaging erfolg über Channels; dabei handelt es sich sowohl um Protokolle, wie etwa TCP, aber auch um höhere Kommunikationsmöglichkeiten, etwa Security Channel. Interessanterweise können die Kommunikationswege ad hoc zur Laufzeit per XML-Konfigurationsdateien ausgetauscht werden.  
Weiterhin erfolgt die Unterhaltung über einen sogenannten Vertrag (Contract) zwischen Client und Server (genauer über die vorhandenen Endpoints), über den die Konditionen der Verbindung definiert sind und für den Verlauf der Unterhaltung Gültigkeit besitzen.  
ABC von WCF: Address (Where?), Binding (How?) und Contract (What?)  
Im Interface der .NET Klassendefinition wird durch Direktiven für WCF erweitert: ServiceContract oder OperationContract - Referenz zu System.ServiceModel nicht vergessen.  
Die Demo zeigte die Funktionalität sowohl in einer Konsoleanwendung wie auch gleichzeitig im IE. WCF ermöglicht es, auf einfache und universelle Art und Weise einen Applikationserver in .NET zu realisieren.

WPF (aka Avalon) ist eine Modernisierung der etwas in die Jahre gekommenen GDI-Fähigkeiten kombiniert mit den modernen Darstellungsmöglichkeiten in GDI+, 2D, 3D, Video, und so weiter... Bei WPF handelt es sich um eine integrierte, vektorbasierte Darstellungsengine, welche intern auf DirectX zur Visualisierung zugreift und die Darstellung sauber von der Funktionlität trennt. Die Präsentation wird mittels XAML deklarativ formuliert und zur Anwendung gebracht. Hehehe, mit dem Ausblick auf die Interop-Kapazität von Sedna wird es extremst spannend werden, wenn man die beiden Technologien miteinander kombiniert (Two Secret Weapons combined). 😎  
XAML als deklarative Sprache für die Benutzeroberfläche ermöglicht es, die Aufgabenverteilung in derProjektentwicklung weiter zu separieren. Dadurch kann man wie bei der Webentwicklung verschiedene Teams zur Umsetzung beauftragen: Programmierteam und Visualteam. Ein wichtiges Kriterium, wenn man bedenkt, dass Entwickler nicht zwangsläufig Grafikdesigner und umgekehrt sind.  
XAML Plugin für weitere Browser wie etwa Safari, Mozilla oder Firefox sind seitens Microsoft angedacht. Die Verwendung von XAML in der Webumgebung wird primär mit dem IE7 möglich werden. Potentiell wird dieser Ansatz auch auf weitere Betriebssysteme erweitert werden. Damit kann man durch die Kombination eines Windowsbasierten Applikationsserver und diversen Clients sehr viel umfangreicher unterschiedliche Kunden ansprechen und für die eigenen Anwendungen gewinnen.  
XamlPad kann zum Testen von deklarativem XAML genutzt werden. Interessanterweise ist die Kombinationsfreiheit für das Zusammensetzen der UI extremst hoch. Als Beispiele wurden etwa Videos auf Buttons gezeigt, oder einen Button innerhalb einer Combobox. Ich denke, das hier eine tolle Spielwiese für coole Benutzeroberflächen zur Verfügung gestellt wird. Aber... es gilt zu beachten, dass man es nicht übertreibt, da die Benutzer auch intuitiv mit der Applikation in gewohnter Weise umgehen sollten.

\*\*Extending VFP with VFP\*\*  
Seit Jahren ist Visual FoxPro als Produkt erweiterbar. Beginnend mit den \_&lt;Component&gt; Systemvariablen in FoxPro DOS, über die Builder seit VFP 3 und der Einführung von IntelliSense in VFP 7.0. Durch die freie Verfügbarkeit des Quellcodes sämtlicher zusätzlicher Applikationen (XSource.zip) kann man nicht nur sehen, wie die Tools funktionieren, sondern hat die Freiheit diese zu ergänzen und in eigenen Anwendungen wieder zu verwenden. Dies ist alles unter What's New in den Solutions Samples eindrucksvoll hinterlegt, aber die meisten Entwickler wissen es nicht. Eine sehr gutes Beispiel ist die Funktionalität von \_MenuHit. Hierüber kann man den nativen Code von VFP abfangen und eigene Tools integrieren. Etwa einen verbesserten Dialog für das Anlagen von Properties oder Methods. Die Technik dahinter wird wie so vieles über die Fähigkeiten von IntelliSense abgedeckt. Durch Anlage von neuen Datensätzen in der \_FoxCode-Tabelle ist es möglich sämtliche Menüeinträge abzufangen und eigene Routine stattdessen auszuführen.  
Eine weitere Möglichkeit zum Verfeinern der IDE ist die Integration von eigenen PropertyEditoren in das Property Sheet. So, kann man für native und eigene Properties wiederum mehr Kontrolle produzieren. Etwa, dass man logischen Eigenschaften eine Combobox zur Auswahl des Wertes verabreichen kann. Bei der Entwicklung eigener Erweiterungen sollte man auf alle Fälle folgendes Statement bei der Entwicklung bzw. beim Debuggen absetzen:  
[code]Sys(2030,1)[/code]  
Bedingt durch die Einschränkungen für die Zeichenlänge von VFP-Eigenschaften kann man die Verweise auf die PropertyEditor ebenfalls in der \_FoxCode ablegen. Man muss dazu im Memberdata Editor lediglich 'Global' verwenden. Durch Verwendung einer tabellenbasierten Factory mit gleichartigen Editorklassen erzeugt man sich sehr viel Flexibilität für die tägliche Programmierung. Durch Abfrage auf die Tabelle erhält man eine Objektreferenz auf den gewünschten PropertyEditor und kann dann die spezifische Bearbeitung für das gewählte Attribut umsetzen.  
Mittels IntelliSense können übrigens auch technische Richtlinien bei der Programmierung eingehalten werden. Etwa die implizite Erweiterung des Local-Statement für Variablen. Doug Hennig zeigte dies sehr eindrucksvoll mit Hilfe eines eigenen Skripts. Im übrigen gibt es im FoxWiki sehr nützliche Beispiele für Custom IntelliSense Scripts.  
Mit dem Ausblick auf den My-Namescape waren hier viele Informationen in kurzer Zeit zum Thema Erweiterbarkeit von Visual FoxPro verfügbar.

\*\*Object Thinking\*\*  
Die Historie der verschiedenen VFP-Versionen als Aufhänger zur Session. Wie hat sich die Denkweise der eigenen Programmierung im Laufe der Zeit in den verschiedenen Versionen geändert? gab es überhaupt eine persönliche Weiterentwicklung, oder doch nur eine Aktualisierung des Werkzeugs bei gleicher Arbeitweise.  
Literatur: MS Press Object Thinking by David West.

- Everything is an object  
- Simulation of the problem aids in object discovery and definition (Modelling)  
- Objects must be composable (Building larger objects)  
- Distributed objects must replace hierarchical centralized control (Independence)

Was macht ein Objekt eigenlich aus?  
Inheritance, Responsibility (One thing and one thing only), Delegation (Aufgaben abgeben), Polymorphism (Gleicher Name bei unterschiedlichem Verhalten) und Encapsulation (Autarkes Arbeiten mit Wissen über weitere Informationsbeschaffung; Bsp: Telefonnummer von jemand herausbekommen)  
Wie können wir die Ziele erreichen?  
Gemeinsames Vokabular und Grammatik definieren, etwa durch Erstellung eines Glossar  
Evaluation criteria - Zielvorgabe definieren, denn der Kunde weiß nicht, was eigentlich er will  
Decomposition based on "natural joints" in the domain - Zerlegung der natürlichen Verhältnisse in kleinere Bausteine.  
Responsibility assignment based on behavior - jedes Objekt hat nur eine einzige Aufgabe und ist dafür verantwortlich.  
Aggregation of objects by interaction  
A way to add design und implementation detail - Flexibilität für spätere Anpassungen und Erweiterungen berücksichtigen

\*\*Adding IntelliSense to Your Applications\*\*  
Scripting, Expression Builder oder AutoCorrect (Commonly Expressions und Abbrevs) mit Auswahllisten. Die Systemvariablen \_CodeSense und \_FoxCode sind in der Runtime leer, sobald diese gesetzt werden, funktioniert auch IntelliSense zur Runtime. Am einfachsten erzeugt man sich einen generischen Stub für alle Projekte.  
[code]\_CodeSense = "foxcode.exe"  
\_FoxCode = "foxcode.dbf"[/code]  
Dazu erstellt man sich ein neues Projekt und ergänzt die beiden Dateien foxcode.prg and foxcode2.dbf. Das war's auch schon fast. Ein wenig die überflüssigen Bestandteile entsorgt und kompilieren. Durch Löschen von vorhandenen Datensätzen kann man dem Anwender einen reduzierten Satz der Befehle geben. Klingt soweit schon sehr motivierend, aber leider gibt's ein paar Restriktionen: IntelliSense funktioniert nur in PRG und Memos (hier nur unter bestimmten Bedingungen) und nicht wie vllt. gedacht in Editboxen. Die beste Empfehlung ist der Weg über PRGs:  
[code]Modify Command (m.lcFile) Window (m.loForm.Name)[/code]  
Bei einer Top-Level Form muss die Klausel 'In Window' angegeben werden. Weiterhin ist es sicherlich sinnvoll, wenn man in der Anwendung eine Möglichkeit zur Verwaltung der Snipplets anbietet. Bei Klassen ist es hilfreich, wenn man ebenfalls eine Möglichkeit anbietet, um überflüssige PEMs ausblenden zu können bzw. nur die benötigten anzeigt. Stichwort: Favoriten (FfiBuilder)  
\*\*Abschliessender Eindruck des ersten Tages\*\*
