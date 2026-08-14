---
uid: software-development-stack
title: Software development stack 2012
slug: software-development-stack
date: 2012-08-13
status: published
type: post
description: Brief description of the current software development stack / set of tools at IOS Indian Ocean Software Ltd.
tags:
- Development
keywords: Development
metaTitle: Software development stack 2012
metaDescription: Brief description of the current software development stack / set of tools at IOS Indian Ocean Software Ltd.
image: ''
ogTitle: Software development stack 2012
ogDescription: A couple of months ago, I posted on Google+ about my evaluation period for a new software development stack in general.
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
canonicalUrl: https://jochen.kirstaetter.name/software-development-stack/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2012-08-13T18:00:00Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: A couple of months ago, I posted on Google+ about my evaluation period for a new software development stack in general.
twitterTitle: Software development stack 2012
twitterDescription: A couple of months ago, I posted on Google+ about my evaluation period for a new software development stack in general.
twitterImage: 
facebookTitle: Software development stack 2012
facebookDescription: A couple of months ago, I posted on Google+ about my evaluation period for a new software development stack in general.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
A couple of months ago, [I posted on Google+](https://plus.google.com/117698191428446859536/posts/iJ43jfGanuc "I posted on Google+") about my evaluation period for a new software development stack in general.

*"Analysing existing 'jungle' of multiple applications and tools in various languages for clarification and future design decisions. Great fun and lots of headaches... #DevelopersLife"*

Surprisingly, there was response... ;-) - And this series of articles is initiated by this post. Thanks Olaf.

## The past few years...

Well, after all my first choice of software development in the past was Microsoft Visual FoxPro 6.0 - 9.0 in combination with Microsoft SQL Server 2000 - 2008 and Crystal Reports 9.x - XI. Honestly, it is my main working environment due to exisiting maintenance and support plans with my customers, but also for new project requests. And... hands on, it is still my first choice for data manipulation and migration options.

But the earth is spinning, and as a software craftsman one has to be flexible with the choice of tools. In parallel to my knowledge and expertise in the above mentioned tools, I already started very early to get my hands dirty with the Microsoft .NET Framework. If I remember correctly, I started back in 2002/2003 with the first version ever. But this was more out of curiousity. During the years this kind of development got more serious and demanding, and I focused myself on interop and integrational libraries and applications. Mainly, to expose exisitng features of the .NET Framework to Visual FoxPro - I even had [sessions about that at the German Developer's Conference in Frankfurt](xref:speaker-at-developer-conferences-user-groups).

## Observation of recent developments

With the recent hype on Javascript and HTML5, especially for Windows 8 and Windows Phone 8 development, I had several 'Deja vu' events... Back in early 2006 (roughly) I had a conversation on the future of Web and Desktop development with my former colleagues Golo Roden and Thomas Wilting about the underestimation of Javascript and its root as a prototype-based, dynamic, full-featured programming language. During this talk with them I took the Mozilla applications, namely Firefox and Thunderbird, as a reference which are mainly based on XML, CSS, Javascript and images - besides the core rendering engine. And that it is very simple to write your own extensions for the Gecko rendering engine. Looking at the Windows Vista Sidebar widgets, just underlines this kind of usage. So, yes the 'Modern UI' of Windows 8 based on HTML5, CSS3 and Javascript didn't come as any surprise to me. Just allow me to ask why did it take so long for Microsoft to come up with this step?

## A new set of tools

Ok, coming from web development in HTML 4, CSS and Javascript prior to Visual FoxPro, I am partly going back to that combination of technologies. What is the other part of the software development stack here at [IOS Indian Ocean Software Ltd](https://www.ios.mu/)? Frankly, it is easy and straight forward to describe:

- [Microsoft Visual FoxPro 9.0 SP 2](https://msdn.com/vfoxpro "Microsoft Visual FoxPro 9.0 SP 2") - still going strong!
- [Visual Studio 2012](https://msdn.com/vstudio "Visual Studio 2012") (C# on latest .NET Framework)
- [MonoDevelop](https://monodevelop.com/ "MonoDevelop")
- [Telerik DevCraft Suite](https://www.telerik.com/developer-productivity-tools.aspx "Telerik DevCraft Suite")
  - WPF
  - ASP.NET MVC
  - Windows 8
  - Kendo UI
  - Windows Phone 8
  - OpenAccess ORM
  - Reporting
  - JustCode
- [CODE Framework](https://codeframework.codeplex.com/ "CODE Framework") by EPS Software
- [MonoTouch](https://xamarin.com/monotouch/ "MonoTouch") and [Mono for Android](https://xamarin.com/monoforandroid "Mono for Android")
- [Subversion](https://subversion.apache.org/ "Subversion")
- Continious Integration with [JetBrains TeamCity](https://www.jetbrains.com/teamcity/ "JetBrains TeamCity")
- and additional tools for the daily routine: [Notepad++](https://notepad-plus-plus.org/ "Notepad++"), JustCode, SQL Compare, DiffMerge, VMware, etc.
- Following the principles of [Clean Code](https://cleancoder.com/ "Clean Code") [Developer](https://clean-code-developer.com/ "Developer") and the [Agile Manifesto](https://agilemanifesto.org/ "Agile Manifesto")

Actually, nothing special about this combination but rather a solid fundament to work with and create line of business applications for customers.Honestly, I am really interested in your choice of 'weapons' for software development, and hopefully there might be some nice conversations in the comment section.

Over the next coming months I'm going to describe a little bit more in detail about the reasons for my decision. Articles will be added bit by bit here as reference, too. Please bear with me...

Regards, JoKi