---
uid: ctp-fr-sedna-und-visual-foxpro-90-sp2
title: CTP für Sedna und Visual FoxPro 9.0 SP2
slug: ctp-fr-sedna-und-visual-foxpro-90-sp2
date: 2006-10-14
status: published
type: post
description: CTP für Sedna und Visual FoxPro 9.0 SP2 Das solche Neuigkeiten immer kurz vor dem Wochenende kommen müssen. Tss, da ist man gedanklich schon auf Entspannung und dann wird man von Microsoft mit neuen Gimmicks versorgt. Ausgelöst durch einen RSS Feed auf andere Blogs habe ich erfahren, dass sowohl ein
tags:
- Community
keywords: Community
metaTitle: CTP für Sedna und Visual FoxPro 9.0 SP2
metaDescription: CTP für Sedna und Visual FoxPro 9.0 SP2 Das solche Neuigkeiten immer kurz vor dem Wochenende kommen müssen. Tss, da ist man gedanklich schon auf Entspannung und dann wird man von Microsoft mit neuen Gimmicks versorgt. Ausgelöst durch einen RSS Feed auf andere Blogs habe ich erfahren, dass sowohl ein
image: ''
ogTitle: CTP für Sedna und Visual FoxPro 9.0 SP2
ogDescription: Das solche Neuigkeiten immer kurz vor dem Wochenende kommen müssen. Tss, da ist man gedanklich schon auf Entspannung und dann wird man von Microsoft mit neuen Gimmicks versorgt. Ausgelöst durch einen...
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
canonicalUrl: https://jochen.kirstaetter.name/ctp-fr-sedna-und-visual-foxpro-90-sp2/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-10-14T11:42:40Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Das solche Neuigkeiten immer kurz vor dem Wochenende kommen müssen. Tss, da ist man gedanklich schon auf Entspannung und dann wird man von Microsoft mit neuen Gimmicks versorgt. Ausgelöst durch einen...
twitterTitle: CTP für Sedna und Visual FoxPro 9.0 SP2
twitterDescription: Das solche Neuigkeiten immer kurz vor dem Wochenende kommen müssen. Tss, da ist man gedanklich schon auf Entspannung und dann wird man von Microsoft mit neuen Gimmicks versorgt. Ausgelöst durch einen...
twitterImage: 
facebookTitle: CTP für Sedna und Visual FoxPro 9.0 SP2
facebookDescription: Das solche Neuigkeiten immer kurz vor dem Wochenende kommen müssen. Tss, da ist man gedanklich schon auf Entspannung und dann wird man von Microsoft mit neuen Gimmicks versorgt. Ausgelöst durch einen...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Das solche Neuigkeiten immer kurz vor dem Wochenende kommen müssen. Tss, da ist man gedanklich schon auf Entspannung und dann wird man von [Microsoft mit neuen Gimmicks](https://msdn.microsoft.com/vfoxpro/letters/) versorgt. Ausgelöst durch einen RSS Feed auf andere Blogs habe ich erfahren, dass sowohl ein neuer [Community Techology Preview (CTP) für Sedna wie auch für das kommende Service Pack 2](https://www.microsoft.com/downloads/details.aspx?FamilyId=808E96E1-3D87-421F-9BA5-4AAFE70C7B21&displaylang=en) für Visual FoxPro 9.0 veröffentlicht wurden.

\*\*Sedna und NET4COM\*\*  
Fein, gerade in Bezug auf NET4COM interessiert mich natürlich die Fassung für meine [Session auf der diesjährigen Entwicklerkonferenz](https://devcon.dfpug.de). Inzwischen ist das .NET Framework 2.0 als Grundlage für NET4COM rangezogen worden. Die Beispiele in Visual FoxPro wurden ergänzt und es gibt eine entsprechende FoxPro Foundation Class (FFC) für die einfache Nutzung des COM-Servers. Aktuell habe ich mir die Details noch nicht angeschaut, aber das wird noch passieren. Hm, zusätzlich muss ich nun auch meine Sessionnotizen überarbeiten und aktualisieren... Danke... 😁

\*\*Service Pack 2\*\*  
Herrje, vor dem Vergnügen zuerst die Arbeit - anders kann man die Installationsorgie bedingt durch den Microsoft Windows Installer nicht bezeichnen. Aber hey, ich bin doch selbst schuld. Wie kann man auf die Idee kommen und keine Standardpfade zu verwenden. Ist ja schon eine Frechheit, dass man lokale VFP Installation von einem Netzwerk ausgehend installiert wurde. Nunja, da ich nicht in der Firma bin, klappt das Update auf SP2 schon mal prinzipiell nicht. Okay, kein Thema nehmen wir die DVD aus dem MSDN-Package und korrigieren den Installationspfad beim Update... No chance! Gut, passen wir die Pfadinfos in der Registry an und probieren es erneut. Schon besser, aber bei der Aufforderung zur Einlage der 'Disk 1' hört der Spass auf.

Na gut, dann eben komplette Deinstallation von VFP 9.0, Reboot, dann frische blanke Installation von VFP 9.0 - wow, erneuter Reboot durch WCUs - und nun endlich zeigt sich auch das Update auf SP2 kooperativ. Es kann eventuell daran gelegen haben, dass das Update SP2 ein frisches VFP 9.0 - also ohne SP1 - erfordert... who knows. Ich werde meine Erkenntnisse zunächst noch an das Supportcenter, dass es bei der Final einfachen wird.

Die neue Versionsnummer lautet übrigens: \*\*Visual FoxPro 09.00.0000.4611 for Windows\*\*

Und interessanterweise bzw. auch stillschweigend wurde der OLE DB Provider für Visual FoxPro 9.0 ebenfalls aktualisiert, was aber bisher nirgends dokumentiert ist. Und der OLE DB Provider eigentlich separat vom Hauptprodukt als Download angeboten wird. Verschleierungstaktik von Microsoft?

\*\*Aktualisierter RuntimeInstaller\*\*  
Als langjährigen Service bietet ProLib die entsprechenden Runtimeinstaller für die Auslieferung von VFP-Anwendungen beim Kunden kostenfrei an. Damit braucht man sich selbst keine Gedanken mehr über Dateien und Registrierungen und so machen. Laufen lassen, Einstellungen setzen und wohlfühlen. Unsere Installer können übrigens auch in eigene Setups integriert werden.  
Viel Spass mit dem CTP des Service Pack 2 für VFP 9.0, JoKi
