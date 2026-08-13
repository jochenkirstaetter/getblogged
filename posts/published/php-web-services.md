---
uid: php-web-services
title: PHP Web Services by Lorna Jane Mitchell - Nice try
slug: php-web-services
date: 2013-07-16
status: published
type: post
description: I was astonished that a small book like 'PHP Web Services' would be able to cover all the interesting topics about APIs and Web Services, independently whether they are written in PHP or not. And unfortunately, the title isn't able to stand up to the readers (or at least my) expectations.
tags:
- Recension
keywords: Recension
metaTitle: PHP Web Services by Lorna Jane Mitchell - Nice try
metaDescription: I was astonished that a small book like 'PHP Web Services' would be able to cover all the interesting topics about APIs and Web Services, independently whether they are written in PHP or not. And unfortunately, the title isn't able to stand up to the readers (or at least my) expectations.
image: ''
ogTitle: PHP Web Services by Lorna Jane Mitchell - Nice try
ogDescription: "Thanks to the membership in the O'Reilly User Group Programme the Mauritius Software Craftsmanship Community (short: MSCC) recently received a welcome package with several book titles. Among them is..."
layout: post
bodyClass: post-template tag-recension
postClass: post tag-recension
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
canonicalUrl: https://jochen.kirstaetter.name/php-web-services/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2013-07-16T07:06:06Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: "Thanks to the membership in the O'Reilly User Group Programme the Mauritius Software Craftsmanship Community (short: MSCC) recently received a welcome package with several book titles. Among them is..."
twitterTitle: PHP Web Services by Lorna Jane Mitchell - Nice try
twitterDescription: "Thanks to the membership in the O'Reilly User Group Programme the Mauritius Software Craftsmanship Community (short: MSCC) recently received a welcome package with several book titles. Among them is..."
twitterImage: 
facebookTitle: PHP Web Services by Lorna Jane Mitchell - Nice try
facebookDescription: "Thanks to the membership in the O'Reilly User Group Programme the Mauritius Software Craftsmanship Community (short: MSCC) recently received a welcome package with several book titles. Among them is..."
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

[![](https://ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=1449356567&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=geblbyjo-20)](https://www.amazon.com/gp/product/1449356567/ref=as_li_ss_il?ie=UTF8&camp=1789&creative=390957&creativeASIN=1449356567&linkCode=as2&tag=geblbyjo-20)![](https://ir-na.amazon-adsystem.com/e/ir?t=geblbyjo-20&l=as2&o=1&a=1449356567)

Thanks to the membership in the O'Reilly User Group Programme the [Mauritius Software Craftsmanship Community](https://www.meetup.com/MauritiusSoftwareCraftsmanshipCommunity/ "Mauritius Software Craftsmanship Community") (short: MSCC) recently received a welcome package with several book titles. Among them is the latest publication of [Lorna Jane Mitchell](https://www.lornajane.net/ "Lorna Jane Mitchell") - '[PHP Web Services: APIs for the Modern Web](https://shop.oreilly.com/product/0636920028291.do "PHP Web Services: APIs for the Modern Web")'.

Following is [the book review I put on Amazon](https://www.amazon.com/gp/product/1449356567/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1449356567&linkCode=as2&tag=geblbyjo-20 "PHP Web Services - Nice try"):

> Nice try!
>
> Initially, I was astonished that a small book like 'PHP Web Services' would be able to cover all the interesting topics about APIs and Web Services, independently whether they are written in PHP or not. And unfortunately, the title isn't able to stand up to the readers (or at least my) expectations. Maybe as a light defense, there is no usual paragraph about the intended audience of that book, but still I have to admit that the first half (chapters 1 to 8) are well written and Lorna has her points on the various technologies. Also, the code samples in PHP are clean and easy to understand.
>
> With chapter 'Debugging Web Services' the book started to change my mind about the clarity of advice and the instructions on designing and developing good APIs. Eventually, this might be related to the fact that I'm used to other tools since years, like Telerik Fiddler as HTTP proxy in order to trace and inspect any kind of request/response handling. Including localhost monitoring, SSL certification acceptance, and the ability to debug mobile devices, especially iOS-based ones. Compared to Charles, Fiddler is available for free.
>
> What really got me off the hook is the following statement in chapter 10 about Service Type Decisions: *"For users who have larger systems using technology stacks such as Java, C++, or .NET, it may be easier for them to integrate with a SOAP service."* WHAT? A couple of pages earlier the author recommends to stay away from 'old-fashioned' API styles like SOAP (if possible). And on top of that I wonder why there are tons of documentation towards development of RESTful Web Services based on WebAPI. The ASP.NET stack clearly moves away from SOAP to JSON and REST since years! Honestly, as a software developer on the .NET stack this leaves a mixed feeling after all.
>
> As for the remaining chapters I simply consider them as 'blah blah' without any real value and lots of theoretical advice. Related to the chapter 13 about 'Documentation', I just had the 'pleasure' to write a C#-based client against a Java-based SOAP Web Service. Personally, I take the WSDL as the master reference in the first place and Visual Studio generates all the stub types involved in the communication. During the implementation and testing I came across a 'java.lang.NullPointerException' in various methods and for various method parameters. The WSDL and the generated types were declared as Nullable, so nothing to worry about, or? Well, I logged in a support ticket, and guess what was the response to that scenario? *"The service definition in the WSDL is wrong, please refer to the documentation in order to use the methods and parameters correctly"* - No comment!
>
> Lorna's title is a quick read and in some areas she has good advice on designing and implementing Web Services and APIs. But roughly 100 pages aren't enough to cover a vast topic like that. After all, nice try and I'm looking forward to an improved second edition.

Honestly, I never thought that I would come across a poor review. In general, it's a good book but it clearly has a lack of depth, the PHP code samples are incomplete (closing tags missing), and there are too many assumptions and theoretical statements.
