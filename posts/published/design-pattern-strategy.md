---
uid: design-pattern-strategy
title: 'Design Pattern: Strategy'
slug: design-pattern-strategy
date: 2006-04-04
status: published
type: post
description: 'Design Pattern: Strategy Heute denken wir uns einmal eine Strategie aus, wie wir Problemstellungen in unseren Anwendungen schneller, flexibler und einfacher lösen können. Dieser Artikel beschreibt die exemplarische Implementierung des Entwurfsmuster Strategie (Strategy) in Visual FoxPro.Schauen wir uns zunächst einmal wieder die Definition aus der Wikipedia an:Strategie-Objekte werden ähnlich wie'
tags:
- Development
keywords: Development
metaTitle: 'Design Pattern: Strategy'
metaDescription: 'Design Pattern: Strategy Heute denken wir uns einmal eine Strategie aus, wie wir Problemstellungen in unseren Anwendungen schneller, flexibler und einfacher lösen können. Dieser Artikel beschreibt die exemplarische Implementierung des Entwurfsmuster Strategie (Strategy) in Visual FoxPro.Schauen wir uns zunächst einmal wieder die Definition aus der Wikipedia an:Strategie-Objekte werden ähnlich wie'
image: ''
ogTitle: 'Design Pattern: Strategy'
ogDescription: Heute denken wir uns einmal eine Strategie aus, wie wir Problemstellungen in unseren Anwendungen schneller, flexibler und einfacher lösen können. Dieser Artikel beschreibt die exemplarische...
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
canonicalUrl: https://jochen.kirstaetter.name/design-pattern-strategy/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-04T01:00:00Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Heute denken wir uns einmal eine Strategie aus, wie wir Problemstellungen in unseren Anwendungen schneller, flexibler und einfacher lösen können. Dieser Artikel beschreibt die exemplarische...
twitterTitle: 'Design Pattern: Strategy'
twitterDescription: Heute denken wir uns einmal eine Strategie aus, wie wir Problemstellungen in unseren Anwendungen schneller, flexibler und einfacher lösen können. Dieser Artikel beschreibt die exemplarische...
twitterImage: 
facebookTitle: 'Design Pattern: Strategy'
facebookDescription: Heute denken wir uns einmal eine Strategie aus, wie wir Problemstellungen in unseren Anwendungen schneller, flexibler und einfacher lösen können. Dieser Artikel beschreibt die exemplarische...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Heute denken wir uns einmal eine Strategie aus, wie wir Problemstellungen in unseren Anwendungen schneller, flexibler und einfacher lösen können. Dieser Artikel beschreibt die exemplarische Implementierung des Entwurfsmuster Strategie (Strategy) in Visual FoxPro.

Schauen wir uns zunächst einmal wieder die Definition aus der Wikipedia an:

*Strategie-Objekte werden ähnlich wie Klassenbibliotheken verwendet. Im Gegensatz dazu handelt es sich jedoch nicht um externe Programmteile, die als ein Toolkit genutzt werden können, sondern um integrale Bestandteile des eigentlichen Programms, die deshalb als eigene Objekte definiert wurden, damit sie durch andere Algorithmen ausgetauscht werden können.*

*Meistens wird eine Strategie durch Klassen umgesetzt, die eine bestimmte Schnittstelle implementieren. In Sprachen wie Smalltalk, in denen auch der Programmcode selbst in Objekten abgelegt werden kann, kann eine Strategie aber auch durch solche Code-Objekte realisiert werden.*

*Die Verwendung von Strategien bieten sich an, wenn  
- viele verwandte Klassen sich nur in ihrem Verhalten unterscheiden,  
- unterschiedliche, austauschbare Varianten eines Algorithmus benötigt werden,  
- Daten innerhalb eines Algorithmus vor Klienten verborgen werden sollen oder  
- verschiedene Verhaltensweisen innerhalb einer Klasse fest integriert (meist über Mehrfachverzweigungen) sind und  
- die verwendeten Algorithmen wiederverwendet werden sollen oder  
- die Klasse flexibler gestaltet werden soll.*

Hat jemand was verstanden? Ich hab's auf den ersten Blick ehrlich gesagt nicht kapiert und mir daher mal verschiedene Gedanken über den obigen Inhalt gemacht. Dabei bin ich von der Situation *viele verwandte Klassen sich nur in ihrem Verhalten unterscheiden* aus gestartet. Okay, also viele verwandte Klassen bedeutet zunächst, dass eine abstrakte Klasse und zig Ableitungen davon gibt, die alle über die gleiche Schnittstelle verfügen. Soweit ja noch klar. Damit können wir sicherstellen, dass die einzelnen Klassen austauschbar werden und wir erhalten Flexibilität und Wiederverwendbarkeit.

Jetzt brauchen wir noch irgendetwas, welches wir als Ansprechpartner innerhalb unserer Anwendung nutzen können. Diese Komponente trägt dann auch dafür Sorge, dass die jeweilige Instanz des gewünschten Verhaltens verwendet wird. Wir müssen uns also nicht mehr drum kümmern, sondern unterhalten uns nur mit dieser Komponente. Somit kapseln wir die einzelnen Strategien vom Klienten.

Gut, damit ergeben sich für uns folgende Erkenntnisse:  
- abstrakte Klasse für die Schnittstelle (abstrakte Strategie)  
- beliebige Anzahl konkreter Klassen mit dem Algorhythmus (konkrete Strategie)  
- einen Ansprechpartner für unsere Aufrufe (Kontext)  
- und unsere Anwendung (Klient)

## Unsere Anforderung
Der nachfolgende Beispielcode geht davon aus, dass wir ein Exportmodul für unsere Anwendung erstellen wollen. Wir haben einen Cursor und wollen diesen in unterschiedliche Formate exportieren. Das heißt, wir haben unterschiedliche Ausgabeformate für den gleichen Input und wollen dies auf flexible Art und Weise lösen. Das Beispiel selbst ist sehr einfach gehalten und steht in Analogie zum Befehl Copy To in VFP, aber auch weiteren Exportmöglichkeiten.

## Abstrakte Strategie
Als erstes erstellen wir uns unsere Klassendefinition für alle Exportvarianten:  

```
\*//- Abtrakte Basisklasse für alle Exporttypen (abstrakte Strategie)  
Define Class AbstraktExport As Custom && Abstract Strategy  
cDateierweiterung = ""  
cVerzeichnis = ""  
cDatei = ""  
cBeschriftung = ""  
  
Function Schreiben() As Boolean  
EndFunc  
EndDefine
```
  
Ganz einfach gehalten. Es gibt ein Informationen zur Ausgabedatei und die eigentliche Methode zum Erzeugen der Ausgabe.

## Konkrete Strategie(n)
Wir leiten uns hier für jeden Exporttypen, den wir anbieten wollen, eine eigene Klasse von unserer abstrakten Strategie ab und implementieren den Code in der Methode schreiben. Wir wollen folgende Formate anbieten: CSV, XML und Excel. Dazu definieren wir uns drei Klassen:  

```
\*--- Export als kommaseparierte Liste (CSV)  
Define Class ExportCsv As AbstraktExport && (konkrete Strategie)  
cDateierweiterung = ".txt"  
cBeschriftung = "Export als kommaseparierte Liste"  
  
Function Schreiben() As Boolean  
Local llOk, lcAlias  
llOk = .T.  
lcAlias = Alias()  
  
Select(m.lcAlias)  
Try  
Copy To (This.cDatei + This.cDateierweiterung) Type Csv  
Catch  
llOk = .F.  
EndTry  
  
Return m.llOk  
EndFunc  
EndDefine

\*--- Export nach XML  
Define Class ExportXml As AbstraktExport  
cDateierweiterung = ".xml"  
cBeschriftung = "XML-Datei (\*.xml)"  
  
Function Schreiben() As Boolean  
Local llOk, lcAlias  
llOk = .T.  
lcAlias = Alias()  
  
Select(m.lcAlias)  
Try  
CursorToXML(m.lcAlias, ;  
This.cDatei + This.cDateierweiterung, ;  
1, 4+8+48+512, 0, "1")  
Catch  
llOk = .F.  
EndTry  
  
Return m.llOk  
EndFunc  
EndDefine

\*--- Export nach Excel (einfach)  
Define Class ExportExcel As AbstraktExport && (konkrete Strategie)  
cDateierweiterung = ".xls"  
cBeschriftung = "Export nach Excel"  
  
Function Schreiben() As Boolean  
Local llOk, lcAlias  
llOk = .T.  
lcAlias = Alias()  
  
Select(m.lcAlias)  
Try  
Copy To (This.cDatei + This.cDateierweiterung) Type Xl5  
Catch  
llOk = .F.  
EndTry  
  
Return m.llOk  
EndFunc  
EndDefine  
```
  
Insgesamt gewohnter Anblick und vertraute VFP-Befehle. Dennoch sehen wir, dass der Export nach Excel und CSV über Copy To erfolgt, während die Ausgabe nach XML über CursorToXML() realisiert wird. Und hier zeichen sich bereits die ersten Vorteile unserer Strategie ab. Egal, welches Ausgabeformat wir haben wollen, würden wir aktuell immer nur die Methode Schreiben() ausführen.

## Die Kapselung (oder der Kontext)
Gut, zum gegenwärtigen Zeitpunkt haben wir nur ein paar lose Klassendefinitionen rumfliegen. Natürlich wollen wir in unserer Anwendung nur einen zentralen Punkt haben, über den wir den Export veranlassen können. Weiterhin wollen wir ebenfalls nicht, dass an beliebigen Stellen einfach mal zig Instanzen unserer konkreten Strategien produziert werden. Daher erstellen wir uns eine weitere Klassen, die zur Verwaltung unserer unterschiedlichen Ausgabeformate genutzt wird und als Kommunikationspartner mit unserer Anwendung zur Verfügung steht.  

```
\*--- Verwaltungsklasse unserer Ausgabeformate  
Define Class ExportHandler As Custom && (Kontext)  
Protected oExportTyp  
oExportTyp = .Null.  
  
Function Init() As Boolean  
\*--- Initialen Exporttyp laden (Default)  
This.oExportTyp = CreateObject("ExportXml")  
EndFunc

Function Destroy() As Boolean  
This.oExportTyp = .Null.  
EndFunc

Function SetzeExportTyp(tcExportTyp As String) As Boolean  
This.oExportTyp = .Null.  
Try  
This.oExportTyp = CreateObject("Export" + m.tcExportTyp)  
Catch  
This.oExportTyp = .Null.  
Finally  
Return (Vartype(This.oExportTyp) == "O")  
EndTry  
EndFunc

Function GebeExportTyp() AS String  
Return This.oExportTyp.cBeschriftung  
EndFunc

Function Schreiben(tcDateiname As String) As Boolean  
This.oExportTyp.cDatei = Juststem(tcDateiname)  
This.oExportTyp.cVerzeichnis = Evl(JustPath(tcDateiname),FullPath(""))

Return This.oExportTyp.Schreiben()  
EndFunc  
  
Function ToCsv(tcDateiname As String) As Boolean  
This.SetzeExportTyp("Csv")  
Return This.Schreiben(m.tcDateiname)  
EndFunc

Function ToXml(tcDateiname As String) As Boolean  
This.SetzeExportTyp("Xml")  
Return This.Schreiben(m.tcDateiname)  
EndFunc  
EndDefine  
```
  
Ich habe hier zwei Ansätze in der Klasse implementiert:  
- Allgemeiner Ansatz, wir haben die Kontrolle über das gewünschte Ausgabeformat  
- Vereinfachte Methoden (ToCvs, ToXml, etc.)  
Und so langsam dürfte erkennbar sein, warum das Entwurfsmuster Strategie sehr nützlich ist. Wir müssen nun in unserer Anwendung nur noch den Kontext instanziieren und alles weitere geht dann automatisch.  

```
oExport = CreateObject("ExportHandler")  
oExport.SetzeExportTyp("Excel")  
? oExport.Schreiben("C:TempMeinExportExcel")  
? oExport.ToXml("C:TempMeinExportXML")  
```


## Ausbaustufen
Gut mit diesem Grundgerüst können wir bereits erste Ergebnisse produzieren und fleissig arbeiten. Sollten wir die Anforderung erhalten, weitere Ausgabeformate in unserer Anwendung anzubieten, dann ergeben sich uns hier maximal zwei Schritte, die wir durchführen müssen. Als erstes erstellen wir eine neue Klasse für das geforderte Ausgabeformat (notwendig) und als zweites können wir im Kontext eine neue Methode anbeiten (optional), die das neue Format nach außen anbietet. Und das war's bereits.

Die Methode im Kontext zum Einstellen des gewünschten Exporttyps kann man übrigens noch problemlos aufbohren. Wir haben in unseren Anwendungen eine Verwaltungstabelle für verschiedene Import- und Exportformate. Dabei nutzen wir innerhalb der Anwendung, so wie hier im Code Tokens und setzen eine Abfrage auf die Tabelle ab, um die Informationen zu Klassenname, Klassenbibliothek, Beschriftung, Dateierweiterung, etc. in Erfahrung zu bringen.

Das gezeigte Beispiel behandelt den Export von Informationen. Natürlich lässt sich das Konzept auch auf andere Szenarien anwenden, hier mal ein paar Möglichkeiten: Import \*g\*, Verschlüsselung, Konvertierung, und so weiter...

Übrigens, wenn man den Druck ebenfalls als Datenexport betrachtet, braucht man lediglich eine neue Klasse zu schreiben und anzubinden. Was potentiell für einfache Reports sehr praktisch sein kann.  

```
\*--- Export als Druckdokument  
Define Class ExportReport As AbstraktExport  
Protected cReportDatei  
cReportDatei = "Schnellausgabe.frx"  
  
Function Schreiben() As Boolean  
Local llOk, lcAlias  
llOk = .T.  
lcAlias = Alias()  
  
Select(m.lcAlias)  
Try  
Report Form (This.cReportDatei) To Printer Prompt  
Catch  
llOk = .F.  
EndTry  
  
Return m.llOk  
EndFunc  
EndDefine  
```


Okay, jetzt aber genug... Ich hoffe, dass dieser Artikel das grundsätzliche Konzept des Strategie-Muster ausreichend erklärt, und dass der gezeigte Quellcode leicht verständlich sowie nachvollziehbar ist.  
Bis denne, JoKi