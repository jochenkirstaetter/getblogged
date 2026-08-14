---
uid: pathinfo-oder-wozu-gibt-es-eigentlich-rfcs
title: PATH_INFO oder wozu gibt es eigentlich RFCs?
slug: pathinfo-oder-wozu-gibt-es-eigentlich-rfcs
date: 2006-04-10
status: published
type: post
description: An manchen Tagen sollte man erst gar nicht mit dem Programmieren anfangen und einfach im Bett liegen bleiben. So auch heute.
tags:
- Development
keywords: Development
metaTitle: PATH_INFO oder wozu gibt es eigentlich RFCs?
metaDescription: An manchen Tagen sollte man erst gar nicht mit dem Programmieren anfangen und einfach im Bett liegen bleiben. So auch heute.
image: ''
ogTitle: PATH_INFO oder wozu gibt es eigentlich RFCs?
ogDescription: An manchen Tagen sollte man erst gar nicht mit dem Programmieren anfangen und einfach im Bett liegen bleiben. So auch heute. Nach etlichen Jahren holte mich heute aus ganz konspirativen Gründen die...
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
canonicalUrl: https://jochen.kirstaetter.name/pathinfo-oder-wozu-gibt-es-eigentlich-rfcs/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-10T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: An manchen Tagen sollte man erst gar nicht mit dem Programmieren anfangen und einfach im Bett liegen bleiben. So auch heute. Nach etlichen Jahren holte mich heute aus ganz konspirativen Gründen die...
twitterTitle: PATH_INFO oder wozu gibt es eigentlich RFCs?
twitterDescription: An manchen Tagen sollte man erst gar nicht mit dem Programmieren anfangen und einfach im Bett liegen bleiben. So auch heute. Nach etlichen Jahren holte mich heute aus ganz konspirativen Gründen die...
twitterImage: 
facebookTitle: PATH_INFO oder wozu gibt es eigentlich RFCs?
facebookDescription: An manchen Tagen sollte man erst gar nicht mit dem Programmieren anfangen und einfach im Bett liegen bleiben. So auch heute. Nach etlichen Jahren holte mich heute aus ganz konspirativen Gründen die...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
An manchen Tagen sollte man erst gar nicht mit dem Programmieren anfangen und einfach im Bett liegen bleiben. So auch heute. Nach etlichen Jahren holte mich heute aus ganz konspirativen Gründen die Vergangenheit ein. Da ich bereits seit 1996 dynamische Webseiten entwickle, kommt potentiell einiges an Wissen und Informationen - engl. Knowledge - zu bestimmten Themen im Bereich der Webentwicklung zusammen. Und eines hat mich dabei bestimmt mehr als einmal interessiert:

## Servervariablen
Sind extrem nützlich beim Schreiben von dynamischen Sites, die beispielsweise mit relativen Pfadangaben, Informationen zum Request und zum eigentlichen Webserver arbeiten sollen / müssen. Dabei bin ich immer mal wieder über die PATH\_INFO Variable gestolpert. Ich habe mich ehrlich gesagt nie sonderlich intensiv mit dieser speziellen Variablen beschäftigt, bis zum heutigen Tage...

## PATH_INFO allgemein
Ehrlich gesagt, fehlt mir aktuell die Information, was der eigentliche Auslöser war, dass ich mir diese Variable intensiver angeschaut habe. Ich würde aktuell mal drauf tippen, dass es mit dem DirectCall Plugin der Active FoxPro Pages begonnen hat. Das DirectCall ermöglicht es unter anderem, dass man die Objekte und Methoden seiner Webanwendung "direkt" aufrufen kann. Daher auch die Namensgebung. Nun, die zu verwendende URL sieht dabei ungefähr so aus:

[https://localhost/!application/object/method.afp](https://localhost/!application/object/method.afp)

Entscheidend hierbei ist das Ausrufezeichen zu Beginn des Skriptpfades. Und dabei kam die Idee, dass man ja prinzipiell auch Pfadinformationen nach der Skriptdatei nutzen kann. Das Ganze sieht dann exemplarisch so aus:

[https://localhost/script.afp/weiterer/Pfad/irgendwohin](https://localhost/script.afp/weiterer/Pfad/irgendwohin)

In beiden Fällen sind es gültige URLs. Wieso eigentlich der Aufwand?  
Nun, die Idee hinter diesem URL-Konstrukt ist, dass man suchmaschinenfreundliche Adressen produzieren kann \*ohne\* auf zusätzliche, serverspezifische Module wie mod\_rewrite zurück greifen zu müssen. Denn... und nun kommt der Trick an der Sache: Genau dafür gibt es die Servervariable PATH\_INFO.  
Zumindest in der Theorie...

## PATH_INFO - Ist-Zustand
Die Praxis bringt einen ganz schnell wieder auf den Boden der Tatsachen, denn weder der IIS noch der Apache über mod\_isapi bringen die korrekten Werte für die Variable. Mein Problem hat damit begonnen, dass der obige Aufruf mit zusätzlichem Pfad nach der Skriptdatei in Active FoxPro Pages zu einem HTTP 404 führte. Okay, wir haben ja Sourcen und können uns das mal anschauen... Nach einem einstündigem Skype-Talk mit meinem Kollegen Christof kamen wir dann auf den Punkt, dass ich ein AFP Plugin schreibe und mal genauer analysiere, was denn tatsächlich vom Webserver in PATH\_INFO und daran gekoppelt PATH\_TRANSLATED geschickt wird.

\*hüstel\* - Ich hätte es besser nicht machen sollen... Denn beide Server bringen, ehrlich gesagt, nicht den erwarteten Wert.

## PATH_INFO - Soll-Zustand
Nach ein paar Recherchen und Durchforsten von Bugreports im Bereich Perl und PHP, dann die [Analyse der RFC 3875 - The Common Gateway Interface (CGI) Version 1.1](https://www.ietf.org/rfc/rfc3875) und joah, es wird immer interessanter. Laut RFC 3875 definiert sich PATH\_INFO folgendermaßen (Kapitel 4.1.5):  
*The PATH\_INFO variable specifies a path to be interpreted by the CGI  
script. It identifies the resource or sub-resource to be returned by  
the CGI script, and is derived from the portion of the URI path  
hierarchy following the part that identifies the script itself.*  
Und gemäß der Darstellung in Kapitel 3.3 - The Script-URI:  
*The various  
components of the Script-URI are defined by some of the  
meta-variables (see below);*

*script-URI = &lt;scheme&gt; "://" &lt;server-name&gt; ":" &lt;server-port&gt;  
&lt;script-path&gt; &lt;extra-path&gt; "?" &lt;query-string&gt;*

*where &lt;scheme&gt; is found from SERVER\_PROTOCOL, &lt;server-name&gt;,  
&lt;server-port&gt; and &lt;query-string&gt; are the values of the respective  
meta-variables. The SCRIPT\_NAME and PATH\_INFO values, URL-encoded  
with ";", "=" and "?" reserved, give &lt;script-path&gt; and &lt;extra-path&gt;.*  
würde dies nach RFC bedeuten, dass im Normalfall PATH\_INFO und damit verbunden PATH\_TRANSLATED leer sind. Erst bei so obstrusen URLs wie etwa

[https://localhost/script.afp/weiterer/Pfad/irgendwohin](https://localhost/script.afp/weiterer/Pfad/irgendwohin)

würde sich die Servervariable mit dem Wert

/weiterer/Pfad/irgendwohin

füllen und dann wiederum vom Webserver durch die virtual-to-physical mappings auf einen korrespondierenden Wert in PATH\_TRANSLATED erweitert werden.

Tja, leider ist dem nicht so. Und ich glaube, dass bei der weiteren intensiven Beschäftigung mit der RFC 3875 weitere Ungereimtheiten ans Tageslicht kommen würden. Sowohl traurig wie auch spannend finde ich jedoch, dass selbst der Apache über Jahre nun diese Variable verkehrt füllt.

**Konsequenzen... **  
Nun, wenn es die Webserver nicht einheitlich korrekt gemäß RFC hinbekommen, dann gibt's nur zwei Möglichkeiten - die Segel streichen oder was dagegen unternehmen. Ich werde auf alle Fälle das AFP Plugin programmieren, da mich zum einen die suchmaschinenfreundlichen URLs ohne mod\_rewrite interessieren und zum anderen weil es nach RFC konform wäre, und damit weitere Tricks im Zusammenspiel mit der Entwicklung von dynamischen Websites bietet.

Und ich werde einen Bugreport für den IIS 7.0 einreichen. ;-)  
Schliesslich bin ich seit längerem Beta Tester für Windows Vista und Longhorn Server, also kann man dazu auch mal was Passendes melden.

## PathInfo Plugin
Netterweise kann man in den Active FoxPro Pages sehr einfach und schnell, neue Plugins einbinden und verwenden. Persönlich halte ich die Implementierung und Befüllung seitens der Webserver für nicht RFC-konform und damit leiden natürlich dann auch die Skriptsprachen, welche genutzt werden - egal, ob AFP, PHP, ASP.NET oder Sonstiges.  
Bis denne, JoKi