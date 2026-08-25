---
uid: zwei-unterschiedliche-datenbanken-in-adonet-verbinden
title: Zwei unterschiedliche Datenbanken in ADO.NET verbinden
date: 2006-04-28
status: published
type: post
description: Zwei unterschiedliche Datenbanken in ADO.NET verbinden.
tags:
- Development
keywords: Development
metaTitle: Zwei unterschiedliche Datenbanken in ADO.NET verbinden
metaDescription: Zwei unterschiedliche Datenbanken in ADO.NET verbinden.
image: ''
ogTitle: Zwei unterschiedliche Datenbanken in ADO.NET verbinden
ogDescription: C#, ADO.NET, Ole DB Provider, ADOX, FoxPro, Access
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
canonicalUrl: https://jochen.kirstaetter.name/zwei-unterschiedliche-datenbanken-in-adonet-verbinden/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-28T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: C#, ADO.NET, Ole DB Provider, ADOX, FoxPro, Access
twitterTitle: Zwei unterschiedliche Datenbanken in ADO.NET verbinden
twitterDescription: C#, ADO.NET, Ole DB Provider, ADOX, FoxPro, Access
twitterImage: 
facebookTitle: Zwei unterschiedliche Datenbanken in ADO.NET verbinden
facebookDescription: C#, ADO.NET, Ole DB Provider, ADOX, FoxPro, Access
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
C#, ADO.NET, Ole DB Provider, ADOX, FoxPro, Access

## Die Anforderung
Dieser Beitrag basiert auf einer netten Unterhaltung auf [myCSharp.de](https://www.myCSharp.de) zum Thema Zugriff auf Access und FoxPro-Datenbank. Die eigentliche Problemstellung ist, dass als Ergänzung zu einer Warenwirtschaftssoftware (geschrieben in VFP) weitere Informationen per Microsoft Access ergänzt wurden. Diese beiden Datenquellen sollen über ADO.NET in einer C#-Anwendung angezeigt und bearbeitet werden können. Natürlich gibt es hierzu unterschiedliche Philosophien und Lösungsansätze. Da unter anderem erwähnt wurde, dass ein Umstieg auf den Microsoft SQL Server angedacht sei, war eine meiner Ideen, dass man das Feature *Verknüpfte Server* nutzen könnte, um dem Client nur noch eine Datenquelle zu präsentieren.

## Unterhaltungsverlauf und Gespräche
Wie aus der Unterhaltung unschwer zu erkennen sein dürfte, gibt es sicherlich viele Wege nach Rom. Nun, Ronny und ich hatten noch ein paar weitere Ideenaustausche per Mail und ich habe ihn auf verschiedene Ressourcen im Bereich VFP und C# hingewiesen. Der Vollständigkeit wegen hier nochmal die Auflistung:

[Connection Strings](https://www.connectionstrings.com)  
[VFP Datenbank in .NET](xref:vfp-datenbank-in--net)  
[In 80 Zeilen um die VFP-Tabelle](xref:in-80-zeilen-um-die-vfp-tabelle)  
[Webcast: Visual FoxPro als Datenbank für Visual Studio 2005](https://www.microsoft.com/germany/MSDN/webcasts/library.aspx?id=118758879)

Letztendlich, bleibt es dann doch beim direkten Zugriff auf die VFP-Tabellen. Nach einiger Zeit bekam ich dann wieder Post von ihm und dabei machte mich folgende Aussage doch ziemlich stutzig:

*Die DB die mir zur Verfügung steht ist angeblich leider aus Performancegründen lt. Hersteller NICHT mit PrimaryKeys bestückt.*

Nunja, Primärschlüssel sind meiner bescheidenen Meinung nach eigentlich das A und O einer performanten Datenbank, insbesondere mit der Idee, dass ein Index auf der Tabelle sitzt, der gerade die SQL-Statements auf die Tabelle erheblich beschleunigt. Gerade in VFP mit seiner Rushmore-Optimierung. Eventuell werde ich mal eine Mail in Richtung Hersteller senden und nachfragen. Schliesslich gibt es täglih neue Dinge zu lernen.

## Fehlender Primärschlüssel in ADO.NET
Damit sind wir beim eigentlichen Kern dieses Beitrags. In ADO.NET gibt es unterschiedliche Möglichkeiten DataConnections und daraus resultierende DataSets zu produzieren. Leider verlässt sich der visuelle Assistent jedoch auf das Vorhandensein eines Primärschlüssels. Auch kann man auf diese Weise beispielsweise nicht die Fähigkeiten des OleDbCommandBuilder nutzen, um sich die SQL-Statements für INSERT, UPDATE und DELETE generieren zu lassen. Schade eigentlich... Aber eines der starken Features von ADO.NET im Vergleich zu vorherigen Technologien wie etwa ADO ist jedoch die Tatsache, dass man die Commands selbst formulieren kann. Das ist auch in Verbindung mit dem SQL Server hochinteressant. Denn aus Sicherheitsgründen wird beispielsweise die direkte Manipulationen von Tabellen nicht zugelassen und die Verarbeitung kann nur über Stored Procedures erfolgen, während SELECT-Statements problemlos abgesetzt werden können. Nun die DataCommand-Klassen in ADO.NET sind absolut flexibel um diesen Task meisterlich zu absolvieren. Schauen wir uns dies mal an.

**Die Lösungsidee...**  
Ausgehend von der vorliegenden Struktur der VFP-Tabelle, dem Tabellenfeld, und den zusätzlichen Informationen in der Access-Datenquelle erstellen wir uns zuerst zwei unabhängige DataConnections über die wir die weitere Kommunikation fahren werden. Nach meinem aktuellen Kenntnisstand ist die Abhängigkeit eine logische 1:1-Beziehung, und diese werden wir in der C#-Anwendung als Windows Form anzeigen und verändern. Wir werden die VFP-Tabelle als Master in einem DataGrid anzeigen und die weiteren Details aus der Access-Tabelle in weiteren UI-Controls. Sicherlich interessant ist, dass die Navigation synchron erfolgt und das Änderungen in beiden Datenquellen erfolgen können.

## Strukturanalyse und Statements formulieren