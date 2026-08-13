---
uid: rock-your-code-defensive-programming-for-microsoft-net
title: 'Rock Your Code: Defensive Programming for Microsoft .NET by David McCarter'
slug: rock-your-code-defensive-programming-for-microsoft-net
date: 2019-02-03
status: published
type: post
description: Talking about Defensive Programming during times of Test Driven Development, Clean Code, Domain Driven Development and all other kinds of buzzwords seems a bit unusual. From his long-year experience David McCarter shares a collection of rules of thumb to write better, rock-solid code.
tags:
- Recension
- Development
keywords: Recension, Development
metaTitle: 'Rock Your Code: Defensive Programming for Microsoft .NET by David McCarter'
metaDescription: Talking about Defensive Programming during times of Test Driven Development, Clean Code, Domain Driven Development and all other kinds of buzzwords seems a bit unusual. From his long-year experience David McCarter shares a collection of rules of thumb to write better, rock-solid code.
image: https://images.unsplash.com/photo-1496169514208-d9affacc58ba?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
ogTitle: 'Rock Your Code: Defensive Programming for Microsoft .NET by David McCarter'
ogDescription: Talking about Defensive Programming during times of Test Driven Development, Clean Code, Domain Driven Development and all other kinds of buzzwords seems a bit unusual. From his long-year experience David McCarter shares a collection of rules of thumb to write better, rock-solid code.
layout: post
bodyClass: post-template tag-recension tag-development
postClass: post tag-recension tag-development
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/rock-your-code-defensive-programming-for-microsoft-net/
imageUrl: https://images.unsplash.com/photo-1496169514208-d9affacc58ba?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
twitterImageUrl: https://images.unsplash.com/photo-1496169514208-d9affacc58ba?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: https://images.unsplash.com/photo-1496169514208-d9affacc58ba?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
featured: false
publishedAt: 2019-02-03T13:16:29Z
updatedAt: 2019-02-07T05:45:52Z
excerpt: Talking about Defensive Programming during times of Test Driven Development, Clean Code, Domain Driven Development and all other kinds of buzzwords seems a bit unusual. From his long-year experience David McCarter shares a collection of rules of thumb to write better, rock-solid code.
twitterTitle: 'Rock Your Code: Defensive Programming for Microsoft .NET by David McCarter'
twitterDescription: Talking about Defensive Programming during times of Test Driven Development, Clean Code, Domain Driven Development and all other kinds of buzzwords seems a bit unusual. From his long-year experience David McCarter shares a collection of rules of thumb to write better, rock-solid code.
twitterImage: 
facebookTitle: 'Rock Your Code: Defensive Programming for Microsoft .NET by David McCarter'
facebookDescription: Talking about Defensive Programming during times of Test Driven Development, Clean Code, Domain Driven Development and all other kinds of buzzwords seems a bit unusual. From his long-year experience David McCarter shares a collection of rules of thumb to write better, rock-solid code.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Talking about Defensive Programming during times of Test Driven Development, Clean Code, Domain Driven Development and all other kinds of buzzwords seems a bit unusual. From his long-year experience David McCarter shares a collection of rules of thumb to write better, rock-solid code. The book is part of his conference series titled *Improving Code Quality... One Developer at A Time*.

Back in 2017 I met David at the C# Corner conference in Delhi, India. While I gave a session on .NET Core on Linux, he had several sessions on how to be successful as a software developer and how to improve programming skills by sharing his experience as a programmer for over two decades.

His series *[Improving Code Quality... One Developer at A Time](http://dotNetTips.com)* was already in full swing and the review on his book on Defensive Programming is a milestone on this journey.

The targeted audience of the title are .NET developers with little to a few years of experience. The major focus is on how to write code that avoids causing exceptions. And in case that an exception happens on how to deal with it depending on the application layer it occurs. Lastly, David writes about techniques to log exceptions in .NET Core.

> Stop exceptions before they happen

Of course, the best way to deal with an exception is not to cause an exception. And that's how defensive programming adds value to your code base. Use the existing features of .NET and .NET Core to check the state of objects, properties and parameters before using them further.

Typically, one would always check an object or property for `null`. If you're working with file system operations check whether a file really exists before accessing it. Treat all incoming parameters and data as incomplete or damaging to your program execution. If the state of an object or property does not match the expected situation stop any further execution and return back to the caller. Stay on the positive path...

Lastly, David gives a few tips on how to deal with exceptions that are still occurring inclusive the ones that our code might actually throw given incorrect state evaluation. The .NET Framework has several options on where to catch such exception, inclusive the option to implement an "catch-all" exception handler that wouldn't miss a single beat.

The book has 42 pages in total and is relatively short in regards to the topic overall. Given the length of Rock Your Code - Defensive Programming it is a good fit for a couple of lunch breaks, one or two commute units or a dedicated Friday afternoon learning session. Some information might be too obvious to an experienced .NET developer but surely a good resource for junior developers to get on the right track of writing better source code from the very beginning.

You can get a copy of [Rock Your Code - Defensive Programming on Amazon](https://amzn.to/2RWrwBJ) at an exceptional low price.

[![](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07GCQJ6FJ&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=geblbyjo-20&language=en_US)](https://www.amazon.com/dp/B07GCQJ6FJ/ref=as_li_ss_il?ie=UTF8&linkCode=li3&tag=geblbyjo-20&linkId=57d9e7bb737a941d48f9470659f2c835&language=en_US)![](https://ir-na.amazon-adsystem.com/e/ir?t=geblbyjo-20&language=en_US&l=li3&o=1&a=B07GCQJ6FJ)

> This book brings writing better code to the next level.

The bespoken book is one of the newer titles of [David McCarter](https://amzn.to/2WdIydK); available on Amazon. You might also be interested in his advice on how to [Rock Your Technical Interview](https://amzn.to/2Msxe97).

<small>Disclaimer: I'm a technical editor of the book.  
Image credit: John Pratt</small>
