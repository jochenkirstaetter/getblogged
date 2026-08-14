---
uid: pathinfo-plugin-fr-afp
title: PathInfo Plugin für AFP
slug: pathinfo-plugin-fr-afp
date: 2006-04-11
status: published
type: post
description: Nachschlag... Ausgehend von meinem gestrigen Eintrag heute eine kleinere Ergänzung. Da mich die Thematik doch ein wenig heute Nacht beschäftigt hat, habe ich mal hingesetzt und ein Plugin für die...
tags:
- Development
keywords: Development
metaTitle: PathInfo Plugin für AFP
metaDescription: Nachschlag... Ausgehend von meinem gestrigen Eintrag heute eine kleinere Ergänzung. Da mich die Thematik doch ein wenig heute Nacht beschäftigt hat, habe ich mal hingesetzt und ein Plugin für die...
image: ''
ogTitle: PathInfo Plugin für AFP
ogDescription: Nachschlag... Ausgehend von meinem gestrigen Eintrag heute eine kleinere Ergänzung. Da mich die Thematik doch ein wenig heute Nacht beschäftigt hat, habe ich mal hingesetzt und ein Plugin für die...
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
canonicalUrl: https://jochen.kirstaetter.name/pathinfo-plugin-fr-afp/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-11T10:29:00Z
updatedAt: 2023-09-18T02:37:11Z
excerpt: Nachschlag... Ausgehend von meinem gestrigen Eintrag heute eine kleinere Ergänzung. Da mich die Thematik doch ein wenig heute Nacht beschäftigt hat, habe ich mal hingesetzt und ein Plugin für die...
twitterTitle: PathInfo Plugin für AFP
twitterDescription: Nachschlag... Ausgehend von meinem gestrigen Eintrag heute eine kleinere Ergänzung. Da mich die Thematik doch ein wenig heute Nacht beschäftigt hat, habe ich mal hingesetzt und ein Plugin für die...
twitterImage: 
facebookTitle: PathInfo Plugin für AFP
facebookDescription: Nachschlag... Ausgehend von meinem gestrigen Eintrag heute eine kleinere Ergänzung. Da mich die Thematik doch ein wenig heute Nacht beschäftigt hat, habe ich mal hingesetzt und ein Plugin für die...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Nachschlag...  
  
Ausgehend von meinem gestrigen Eintrag heute eine kleinere Ergänzung. Da mich die Thematik doch ein wenig heute Nacht beschäftigt hat, habe ich mal hingesetzt und ein Plugin für die Active FoxPro Pages programmiert. Denn, so wie es nach allem Anschein aussieht, scheint es sich hierbei um eine Limitierung seitens der ISAPI im Vergleich zu reellem CGI 1.1 zu sein. Laut Aussage in der MSDN zu ISAPI-Extension findet sich nämlich folgendes:  
  
*Path information, as given by the client, for example, "/vdir/myisapi.dll/zip". If this information comes from a URL, it is decoded by the server before it is passed to the CGI script or ISAPI filter.*  
  
*If the AllowPathInfoForScriptMappings metabase property is set to true (to support exclusive CGI functionality), PATH_INFO will only contain "/zip" and ISAPI applications such as ASP will break.*  
-- Quelle: [MSDN](https://web.archive.org/web/20060516125129/http://msdn.microsoft.com/library/?url=/library/en-us/iissdk/html/21b3be8f-d4ed-4059-8e21-6cba2c253006.asp?frame=true)  
  
Ohne Sichtung des Quellcode vom Apache mod_isapi gehe ich davon aus, dass es sich hierbei um das gleiche Verhalten handelt, nämlich dass eben ISAPIs nicht fehlschlagen.  
  
Da die AFP derzeit eben auch als ISAPI programmiert ist, wird mir wohl nichts anderes übrig bleiben, als die Situation anders zu lösen. Und dabei gibt es wiederum mehrere Lösungsmöglichkeiten; ich habe mich aktuell für die einfachste entschieden: Plugin erstellen.  
  
Gemäß den Vorgaben der AFP-Hilfe zur Puginerstellung geht das auch sehr schnell und einfach über die Tastatur. Kleine Orientierung im mitgelieferten Quellcode vom Voodoo Plugin und dem Beispielcode für das RuntimeExec Plugin und bunt zusammengewürfelt. Nach ein, zwei Stunden inklusive der Tests unter Apache und IIS kam dann folgendes dabei raus:  
  
## Code:
\*======================================================================  
* Executes AFP pages based on current PATH_INFO information of web server.  
* This plugin checks the URL and re-routes page execution based of the provided  
* path information. This behaviour is related to AcceptPathInfo directive of Apache web server  
* and AllowPathInfoForScriptMappings of IIS.  
* MSDN information: ms-help://MS.MSDNQTR.2006JAN.1033/iissdk/html/da14bb52-fb04-4e0b-a11b-a6035b5d65c9.htm  
* 
* This plugin parses PATH_INFO and PATH_TRANSLATED as described in RFC 3875:  
* http://www.ietf.org/rfc/rfc3875  
\*======================================================================  
LParameter roPlugIn  
roPlugIn = CreateObject("CPlugIn_PathInfo")  
  
\*======================================================================  
* CPlugIn_PathInfo  
\*======================================================================  
Define Class CPlugIn_PathInfo as CPlugin  
  
; &  
nbsp;cID = "PathInfo"  
oHook = NULL  
Procedure Load  
This.oHook = CreateObject("CHookPathInfo")  
This.oHook.Hook&#  
40;)  
EndProc  
Procedure Unload  
This.oHook.Unhook()  
This.oHook.Release()  
EndProc  
EndDefine  
  
\*======================================================================  
* CHookCallFactory objects are responsible to parse the request and return an appropriate  
* CCall object, if they want to handle a request.  
\*======================================================================  
Define Class CHookPathInfo as CHookCallFactory  
Procedure CreateCall  
LParameter toFile, tnLevel  
&nb;  
sp; Local lcApp, lcPage  
  
\*------------------------------------------------------------------  
* Get references to various AFP objects and store them in private variables. The  
* CreateObject() method only creates a new object, if the requested object has not  
* yet been loaded. Otherwise, a reference to the existing object is returned.  
* 
* NEVER store these references in properties. This might cause problems with AFP.  
\*------------------------------------------------------------------  
&nbs;  
p;Private REQUEST  
REQUEST = This.CreateObject("Request")  
  
Local lcPathInfo, lcPathTranslated, lcLocation, lcVirtualLocation  
m.lcPathInfo = Request.ServerVariables("PATH_INFO")  
m.lcPathTranslated = Request.ServerVariables("PATH_TRANSLATED")  
;  
  
&  
nbsp; m.lcPathInfo = StrExtract(m.lcPathInfo,".afp","",1,1+2)  
m.lcLocation = Strtran(m.lcPathTranslated, Chrtran(m.lcPathInfo, "/", "\"), "")  
&n;  
bsp; m.lcVirtualLocation = Strtran(toFile.cVirtualLocation, m.lcPathInfo, "")  
m.lcPathTranslated = JustPath(m.lcLocation) + Chrtran(m.lcPathInfo, "/", "\")  
If Empty(m.lcPathInfo)  
  
; &  
nbsp; m.lcPathTranslated = ""  
EndIf  
  
\*------------------------------------------------------------------  
* Correct PATH_* server variables and execute  
* requested script file.  
\*------------------------------------------------------------------  
Request.cData = Strtran( ;  
Request.cData, ;  
[PATH_INFO:] + Request.ServerVariables("PATH_INFO"), ;  
[PATH_INFO:] + m.lcPathInfo, ;  
1, 1, 2 ;  
)  
Request.cData = Strtran( ;  
Request.cData, ;  
[PATH_TRANSLATED:] + Request.ServerVariables("PATH_TRANSLATED"), ;  
[PATH_TRANSLATED:] + m.lcPathTranslated, ;  
1, 1, 2 ;  
)  
Request.Reset()  
  
toFile.Reset( ;  
m.lcLocation, ;  
m.lcVirtualLocation, ;  
toFile.cHost ;  
)  
Return DoDefault(m.toFile,m.tnLevel)  
EndProc  
  
EndDefine  
  
  
Die Klasse CPlugIn_PathInfo ist die konkretisierte Ableitung der AFP Pluginklasse und darin instanziieren wir die eigentliche Anpassung der ServerVariablen in der Klasse CHookPathInfo. Wir müssen wir über eine Factory gehen, da die Active FoxPro Pages intern eine Chain of Responsibility über alle Call-Prozesse aufbaut und auf diese Weise ermöglicht, dass multiple Plugins den ursprünglichen Request des Clients analysieren, modifizieren und verarbeiten können.  
  
Die Integration in die AFP erfolgt entweder per ControlCenter oder händisch über die Bearbeitung der afp.config:  
  
## Code:
&lt;plugin location="%root%\plugin\pathinfo.fxp" engine="AFP"/&gt;  
  
  
  
Zeile einfügen, speichern und AFP neu starten.  
  
Anbei übrigens auch ein ZIP-Archiv mit den benötigten Dateien:  
  
[http://jochen.kirstaetter.name/files/joki_PathInfo.plugin.zip](https://web.archive.org/web/20060516125129/http://jochen.kirstaetter.name/files/joki_PathInfo.plugin.zip)  
  
Das war's auch schon.  
  
  
Bis denne, JoKi