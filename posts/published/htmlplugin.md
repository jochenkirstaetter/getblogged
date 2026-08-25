---
uid: htmlplugin
title: HTML Plugin for Active FoxPro Pages
date: 2009-12-14
status: published
type: post
description: HTML Plugin for Active FoxPro Pages HTML Plugin for Active FoxPro Pages MotivationHtml Plugin is primarily a plug-in for Active FoxPro Pages. But that's only half the truth. The plug-in itself is build as a component and offers stand-alone functionality for VFP developers and through COM as well for other
tags:
- Projects
keywords: Projects
metaTitle: HTML Plugin for Active FoxPro Pages
metaDescription: HTML Plugin for Active FoxPro Pages HTML Plugin for Active FoxPro Pages MotivationHtml Plugin is primarily a plug-in for Active FoxPro Pages. But that's only half the truth. The plug-in itself is build as a component and offers stand-alone functionality for VFP developers and through COM as well for other
image: ''
ogTitle: HTML Plugin for Active FoxPro Pages
ogDescription: HTML Plugin for Active FoxPro Pages MotivationHtml Plugin is primarily a plug-in for Active FoxPro Pages. But that's only half the truth. The plug-in itself is build as a component and offers...
layout: post
bodyClass: post-template tag-projects
postClass: post tag-projects
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
canonicalUrl: https://jochen.kirstaetter.name/htmlplugin/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2009-12-14T09:00:39Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: HTML Plugin for Active FoxPro Pages MotivationHtml Plugin is primarily a plug-in for Active FoxPro Pages. But that's only half the truth. The plug-in itself is build as a component and offers...
twitterTitle: HTML Plugin for Active FoxPro Pages
twitterDescription: HTML Plugin for Active FoxPro Pages MotivationHtml Plugin is primarily a plug-in for Active FoxPro Pages. But that's only half the truth. The plug-in itself is build as a component and offers...
twitterImage: 
facebookTitle: HTML Plugin for Active FoxPro Pages
facebookDescription: HTML Plugin for Active FoxPro Pages MotivationHtml Plugin is primarily a plug-in for Active FoxPro Pages. But that's only half the truth. The plug-in itself is build as a component and offers...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
## HTML Plugin for Active FoxPro Pages

## Motivation
Html Plugin is primarily a plug-in for [Active FoxPro Pages](https://www.afpages.com/). But that's only half the truth. The plug-in itself is build as a component and offers stand-alone functionality for VFP developers and through COM as well for other programming languages.

## Setup and Installation
The setup routine installs and registers the component in Windows. The current version of the setup is available here:

[https://jochen.kirstaetter.name/files/html.plugin-0.7.16.exe](xref:htmlplugin)

Just get the file and follow the installation instructions.

## Usage in Visual FoxPro
In VFP you just create an object like so:

<font face="Courier New">Set Procedure To "html.plugin.dll" Additive  
Html = CreateObject("CHTML")</font>

If you have to use COM instead, then this works just fine:

<font face="Courier New">Html = CreateObject("AFPPlugin.Html")</font>

It was quite funny to get this component working in .NET Framework and I'm still working on this topic, but at the moment I got it to create my own namespace (tree) based on this single DLL. After you added a reference to the COM server, you'll have an new namespace tree instead of just one plain entry: ProLib.AFP3.Plugin.Html and due to COM interoperability in .NET the instance name of the class is simple HtmlClass.

I wrote a sample solution that's able to convert an RSS Feed to a .NET DataSet through the Html Plugin. Well, not too hard to implement in pure .NET but the fact is, that the plug-in provides the same functionality to VFP developers.

And Html Plugin is a core part of AfpWiki - a Wiki engine on top of [Active FoxPro Pages](https://www.afpages.com/). Actually the Html Plugin does all the stuff related to Regular Expressions. It's really nice to see that just one line of code parses all hyperlinks of the entire document and converts them into clickable links with 'title' attribute and protocol indicator. There is still a lot of work to do inside of AfpWiki, like backup and restore of the database, online upgrade mechanism as well as an abstraction layer to user authentication and management, but this will be implemented during a couple of weeks. You might check out [https://faq.dfpug.de](https://faq.dfpug.de/) to see the system in action.

Ah, before I forget to mention Html Plugin and AfpWiki are both available for free (as in beer *g*). So, if anyone of you is interested in a Wiki solution just drop me a note.