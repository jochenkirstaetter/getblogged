---
uid: gdg-cloud-munich
title: GDG Cloud Munich (Draft)
slug: gdg-cloud-munich
date: 2023-11-18
status: draft
type: post
description: Ahead of the Google I/O Connect event in Amsterdam there had been exchange with the organisers of GDG Cloud Munich. Thankfully, they accepted a proposal to speak. Why Munich, you ask. It's quite far...
tags:
- Community
keywords: Community
metaTitle: GDG Cloud Munich
metaDescription: Ahead of the Google I/O Connect event in Amsterdam there had been exchange with the organisers of GDG Cloud Munich. Thankfully, they accepted a proposal to speak. Why Munich, you ask. It's quite far...
image: ''
ogTitle: GDG Cloud Munich
ogDescription: Ahead of the Google I/O Connect event in Amsterdam there had been exchange with the organisers of GDG Cloud Munich. Thankfully, they accepted a proposal to speak. Why Munich, you ask. It's quite far...
layout: post
bodyClass: post-template tag-community
postClass: post tag-community
isPost: true
isPage: false
isDraft: true
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
canonicalUrl: https://jochen.kirstaetter.name/gdg-cloud-munich/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: ''
updatedAt: 2024-02-11T08:44:29Z
excerpt: Ahead of the Google I/O Connect event in Amsterdam there had been exchange with the organisers of GDG Cloud Munich. Thankfully, they accepted a proposal to speak. Why Munich, you ask. It's quite far...
twitterTitle: GDG Cloud Munich
twitterDescription: Ahead of the Google I/O Connect event in Amsterdam there had been exchange with the organisers of GDG Cloud Munich. Thankfully, they accepted a proposal to speak. Why Munich, you ask. It's quite far...
twitterImage: 
facebookTitle: GDG Cloud Munich
facebookDescription: Ahead of the Google I/O Connect event in Amsterdam there had been exchange with the organisers of GDG Cloud Munich. Thankfully, they accepted a proposal to speak. Why Munich, you ask. It's quite far...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Ahead of the Google I/O Connect event in Amsterdam there had been exchange with the organisers of GDG Cloud Munich. Thankfully, they accepted a proposal to speak. Why Munich, you ask. It's quite far from Amsterdam.

Given the circumstances that I had to do some of my annual health check-ups and examinations in Germany I cramped a couple of activities into a single trip to Europe. One of them required to stop for a couple of days in Munich. As I was looking for community events around the same time I noticed that the GDG Cloud chapter might have something coming up.

Hence I reached out to Yevgen to see whether there would be a possibility of a meetup around that time, and in case there could be interest in a certain topic. Turns out that both requests aligned nicely and in consequence I was invited to speak at their hybrid event in June.

The topic was "State of GCP: .NET Edition" which covers a range of products and services offered by Google Cloud Platform (GCP) that can be used in combination with Microsoft .NET technology stack, in particular with C#.

Hang on, C# and Google?  
Yup, actually it works pretty well and there are numerous reasons to consider a mature, extensible, open source, and enterprise-battled eco-system for your cloud-based implementations. According to the [TIOBE index](https://www.tiobe.com/tiobe-index/) C# had the largest growth rate compared to other programming languages.

![Source: https://www.tiobe.com/tiobe-index/ ](../content/images/2023/11/uNqLq0ZJtzAvxzpqH2zkZQejEp3Ce8dDcCaupj74g1sJr6j17aEVQf5j-9iX7BZLFIc8rwKb9DM3q_TgnILL3FJ1NInZzmL9YMFOEsYnWP69iKs0HBvkAM9lvf_yNbqoA5-hpvwHzle4LgCPisnVhLlN=s2048.webp)

Personally, it allows me to leverage my existing knowledge and doesn't require me to dig deeper into other programming languages like JavaScript, Go, Python, and so forth, in order to benefit from Google Cloud, and it also shows that one isn't locked in to cloud computing provided by Microsoft Azure while using C# applications. Bearing this in mind, it's actually a solid way to build so-called cross-cloud or multi-cloud solutions.

I was given approximately one hour to present about .NET. After setting up the system and being introduced by Yevgen to the in-person and online audience I started to address a couple of potential misconcpetions regarding Microsoft .NET and C#. The majority of the audience had never used C# before and I was curious about some of the reasons. This then allowed me to go with the flow and clarify some statements. I added up a few practical examples from my experience and then spanned the arc to Google Cloud services that can be used as part of the solution. Again sharing some of the obstacles and pitfalls observed and handled in the process.

Some of the questions asked indicated that there is quite some work to do removing a slightly negative reputation of the Microsoft .NET eco-system, simply because it's Microsoft (maybe its past?), whereas other questions looked behind that facade and brought up comparison to other existing approaches like backend development with Node.js and Express, and how C# could be useful for such backend services.

To begin with .NET development I explained the *dotnet* CLI tool and how project templates get you started.

![](../content/images/2023/11/GE7cNRtch-j07CuvqrRQuMIOp5oKtR8MHt573fsv_MNhTg-CT2RLZWkpt50u4RaG9yiTczeQCfshFVkvv6mAulhHPfzf_873z6wt0_EyI6uSOxZshwZqP9-bv2Yhrdf1n4tBNThODEq5LebCkJlEK-N2=s2048.webp)

When I launched the terminal in Visual Studio Code and started to show how a sample API application is developed in C#, using minimal API, the interest level in the audience rose instantly. I showed the generated source code and how easy it is to get going right away. Some remarks where like "hey, that really looks like Express", "Oh, are those arrow functions?" (meaning anonymous delegates), and "that looks neat and clean".

![](../content/images/2023/11/NZW1v8X81ma5JIzDopc8qKfCfZvR127XwB0cgG1_c3ta2Ke_hM4dqKkBjPV51AmpaBhZXxrXh2cFYY3PqKS5vD5wLd2ls4eDvwFLuexfxgkrERbV-2Kok4oRcPEbqODGMxQKoa3q0kGcef59Diu5_sYA=s2048.webp)

Next, I ventured into the NuGet package management and how developers can integrate any package into their project easily. Especially showing the over 700 NuGet packages available to use Google APIs for all kind of services and functionalities.

![](../content/images/2023/11/evV8iZxybA-TELu0795QGJn2HPcxDvbXswOu-TRmiOJIaDXdTcOnyM7dVhRSyWI5uAx8jP3vHbQ-nT7lIPshrWrUV75QAie0Gf6DC83ecHLIT8FD33k4ABqpSw9xWNfSGJDslHlFIj8_VaH-pQ6QpeTk=s2048.webp)

Also mentioning that the package management is less space-consuming and easier to maintain compared to node modules.

Lastly, it was time to deploy to Google Cloud. All this time I stayed in VS Code and never had to switch focus to another application. The Google Cloud extension for VS Code provides you access to your resources in the cloud, and using the gcloud CLI tool does the rest of the job. Deploying the just created API service to App Engine Flexible was done quickly.

What about serverless? Let's do it. I explained that the dotnet CLI tool can be extended with project templates and showed that there are project templates targetting Google Cloud Functions.

First, I created a new Google Cloud function using the HTTP endpoint trigger, showed the source code and the necessary implementation of the interface, and how to deploy it using the gcloud CLI tool.

![](../content/images/2023/11/QuJw6f0El3MwN3hNX10p3xJrJX6uHQh7cl-bcu5zhL39D3__IYcKxMYI86XuJrkzMc19HUWsviSIItxwVdcAz09lVCzrarZd1kGWW_K5e5giOb5yZQb_QnWBcfdab56vyb-ON5Pfk17BcU0wcCaUdBqR=s2048.webp)

A matter of roughly 5 minutes from start to finish.

![](../content/images/2023/11/X6YzTkXe6obZ17nRy3Uy-hERl0HrCRdpPPZAWsJiH9wLTdiydZ_xPNWuCG8rhrn5uW2K9TiUBb6Wi045va4trKQmbqvkht_VwY2HyvYhgAen_xehmQVMYKQwTE-uD_MQxwY20HpKOkOWu4xx_IluSH9i=s2048.webp)

Then, I did the same using the project template for an event-triggered Google Cloud function, and explained the flexibility of the type-induced interface to create functions handling different types of data loads.

![](../content/images/2023/11/yAl9VB2ZTh5lc5W1JoEceHhODXO_rp0wcd5uXD6jGeRozjDD0i_KiFayOPMunBrQEenf5hoduIXeMrPXCwtiI0kY-Pn1AypawInSvPJgX_BBgqP85a1P82uNkIrzoIq6PFJinEWdfiYb_GIFv0Ypawes=s2048.webp)

And thanks to the Google Cloud functions emulator you can launch, test and debug your local code before deploying it to Google Cloud.

```bash
$ dotnet run
```

Gratefully, with every piece of source code shown and sharing my experience of combining C# implementation using NuGet packages and how to deploy it to GCP there were more and more questions in the audience. Finally, I was indicated by the team of GDG Cloud Munich that we are out of time, and I wrapped it up quickly with my opinionated conclusion of using C# together with the rich .NET eco-system in order to develop scalable, enterprise-ready, and cloud-native solutions using Google Cloud Platform.

I was humbled by the audience's interest to know more and the numerous follow-up questions regarding the talk and the live demos showed. Thanks!

My heart-felt thanks and best wishes to the organising team of GDG Cloud Munich, namely Yevgen Batovskyi and Spyros Kyriazatis, for this opportunity to talk and share my passion. It was an amazing evening at the Google office in Munich.

PS: Apart from the announcement screen the whole talk was a *no slide deck presentation* purely based on me talking about the history, the evolution, the current state of C# and .NET, and how it fares together with GCP based on my experience.

<small>Picture credits: Mary Jane Kirstätter and Inna Zaytseva</small>