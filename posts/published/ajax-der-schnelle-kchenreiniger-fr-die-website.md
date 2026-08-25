---
uid: ajax-der-schnelle-kchenreiniger-fr-die-website
title: AJaX - der schnelle Küchenreiniger für die Website
date: 2006-01-26
status: published
type: post
description: Zumindest war das mein erster Gedanke nachdem ich von einem Kollegen einen Überblick über Asynchronous JavaScript and XML (AJaX) vermittelt bekomme habe.
tags:
- Development
keywords: Development
metaTitle: AJaX - der schnelle Küchenreiniger für die Website
metaDescription: Zumindest war das mein erster Gedanke nachdem ich von einem Kollegen einen Überblick über Asynchronous JavaScript and XML (AJaX) vermittelt bekomme habe.
image: ''
ogTitle: AJaX - der schnelle Küchenreiniger für die Website
ogDescription: Zumindest war das mein erster Gedanke nachdem ich von einem Kollegen einen Überblick über Asynchronous JavaScript and XML (AJaX) vermittelt bekomme habe. Der aktuelle Hype um diesen...
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
canonicalUrl: https://jochen.kirstaetter.name/ajax-der-schnelle-kchenreiniger-fr-die-website/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-01-26T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: Zumindest war das mein erster Gedanke nachdem ich von einem Kollegen einen Überblick über Asynchronous JavaScript and XML (AJaX) vermittelt bekomme habe. Der aktuelle Hype um diesen...
twitterTitle: AJaX - der schnelle Küchenreiniger für die Website
twitterDescription: Zumindest war das mein erster Gedanke nachdem ich von einem Kollegen einen Überblick über Asynchronous JavaScript and XML (AJaX) vermittelt bekomme habe. Der aktuelle Hype um diesen...
twitterImage: 
facebookTitle: AJaX - der schnelle Küchenreiniger für die Website
facebookDescription: Zumindest war das mein erster Gedanke nachdem ich von einem Kollegen einen Überblick über Asynchronous JavaScript and XML (AJaX) vermittelt bekomme habe. Der aktuelle Hype um diesen...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Zumindest war das mein erster Gedanke nachdem ich von einem Kollegen einen Überblick über [Asynchronous JavaScript and XML](https://de.wikipedia.org/wiki/AJaX) (AJaX) vermittelt bekomme habe. Der aktuelle Hype um diesen Kommunikationsansatz zwischen Client (in Form des Browsers) und Server (beliebiger Webserver) scheint mir auf alle Fälle mal wieder ziemlich aufgeblasen. Wenn man bedenkt, dass AJaX eigentlich schon seit 1998 Bestand in der Webentwicklung hat, nunja, Guten Morgen Webentwickler!

Microsoft stellte in Verbindung mit dem Outlook Web Access (OWA) die Kombination von JScript/VBScript und HTML/XML erstmalig vor. Die Verbreitung dieses wirklich coolen Arbeitsumfeldes wurde jedoch bedingt durch die eingesetzte ActiveX-Technologie, der Reduzierung auf die Windowsplattform und damit dem Internet Explorer, sowie den fast täglichen Schlagzeilen zu Sicherheitslücken bei ActiveX-Komponenten in Webseiten extremst in den Hintergrund gedrängt. Wirklich schade...

Der Dreh- und Angelpunkt bei AJaX ist ein clientseitiges Objekt, welches im Hintergrund die Kommunikation mit dem Webserver managen kann, ohne dass durch die abgesetzten Requests und Responses die komplette Webseite neu im Browser aufgebaut werden muss. Mittels Frames kann man zumindest annähernd einen vergleichbaren Effekt erzeugen, da hier nur Teile der optischen Darstellung erneut geladen werden. Und um den Bogen zurück zu ActiveX-Control hinzubekommen, wird für diese Kommunikation ein XMLHttpRequest-Objekt instanziert und genutzt. Und damit erschliesst sich auch das Problem der Vergangenheit: Nur der IE stellte dieses Objekt zur Verfügung.

Inzwischen sprach sich auch bei den anderen Browserherstellern herum, dass dieses XMLHttpReqeust-Objekt für die coolen Aktionen innerhalb einer HTML-Seite einen großen Vorteil darstellt. Somit es gegenwärtig problemlos möglich mit den gängigen Browsern AJaX-Lösungen zu programmieren.

Aber warum sollte man überhaupt AJaX für die Webentwicklung verwenden? Gute Frage, die ich mit einem kleinen Beispiel anführen möchte. Nehmen wir folgende Situation / Aufbau für eine HTML-Darstellung an: Eine zweigeteilte Website mit einer Liste aller Kunden auf der linken Seite und den Detailinformationen des selektierten Kunden in mehreren Controls auf der rechten Seite. An für sich keine schwierige Anforderung und ebenfalls ein geläufiger Aufbau in Desktopanwendungen.

Durch die verbindungslose Kommunikation zwischen Client und Server stehen wir nun vor dem Problem, was eigentlich passiert, wenn der Kunde in der Auswahlliste geändert wird. Im klassischen Sinne würde dies bedeuten, dass ein Request an den Webserver abgesetzt wird und anschliessend die Seite neu aufgebaut wird, da sich die anzuzeigenden Informationen im Detailbereich geändert haben. Naja, nicht gerade prickelnd, wenn man bedenkt, dass vielleicht nur 5% der visuellen Darstellung zu ändern sind. Die Alternative könnte darin bestehen, dass bereits beim ersten Aufruf der Kundenliste alle Detailinformationen geliefert werden. Nunja, bei einer geringen Anzahl macht das vielleicht noch Spass, aber je mehr Kunden vorliegen desto länger dauert der Aufbau. Ein Zugriff über eine schmale Leitung wird hierbei für eine Kaffeepause sorgen. Und genau hier bietet AJaX die geschickteste Lösung.

Nehmen wir wieder unsere Kundenliste her. Alle Einträge haben im Normalfall einen eindeutigen Identifier - den sogenannten Primärschlüssel. Durch den Einsatz des XMLHttpRequest-Objekt, einer speziellen Seite auf dem Webserver und dem Primärschlüssel des gewählten Kunden sind wir in der Lage die Detailinformationen en demand abzurufen und weiter zu verarbeiten. Über das XMLHttpRequest-Objekt setzen wir einen asynchronen Request auf den Webserver ab, welcher uns die Detaildaten des Kunden beispielsweise in XML zurücksendet. Die komplette Verarbeitung erfolgt clientseitig mittels JavaScript. Und damit wäre die Namensgebung für AJaX erklärt. 😁  
**Kurzfassung:** Anstelle eines Anchor lösen wir eine Funktionalität in JavaScript aus, die das Ergebnis in die bestehende HTML-Seite einarbeitet.

Genug der trockenen Theorie schauen wir uns die Sache mal in der Praxis an. Zunächst einmal die fertige HTML-Seite mit der Kundenliste und den Detaildaten des selektierten Kunden. Für die Aktualisierung als Reaktion auf den Wechsel des Kunden nutzen wir die Ereignisverarbeitung von JavaScript. Die Liste bietet uns ein Ereignis onchange() an, und hieran binden wir uns, um unsere eigene Routine laufen zu lassen.

Zum Absetzen des Request benötigen wir erst eine gültige Instanz eines XMLHttpRequest-Objekt. Wir berücksichtigen hierbei gleich die unterschiedlichen Implementierungen der Browser und erzeugen eine generische Methode, die das Objekt für die weitere Ausführung liefert.  

```
function getXmlHttp()  
{  
// Internet Explorer  
try {  
xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");  
} catch(e) {  
try {  
xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");  
} catch(e) {  
xmlHttp = false;  
}  
}  
// Mozilla, Opera und Safari  
if (!xmlHttp && typeof XMLHttpRequest != 'undefined') {  
xmlHttp = new XMLHttpRequest();  
}  
return xmlHttp;  
}  
```


Unserem gerade erzeugten Request-Objekt geben wir die URL und die Parameter zum Abruf der Details. Auch hier bietet es sich an, gleich zu Beginn eine generische Routine zu schreiben, welche in beliebigen Kontexten genutzt werden kann.  

```
function getXmlResponse(cMethod, cParameter)  
{  
var xmlHttp = getXmlHttp();  
if (xmlHttp) {  
xmlHttp.open('GET',  
'ajax.afp?action=' + cMethod +  
'&parameter=' + cParameter,  
true);  
xmlHttp.onreadystatechange = function () {  
if (xmlHttp.readyState == 4) {  
var tooltipcaption = findDOM("tooltipcaption");  
var tooltiptext = findDOM("tooltiptext");  
if(tooltipcaption)  
{  
tooltipcaption.innerHTML = cParameter;  
tooltiptext.innerHTML = xmlHttp.responseText;  
settip('tooltip');  
}  
}  
};  
xmlHttp.send(null);  
}  
}  
```


Abschliessend verarbeiten wir die Antwort des Webservers und verteilen die einzelnen Informationen auf die sichtbaren HTML-Controls. Damit haben wir die visuelle Darstellung der Kundendaten durch den Wechsel des Kunden in der Auswahlliste vollständig realisiert, ohne dass dazu die Seite neu aufgebaut werden musste.

Durch die asynchrone Natur unseres Request/Response-Paares kommt die Aktualisierung leicht verzögert. Ein Umstand den man aber sicherlich gerne im Vergleich zum Komplettaufbau in Kauf nimmt, und einem Auftraggeber erläutern kann.

Das war's für den Einstieg in die Welt der asynchronen Kommunikation mit JavaScript und XML. Und bitte lasst den Haushaltsreiniger unter der Spüle stehen. Der könnte eurem Rechner lediglich schaden denn nutzen.  
Bis denne, JoKi