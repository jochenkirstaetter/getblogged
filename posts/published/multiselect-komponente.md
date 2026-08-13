---
uid: multiselect-komponente
title: MultiSelect-Komponente
slug: multiselect-komponente
date: 2005-03-05
status: published
type: post
description: Die Selektion von mehreren Elementen in einem Control wie etwa dem Grid oder einem TreeView-Control ist sicherlich praktisch und generell interessant.
tags:
- Development
keywords: Development
metaTitle: MultiSelect-Komponente
metaDescription: Die Selektion von mehreren Elementen in einem Control wie etwa dem Grid oder einem TreeView-Control ist sicherlich praktisch und generell interessant.
image: ''
ogTitle: MultiSelect-Komponente
ogDescription: Heute mal einen technischen Eintrag zu Visual FoxPro und komponentenbasierter Programmierung. Die Selektion von mehreren Elementen in einem Control wie etwa dem Grid (Datenrasterelement bzw. DataGrid)...
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
canonicalUrl: https://jochen.kirstaetter.name/multiselect-komponente/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2005-03-05T00:00:00Z
updatedAt: 2018-04-02T08:39:04Z
excerpt: Heute mal einen technischen Eintrag zu Visual FoxPro und komponentenbasierter Programmierung. Die Selektion von mehreren Elementen in einem Control wie etwa dem Grid (Datenrasterelement bzw. DataGrid)...
twitterTitle: MultiSelect-Komponente
twitterDescription: Heute mal einen technischen Eintrag zu Visual FoxPro und komponentenbasierter Programmierung. Die Selektion von mehreren Elementen in einem Control wie etwa dem Grid (Datenrasterelement bzw. DataGrid)...
twitterImage: 
facebookTitle: MultiSelect-Komponente
facebookDescription: Heute mal einen technischen Eintrag zu Visual FoxPro und komponentenbasierter Programmierung. Die Selektion von mehreren Elementen in einem Control wie etwa dem Grid (Datenrasterelement bzw. DataGrid)...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Heute mal einen technischen Eintrag zu Visual FoxPro und komponentenbasierter Programmierung. Die Selektion von mehreren Elementen in einem Control wie etwa dem Grid (Datenrasterelement bzw. DataGrid) oder einem TreeView-Control ist sicherlich praktisch und generell interessant. Daher meine Idee eine passable Komponente für Acodey zu schreiben.  
  
Warum eine Komponente? Nun, zum einen ist in Acodey alles in kleine Bauteile aufgeteilt und wird dann wieder in Komposits zusammengesteckt und zum anderen habe ich wenig Interesse eine zu starke Bindung mit dem Zielobjekt einzugehen. Daher lieber einen Baustein, der genau eine Aufgabe besitzt und diese entsprechend zu erfüllen weiß.  
  
Okay, als Basisklasse nehmen wir ein Label. Das hat den Vorteil, dass man beim Zusammenstecken von Bausteinen etwa in einen Container oder auf einer Form immer schön den Überblick behält und sieht - im wörtlichen Sinne - welche Funktionalität das produzierte Gebilde besitzt. Gut, damit haben wir klassentechnisch die Grundlage geschaffen.  
  
Wie sieht's nun mit der Schnittstelle aus? Klar, irgendwie muss ein Wert - in welcher Form auch immer - an die und von der MultiSelect-Komponente übergeben werden können. Da der Datentyp unterschiedlich ausfallen kann, nehmen wir uValue (u wie undefined. Nein, kein v wie variant, weil v für views in VFP genutzt wird). Die dazu gehörenden Get/Set-Methoden werden durch Aktivierung der Access/Assign-Methoden reguliert. Jaja, nix tippen, klicken ist angesagt, und die Methoden stehen zur Verfügung.  
  
Als nächstes brauchen wir ein Zielobjekt, auf das die Multiselektion wirken kann - fein, neue Eigenschaft oControl anlegen und zur Laufzeit eine Referenz auf das Zielobjekt ablegen. Dies ermöglicht es uns, dass wir innerhalb der Klasse mittels This.oControl auf das Objekt wirken können und unsere Kapselung besser wird. Auch lässt sich dann besser mit dem Scope arbeiten.  
  
Gut, dann je eine Methode zum Setzen und Lesen eines Wertes, welche direkt auf This.oControl wirken und daher in unserer Klassendefinition als abstrakt anzusehen sind. Die Implementierung erfolgt in einer Ableitung bzw. Instanz der Klasse und geht auf Spezialitäten des Zielobjektes ein - schliesslich hat ein Grid ein anderes Interface als beispielsweise ein TreeView Control. Wenn das fehlerfrei funktioniert, kümmern wir uns um den nächsten Schritt.  
  
Die Verarbeitung von mehreren Werten kann unterschiedlich erfolgen. Als Ausgangsmenge bieten sich auch unterschiedlich Quellen - CSV-Liste, Cursor bzw. Tabelle oder eine Collection - an. Für jeden Quelltyp erstellen wir geschützte Get/Set-Methoden, die sich zum einen um das Zerlegen und Zusammensetzen der Werte kümmern, und zum anderen in einer Schleife die Methode für einen Wert auslösen.  
  
Das Konzept der Interface-Überladung ist in VFP ein wenig anders zu handhaben, aber dennoch sind wir in der Lage es zu nutzen. Jetzt erstellen uns zwei öffentliche Methoden, die es uns gestatten die Menge der Werte entgegen zu nehmen bzw. zu liefern. Ich verwende This.SetValues(tuValues As Variant) zum Setzen der Werte und entsprechend This.GetValues zum Abrufen. In den Methoden erfolgt mittels Fallunterscheidung nach Parametertyp der Aufruf der jeweils zuständigen, internen Methode. Also, wenn man eine CSV-Liste in SetValues() gibt, dann erfolgt die Weitergabe an SetValuesCsv(), usw.  
  
Für die Bestimmung des Ausgabeformats müssen wir unserer Komponente noch eine weitere, öffentliche Eigenschaft - nValueType als Enumeration für die möglichen Rückgabewerte - und eine Methode GetCount() spendieren. This.GetValues entscheidet dann intern auf Grund dieser Eigenschaft, welche Methode zur Assimilation der Menge an Werte (die Anzahl liefert und GetCount) zu verwenden ist, und liefert das gewünschte Resultat als CSV-Liste, Cursor, Collection, etc. zurück.  
  
Damit hätten wir das Grundgerüst für weitere Spezialisierungen. Dabei sind wir von den Eigenheiten des Zielobjekts abhängig. Ich nehme an, dass es brauchbar sein dürfte, eine Ableitung pro Grundtyp an Objekten anzulegen. Danach sind lediglich 3 Methoden zu implementieren: SetValue, GetValue und GetCount  
In den drei Methoden wird auf das Interface des Objekts eingegangen; den Rest haben wir bereits einheitlich in der ParentClass.  
  
Und fertig ist ein universeller Baustein für MultiSelektion in Visual FoxPro.  
  
  
Bis denne, JoKi
