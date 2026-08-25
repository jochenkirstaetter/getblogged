---
uid: comproxy
title: COM Proxy for .NET
date: 2009-12-14
status: published
type: post
description: COM Proxy for .NET COM Proxy for .NET MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at news://msnews.microsoft.com/microsoft.public.de.fox (German) about the future of Visual FoxPro, I decided to finalize and deploy my COM Proxy for
tags:
- Projects
keywords: Projects
metaTitle: COM Proxy for .NET
metaDescription: COM Proxy for .NET COM Proxy for .NET MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at news://msnews.microsoft.com/microsoft.public.de.fox (German) about the future of Visual FoxPro, I decided to finalize and deploy my COM Proxy for
image: ''
ogTitle: COM Proxy for .NET
ogDescription: COM Proxy for .NET MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at...
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
canonicalUrl: https://jochen.kirstaetter.name/comproxy/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2009-12-14T08:59:37Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: COM Proxy for .NET MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at...
twitterTitle: COM Proxy for .NET
twitterDescription: COM Proxy for .NET MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at...
twitterImage: 
facebookTitle: COM Proxy for .NET
facebookDescription: COM Proxy for .NET MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
## COM Proxy for .NET

**Motivation  
** Based on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at [news://msnews.microsoft.com/microsoft.public.de.fox](news://msnews.microsoft.com/microsoft.public.de.fox) (German) about the future of Visual FoxPro, I decided to finalize and deploy my **COM Proxy for .NET**. As you might guess the name of this component is its main purpose. It is a dynamic-link library that provides features of the .NET framework classes via COM to any *legacy* programming language like Visual FoxPro. Contrary to current Sedna CTP this component has the same interface for Regular Expressions as the VBScript object has. So, this way it is a lot easier to switch between different implementations.

## Setup and Installation
The component comes in two flavors - for .NET Framework 1.1 and 2.0. The setup routine installs both in separate folders and registers both in Windows. But no fear, the ProgID is the same for both, so it's again very handy for a VFP developer. Last registration of the component is the active one. I'd like to mention that the registration uses the /codebase switch of regasm tool and therefore creates no entries in to the Global Assembly Cache (GAC) on the machine. The current version of the setup is available at my German blog at the URL

[https://jochen.kirstaetter.name/files/ComProxyForNet.msi](https://jochen.kirstaetter.name/files/ComProxyForNet.msi)

Just get the file and follow the installation instructions.

## Usage in Visual FoxPro
So, while the components are COM-based dynamic-link libraries usage in Visual FoxPro is done with its CreateObject() function. The returned object reference is an instance of .NET's Regex class.

<font face="Courier New">RegEx = CreateObject("ProLib.RegEx")  
? RegEx.IsMatch("abc","\w")</font>

You can use any option and functionality of System.Text.RegularExpressions.Regex in Visual FoxPro now. Further information and details on this namespace are provided in the MSDN