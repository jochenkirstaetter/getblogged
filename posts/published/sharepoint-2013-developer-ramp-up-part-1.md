---
uid: sharepoint-2013-developer-ramp-up-part-1
title: SharePoint 2013 Developer Ramp-Up - Part 1
date: 2013-09-02
status: published
type: post
description: Part 1 of Andrew Connell's series on SharePoint 2013 for developers provides a brief history and overview of the various product names and their relation to the actual SharePoint version.
tags:
- Development
keywords: Development
metaTitle: SharePoint 2013 Developer Ramp-Up - Part 1
metaDescription: Part 1 of Andrew Connell's series on SharePoint 2013 for developers provides a brief history and overview of the various product names and their relation to the actual SharePoint version.
image: ''
ogTitle: SharePoint 2013 Developer Ramp-Up - Part 1
ogDescription: Today I had a little spare time during the morning hours and I decided that after checking MVA that I'm going to query the available course material over at Pluralsight. Wow, thanks to fantastic...
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
canonicalUrl: https://jochen.kirstaetter.name/sharepoint-2013-developer-ramp-up-part-1/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2013-09-02T10:06:27Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Today I had a little spare time during the morning hours and I decided that after checking MVA that I'm going to query the available course material over at Pluralsight. Wow, thanks to fantastic...
twitterTitle: SharePoint 2013 Developer Ramp-Up - Part 1
twitterDescription: Today I had a little spare time during the morning hours and I decided that after checking MVA that I'm going to query the available course material over at Pluralsight. Wow, thanks to fantastic...
twitterImage: 
facebookTitle: SharePoint 2013 Developer Ramp-Up - Part 1
facebookDescription: Today I had a little spare time during the morning hours and I decided that after checking MVA that I'm going to query the available course material over at Pluralsight. Wow, thanks to fantastic...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
![Microsoft SharePoint](../content/images/2013/09/sharepoint.webp)Today I had a little spare time during the morning hours and I decided that after checking MVA that I'm going to query the available course material over at Pluralsight. Wow, thanks to fantastic corporations and acquisitions there are lots of courses available. Nicely split by SharePoint version as well as particular interest group. Additionally, I found a couple of online blogs and community sites that I'm going to visit regularly during the next couple of weeks.

## []()Today's resource(s)

Of course, I'm "all in" for the latest developer resources:

- [SharePoint 2013 Developer Ramp-Up - Part 1 - Understanding the Platform and Developer Experience  
](https://pluralsight.com/training/Courses/TableOfContents/cpt-sp2013-dev-ramp-part1 "SharePoint 2013 Developer Ramp-Up - Part 1")
- [SharePoint 2013 Developer Ramp-Up - Part 2](https://pluralsight.com/training/courses/TableOfContents?courseName=cpt-sp2013-dev-ramp-part2 "SharePoint 2013 Developer Ramp-Up - Part 2")
- SharePoint 2013 Developer Ramp-Up - Part 3
- SharePoint 2013 Developer Ramp-Up - Part 4
- SharePoint 2013 Developer Ramp-Up - Part 5
- SharePoint 2013 Developer Ramp-Up - Part 6

I guess, I'm going to stick to the Pluralsight library until the end of this week. We'll see...

Anyway, apart from the video material I came across a couple of other websites which I'd like to list here, too. That's mainly for personal reference instead of bookmarking in the browser, I'll use my own blog for that purpose.

- [Atkinson's SharePoint Blog](https://brandonatkinson.blogspot.com/ "Atkinson's SharePoint Blog")
- [Düsseldorfer Jung](https://duesseldorferjung.wordpress.com/tag/sharepoint/ "Düsseldorfer Jung")
- [Doerflers SharePoint Blog](https://doerflerbm.wordpress.com/)
- [SharePoint Community](https://sharepoint-community.net/ "SharePoint Community")
- [Absolute SharePoint](https://absolute-sharepoint.com/ "Absolute SharePoint")

The links are in no preferential order and I added them as soon as I found them. Most probably, I'm going to report about specific articles from those resources during this challenge. So, stay tuned and I try to provide more details on certain topics.

## []()Takeaway

First contact with the 'real stuff' in order to get an idea about software development in Microsoft SharePoint and beyond. Unfortunately and as already expected, the marketing department over at Microsoft seemed to have nothing better to do than to invent new names and baptise literally the same product with every release. Luckily, the release cycles between versions have been three years (roughly) - 2007, 2010, and 2013. Nonetheless, there will be a lot of version-specfic issues to tackle during this learning phase. Especially, when it's about historical expressions like 'WSS'\* like I had it yesterday... It's going to be exciting and demanding to catch up with roughly 6-7 years of development and changes. Okay, let's face it.

* WSS stands for Windows SharePoint Services 3.0 which forms the 'core engine' of SharePoint 2007.

Part 1 of Andrew Connell's series on SharePoint 2013 for developers provides a brief history and overview of the various product names and their relation to the actual SharePoint version. I guess, I might create a cheat-sheet or something comparable in order to reduce the level of confusion while reading through other material:

- **SharePoint 2007** (aka SharePoint v3 aka SharePoint 12)
  - Windows SharePoint Services (WSS) 3.0
  - Microsoft Office SharePoint Server (MOSS) 2007
  - .NET Framework 3.0, 32-bit or 64-bit OS
- **SharePoint 2010** (aka SharePoint v4 aka SharePoint 14)
  - Microsoft SharePoint Foundation (SPF) 2010
  - Microsoft SharePoint Server (SPS) 2010
  - .NET Framework 3.5 SP1, 64-bit OS only
- **SharePoint 2013**
  - Microsoft SharePoint Foundation (SPF) 2013
  - Microsoft SharePoint Server (SPS) 2013
  - .NET Framework 4.5, 64-bit OS only

After this quick excursion it is getting more interesting. SharePoint 2013 has a number of Development Practices and Techniques under the hood, and it will be quite a decision process depending on the task requirements to choose the correct path to go. At the moment, the following two options seem to be my future fields of operation:

- **Client-Side Object Model** (CSOM)
- **REST** API and OData syntax

As part of my job assignment, I see myself developing within Visual Studio 2012/2013. Most probably the client development in C# will be using CSOM but of course I'll keep an eye on the REST API, too. JavaScript has quite a momentum since a while and it would a shame to ignore this type of opportunity and possibilities.