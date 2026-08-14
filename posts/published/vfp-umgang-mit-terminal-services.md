---
uid: vfp-umgang-mit-terminal-services
title: VFP Umgang mit Terminal Services
slug: vfp-umgang-mit-terminal-services
date: 2007-03-18
status: published
type: post
description: "VFP Umgang mit Terminal Services Zusammenfassung einer Antwort aus der Newsgruppe microsoft.public.de.fox:1. Wie kann das Programm feststellen, dass es in einer TS-Session l&#228;uft?Mittels der Os() Funktion kannst du das ermitteln. Siehe VFP-Hilfe:If Bittest(Val(Os(10)),4) Or Bittest(Val(Os(10)),8);;; ;*--- Running in TS environment...;;;;;Sys(602,0)EndIf2. Wie kann das Programm feststellen, wie der Client-Rechner heisst?GetEnv('CLIENTNAME')3: Da"
tags:
- Community
keywords: Community
metaTitle: VFP Umgang mit Terminal Services
metaDescription: "VFP Umgang mit Terminal Services Zusammenfassung einer Antwort aus der Newsgruppe microsoft.public.de.fox:1. Wie kann das Programm feststellen, dass es in einer TS-Session l&#228;uft?Mittels der Os() Funktion kannst du das ermitteln. Siehe VFP-Hilfe:If Bittest(Val(Os(10)),4) Or Bittest(Val(Os(10)),8);;; ;*--- Running in TS environment...;;;;;Sys(602,0)EndIf2. Wie kann das Programm feststellen, wie der Client-Rechner heisst?GetEnv('CLIENTNAME')3: Da"
image: ''
ogTitle: VFP Umgang mit Terminal Services
ogDescription: 'Zusammenfassung einer Antwort aus der Newsgruppe microsoft.public.de.fox:'
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
canonicalUrl: https://jochen.kirstaetter.name/vfp-umgang-mit-terminal-services/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2007-03-18T14:08:22Z
updatedAt: 2018-04-02T08:39:11Z
excerpt: 'Zusammenfassung einer Antwort aus der Newsgruppe microsoft.public.de.fox:'
twitterTitle: VFP Umgang mit Terminal Services
twitterDescription: 'Zusammenfassung einer Antwort aus der Newsgruppe microsoft.public.de.fox:'
twitterImage: 
facebookTitle: VFP Umgang mit Terminal Services
facebookDescription: 'Zusammenfassung einer Antwort aus der Newsgruppe microsoft.public.de.fox:'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Zusammenfassung einer Antwort aus der Newsgruppe [microsoft.public.de.fox](news://msnews.microsoft.com/microsoft.public.de.fox):

*1. Wie kann das Programm feststellen, dass es in einer TS-Session läuft?*

Mittels der Os() Funktion kannst du das ermitteln. Siehe VFP-Hilfe:

If Bittest(Val(Os(10)),4) Or Bittest(Val(Os(10)),8)  
\*--- Running in TS environment...  
Sys(602,0)  
EndIf

*2. Wie kann das Programm feststellen, wie der Client-Rechner heisst?*

GetEnv("CLIENTNAME")

*3: Da Drucker und ggf. auch Laufwerke (z.B. Memory-Stick für Datensicherung) des Clients mit verwendet werden, müssten Client-abhängige Konfigurations-Dateien (z.Z. gibt es nur ein INI-File im Applikationsverzeichnis) verwendet werden. Wo und wie speichere ich die am besten?*

Im Benutzerprofil - Home(7) zum Beispiel oder GetEnv("LocalAppData") bzw. GetEnv("AppData"). Außerdem kannst du die WIN32 API Funktion SHGetFolderPath verwenden:

#DEFINE CSIDL_MYDOCUMENTS 0x000c  
#DEFINE CSIDL_LOCAL_APPDATA 0x001c

DECLARE SHORT SHGetFolderPath IN shell32;  
INTEGER hwndOwner,;  
INTEGER nFolder,;  
INTEGER hToken,;  
INTEGER dwFlags,;  
STRING @ pszPath

LOCAL lcBuffer  
lcBuffer = REPLICATE(CHR(0),254)  
IF SHGetFolderPath(0, CSIDL_MYDOCUMENTS, 0, 0, @lcBuffer) = 0  
? LEFT(lcBuffer,AT(CHR(0),lcBuffer)-1)  
ENDIF

Weitere Konstanten für Ordner (CSIDL_\*) findest du in der MSDN:

[https://msdn.microsoft.com/library/default.asp?url=/library/en-us/shellcc/platform/shell/reference/enums/csidl.asp](https://msdn.microsoft.com/library/default.asp?url=/library/en-us/shellcc/platform/shell/reference/enums/csidl.asp)  
(eine Zeile!)

*4: Ich habe grad mal per TS-Session als Administrator eine Anwendungs-Installation auf dem Win2003-Server gemacht. Dabei ist mir aufgefallen, dass die Dateien, die normalerweise in WINDOWSSYSTEM32 installiert werden (msvcr71.dll usw.) jetzt in's Verzeichnis Dokumente und EinstellungenAdministratorWINDOWS gekommen sind und somit nicht für die anderen User zur Verfügung stehen. Wie lässt sich das umgehen?*

Hast du den TS-Installmodus vorher aktiviert? Das geht entweder 'automatisch' über den visuellen Weg über Systemsteuerung : Software oder per Prompt:

CHANGE USER /INSTALL  
Enable install mode. This command has to be run before  
installing any new software on a Terminal Server.  
This will create a .ini file for the application  
in the TS system directory.

CHANGE USER /EXECUTE  
Enable execute mode (default)  
Run this when an installation is complete.

CHANGE USER /QUERY  
Display current settings.

Außerdem findest du hier eine nette Zusammenstellung an Fragen und Antworten zum Thema Terminal Services:

[https://www.microsoft.com/technet/community/en-us/terminal/terminal_faq.mspx](https://www.microsoft.com/technet/community/en-us/terminal/terminal_faq.mspx)

Ich hoffe, dass dies einige Tipps fuer euch lieferte...

Bis denne, JoKi