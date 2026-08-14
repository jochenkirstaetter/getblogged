---
uid: regular-expressions-in-vfp
title: Regular Expressions in VFP
slug: regular-expressions-in-vfp
date: 2006-04-22
status: published
type: post
description: Regular Expressions in VFP MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups.
tags:
- Development
keywords: Development
metaTitle: Regular Expressions in VFP
metaDescription: Regular Expressions in VFP MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups.
image: ''
ogTitle: Regular Expressions in VFP
ogDescription: MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at news://msnews.microsoft.com/microsoft.public.de.fox...
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
canonicalUrl: https://jochen.kirstaetter.name/regular-expressions-in-vfp/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-22T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at news://msnews.microsoft.com/microsoft.public.de.fox...
twitterTitle: Regular Expressions in VFP
twitterDescription: MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at news://msnews.microsoft.com/microsoft.public.de.fox...
twitterImage: 
facebookTitle: Regular Expressions in VFP
facebookDescription: MotivationBased on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at news://msnews.microsoft.com/microsoft.public.de.fox...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
**Motivation  
** Based on some research I did in december 2005 and currently refreshed due to a vital discussion in on of Microsoft's news groups at [news://msnews.microsoft.com/microsoft.public.de.fox](news://msnews.microsoft.com/microsoft.public.de.fox) (German) about the future of Visual FoxPro, I decided to finalize and deploy my **COM Proxy for .NET**. As you might guess the name of this component is its main purpose. It is a dynamic-link library that provides features of the .NET framework classes via COM to any *legacy* programming language like Visual FoxPro. Contrary to current Sedna CTP this component has the same interface for Regular Expressions as the VBScript object has. So, this way it is a lot easier to switch between different implementations.

## Setup and Installation
The component comes in two flavors - for .NET Framework 1.1 and 2.0. The setup routine installs both in separate folders and registers both in Windows. But no fear, the ProgID is the same for both, so it's again very handy for a VFP developer. Last registration of the component is the active one. I'd like to mention that the registration uses the /codebase switch of regasm tool and therefore creates no entries in to the Global Assembly Cache (GAC) on the machine. The current version of the setup is available at my German blog at the URL

[https://jochen.kirstaetter.name/files/ComProxyForNet.msi](xref:regular-expressions-in-vfp)

Just get the file and follow the installation instructions.

## Usage in Visual FoxPro
So, while the components are COM-based dynamic-link libraries usage in Visual FoxPro is done with its CreateObject() function. The returned object reference is an instance of .NET's Regex class.

RegEx = CreateObject("ProLib.RegEx")  
? RegEx.IsMatch("abc","w")

You can use any option and functionality of System.Text.RegularExpressions.Regex in Visual FoxPro now. Further information and details on this namespace are provided in the MSDN

Sincerely, JoKi