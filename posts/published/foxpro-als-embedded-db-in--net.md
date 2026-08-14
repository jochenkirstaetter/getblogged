---
uid: foxpro-als-embedded-db-in--net
title: FoxPro als embedded DB in .NET
slug: foxpro-als-embedded-db-in--net
date: 2006-03-23
status: published
type: post
description: FoxPro als embedded DB in .NET Hallo,ein wenig sp&#228;t, aber ich w&#252;rde hier gerne ein paar Ungenauigkeiten klarstellen wollen.*Original von Quest*Ich w&#252;rde gerne FoxPro statt Access als DB nutzen, welches ich mit meiner Anwendung gleich mitinstalliere...Hat zur Nutzung von FoxPro mit C# evtl. jemand eine gute Seite die auf ein
tags:
- Development
keywords: Development
metaTitle: FoxPro als embedded DB in .NET
metaDescription: FoxPro als embedded DB in .NET Hallo,ein wenig sp&#228;t, aber ich w&#252;rde hier gerne ein paar Ungenauigkeiten klarstellen wollen.*Original von Quest*Ich w&#252;rde gerne FoxPro statt Access als DB nutzen, welches ich mit meiner Anwendung gleich mitinstalliere...Hat zur Nutzung von FoxPro mit C# evtl. jemand eine gute Seite die auf ein
image: ''
ogTitle: FoxPro als embedded DB in .NET
ogDescription: Hallo,
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
canonicalUrl: https://jochen.kirstaetter.name/foxpro-als-embedded-db-in--net/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-03-23T11:43:59Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Hallo,
twitterTitle: FoxPro als embedded DB in .NET
twitterDescription: Hallo,
twitterImage: 
facebookTitle: FoxPro als embedded DB in .NET
facebookDescription: Hallo,
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Hallo,

ein wenig spät, aber ich würde hier gerne ein paar Ungenauigkeiten klarstellen wollen.


> \*Original von Quest\*  
> Ich würde gerne FoxPro statt Access als DB nutzen, welches ich mit meiner Anwendung gleich mitinstalliere...  
> Hat zur Nutzung von FoxPro mit C# evtl. jemand eine gute Seite die auf ein paar Sachen tiefer eingeht? Interessieren würde mich v.a. Multiuser-Zugriff, Triggers, Views, Stored Proecdures, etc...
  
VFP anstelle von Access zu verwenden, ist auf alle Fälle schon eine interessante Variante. Entsprechendes lässt sich auch der FAQ zu VFP bei Microsoft nachlesen: [https://msdn.com/vfoxpro/](https://msdn.com/vfoxpro/)


> Ach ja und was ich noch fragen wollte: Der Kern des Ganzen ist kostenlos und für Visual FoxPro muss ich pro Lizenz zahlen? Hab ich das richtig verstanden? Naja aber durchs MSDN-Abo hab ich schonmal eine Lizenz hier... :D
  
Du musst lediglich für eine Entwicklungsumgebung bezahlen. Der weitere Vertrieb deiner Anwendung ist dir überlassen. Weiterhin möchte ich hierzu sagen, dass der Ole DB Provider für VFP ebenfalls online frei verfügbar ist und du damit eigentlich alles hast, um VFP als Datenbank zu verwenden.

In meinem Blog findest du übrigens ein fertiges Beispiel mit allem Drum und Dran. Sogar die Erstellung der Datenbank mit den Tabellen kannst über ADOX und ADO.NET erledigen.

So, damit wäre deine initiale Frage beantwortet, schauen wir uns die weiteren Statements an und kommentieren das ein wenig...


> \*Original von citizen.ron\*  
> keine lizenzprobleme und gehen tut mehr als foxpro sich je träumen lassen wird
  
Welche Lizenzprobleme hat man denn mit VFP? Genau das ist doch der Haken, dass Microsoft das Produkt in den letzten Jahren sehr stiefmütterlich betrachtet hat. Und gerade in Bezug auf Verwendung mit ADO.NET ist es erst recht kostenfrei: [https://msdn.com/vfoxpro/](https://msdn.com/vfoxpro/) dort gibt's den Ole DB Provider und das war's dann auch schon. Mehr ist nicht notwendig.


> \*Original von Der Eisbär\*  
> Vor allem würde ich nicht mehr auf eine Datenbank setzen, die nicht mehr weiterentwickelt wird ...
> 
> Ansonsten sehe ich das wie citizen.ron ... die Hochzeit von VFP ist vorbei (habe selbst beruflich VFP entwickelt, weiß also durchaus, wovon ich rede ;-)) und der SQL Server kann definitiv deutlich mehr als VFP jemals kann.


Zunächst einmal ist VFP ein Produkt, welches seit annähernd 20 Jahren besteht und damit die entsprechende Reife aufzuweisen vermag. Der Produktsupport seitens Microsoft läuft irgendwann 2014 aus. Bis dahin läuft sehr viel Wasser den Rhein hinunter. Weiterhin finde ich es übrigens sehr spannend, dass gerade die Entwicklung von LINQ speziell auf die Features von VFP eingeht und sich daran orientieren wird. Oder wie erklärst du die Integration von Rushmore in .NET 3.0?

Über deine Kenntnisse in Bezug auf VFP möchte hier nicht weiteres zum Besten geben, außer dass du kaum mit der eigentlichen Datenbank in Kontakt gekommen bist, da wir im Projekt primär mit dem MS SQL Server (bedingt durch Anforderung des Kunden) arbeiten. Ergo, bezieht sich dein "Wissen" primär auf die Programmiersprache denn auf die Datenbank.


> \*Original von Der Eisbär\*  
> VFP ist IMHO unter anderem deshalb schon aus dem Rennen, weil es nicht mehr weiterentwickelt wird.


Wo bitte steht dieses Statement? Microsoft hat keine Aussage dazu getroffen. Es wird derzeit an Sedna programmiert, welches als Addon zu VFP 9.0 derzeit angesehen wird. Ob daraus VFP 10 wird oder nicht, entscheidet sich frühestens Mitte/Ende 2007.


> \*Original von Der Eisbär\*  
> Aus VFP kannst Du derzeit mehr schlecht als recht auf .NET zugreifen. Das ändert sich mit Sedna, da Sedna als Integrationsschicht zu verstehen ist.
> 
> In diesem Sinne sehe ich für VFP-Entwickler keinen Sinn, mit Sedna auf .NET zuzugreifen, da der Overhead massivst ist und man ja doch das .NET Framework benötigt.


Und was hat das mit der Frage in Bezug auf die reine VFP-Datenbank zu tun? Ehrlich gesagt, sehe ich hier das Dilemma, dass du VFP immer als Ganzes betrachtest und entsprechend bewertest. Aber eigentlich entspricht VFP 3 Produkten: Programmiersprache, Datenbank und Reportsystem. Was meinst du wie glücklich irgendwelche Office-Anwender sind, wenn man denen einen VFP-COM-Server zur Verfügung stellt, so dass sie stressfrei im Vergleich zu ADO auf ihre Datenquellen kommen...

Achja, der Zugriff auf .NET funktioniert genauso wie bei anderen Nicht-.NET-Sprachen: per COM und das klappt gut. Selbst WinForms lassen sich per COM starten und nutzen.

So, Schnitt. Der Beitrag kommt wahrscheinlich ziemlich spät, aber ändert nichts an den Kommentaren. Ich möchte hier keine Lanze für VFP als lokale DB-Engine für .NET brechen, sondern es kommt auf die jeweiligen Anforderungen an das System an. Sicherlich lässt sich das gleiche Problem auch mit SQLite, Firebird und anderen RDBMS lösen.

Als VFP-Coder tendiere ich selbstredend für VFP als Datenbank, schliesslich sind wir alle subjektiv in unseren Aussagen.  
Bis denne, JoKi