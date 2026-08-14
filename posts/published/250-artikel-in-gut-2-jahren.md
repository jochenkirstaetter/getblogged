---
uid: 250-artikel-in-gut-2-jahren
title: 250 Artikel in gut 2 Jahren?
slug: 250-artikel-in-gut-2-jahren
date: 2006-08-25
status: published
type: post
description: 250 Artikel in gut 2 Jahren? Bei der Betrachtung der Archivsektion in der linken Navigationsleiste beschlich mich der Gedanke, dass es mal interessant w&#228;re zu sehen, wieviele Artikel im Zeitraum seit Juli 2004 bis heute so entstanden sind... Inzwischen schreibe ich seit mehr als 2 Jahren. Wow, ich bin erfreut,
tags:
- General
keywords: General
metaTitle: 250 Artikel in gut 2 Jahren?
metaDescription: 250 Artikel in gut 2 Jahren? Bei der Betrachtung der Archivsektion in der linken Navigationsleiste beschlich mich der Gedanke, dass es mal interessant w&#228;re zu sehen, wieviele Artikel im Zeitraum seit Juli 2004 bis heute so entstanden sind... Inzwischen schreibe ich seit mehr als 2 Jahren. Wow, ich bin erfreut,
image: ''
ogTitle: 250 Artikel in gut 2 Jahren?
ogDescription: Bei der Betrachtung der Archivsektion in der linken Navigationsleiste beschlich mich der Gedanke, dass es mal interessant wäre zu sehen, wieviele Artikel im Zeitraum seit Juli 2004 bis heute so...
layout: post
bodyClass: post-template tag-general
postClass: post tag-general
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
canonicalUrl: https://jochen.kirstaetter.name/250-artikel-in-gut-2-jahren/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-08-25T11:17:14Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Bei der Betrachtung der Archivsektion in der linken Navigationsleiste beschlich mich der Gedanke, dass es mal interessant wäre zu sehen, wieviele Artikel im Zeitraum seit Juli 2004 bis heute so...
twitterTitle: 250 Artikel in gut 2 Jahren?
twitterDescription: Bei der Betrachtung der Archivsektion in der linken Navigationsleiste beschlich mich der Gedanke, dass es mal interessant wäre zu sehen, wieviele Artikel im Zeitraum seit Juli 2004 bis heute so...
twitterImage: 
facebookTitle: 250 Artikel in gut 2 Jahren?
facebookDescription: Bei der Betrachtung der Archivsektion in der linken Navigationsleiste beschlich mich der Gedanke, dass es mal interessant wäre zu sehen, wieviele Artikel im Zeitraum seit Juli 2004 bis heute so...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Bei der Betrachtung der Archivsektion in der linken Navigationsleiste beschlich mich der Gedanke, dass es mal interessant wäre zu sehen, wieviele Artikel im Zeitraum seit Juli 2004 bis heute so entstanden sind... Inzwischen schreibe ich seit mehr als 2 Jahren. Wow, ich bin erfreut, dass es doch geneigte Leser geben soll, die schon sehnsüchtig auf mehr Input warten... \*winke-winke ins Schwabeländle\* 😎

Well, die aktuelle Blogsoftware basiert datentechnisch auf einer MySQL Datenbank 4.irgendwas. Und in Verbindung mit dem MySQL Query Browser oder dem Fuchs ist es auch keine echte Herausforderung:  
`Select count(\*) From posts`  
liefert beim Schreiben des Beitrags exakt **250**.

Der Vollständigkeit wegen das Ganze nun auch in Visual FoxPro:  

```
Local lnHandle  
lnHandle = SQLConnect( ;  
"Driver={MySQL ODBC 3.51 Driver};" + ;  
"Server=jochen.kirstaetter.name;" + ;  
"Port=3306;" + ;  
"Database=blog;" + ;  
"User=blog;" + ;  
"Password=geheim;" + ;  
"Options=19035" ;  
)  
SQLExec(m.lnHandle, "Select count(\*) From posts", "posts")  
Browse Last  
```
  
Unter der Voraussetzung, dass der MyODBC auf dem System installiert ist, ist der Zugriff auf den MySQL Server remote möglich. Auch wenn sich dieser irgendwo auf der Welt befindet. Mein Server ist beispielsweise irgendwo in Minnesota, USA untergestellt. Soweit ich mich erinnern kann... Naja, letztendlich spielt es keine Rolle, wo die Daten tatsächlich physikalisch abgelegt sind. Es hätte sich auch genauso gut um einen anderen Datenbankserver handeln können.

Achja, das Attribut \*Options\* ist absichtlich so gewählt. Im Gegensatz zu den Beispielen auf [ConnectionStrings.com](https://www.connectionstrings.com/) erziele ich gegenwärtig mit dem Wert 19035 die besten Ergebnisse mit dem Fuchs. Der Zahlenwert ist übrigens die dezimale Repräsentation der Bits im Dialog Einstellungen der Verbindung des MyODBC-Treibers. Alternativ kann auch eine DSN im ODBC Administrator anlegen und die Informationen dort ablegen. Das Ergebnis sähe dann vergleichsweise so aus:  

```
Local lnHandle  
lnHandle = SQLConnect("MyBlog", "blog", "geheim")  
SQLExec(m.lnHandle, "Select count(\*) From posts", "posts")  
Browse Last  
```
  
Sofern die erstellte DSN unter dem Namen 'MyBlog' konfiguriert wurde.

Aktuelle Informationen, Tools und Downloads zu MySQL gibt es übrigens in deren [Entwicklersektion auf der Website](https://dev.mysql.com/).

Vielen Dank übrigens für die zahlreichen Feedbacks, Anregungen und Ideen im Laufe der vergangenen Monate. Ich hoffe, dass ich auch künftig weiter an der Tastatur bleiben werde und euch mit zahlreichen Tipps und Tricks dienen kann. Achja, neben diesem Blog gibt es übrigens noch zwei weitere, in denen ich weitaus unregelmäßiger Artikel publiziere:

[Coding for fun](https://weblogs.foxite.com/joki/) - engl. Blog  
[dFPUG Blog](https://blog.dfpug.de/JochenKirstaetter/)

Teilweise handelt es sich um artverwandte Artikel bzw. Verweise, teilweise um vollständig autarke Informationen, die hier nicht veröffentlicht werden. Eine bunte Mischung eben.  
Bis denne, JoKi