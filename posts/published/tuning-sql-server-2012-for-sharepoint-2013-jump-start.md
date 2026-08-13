---
uid: tuning-sql-server-2012-for-sharepoint-2013-jump-start
title: Tuning SQL Server 2012 for SharePoint 2013 Jump Start
slug: tuning-sql-server-2012-for-sharepoint-2013-jump-start
date: 2013-09-01
status: published
type: post
description: Very helpful insights in tuning your SQL Server 2012 for SharePoint 2013. Overall great a Jump Start and lots of funny jokes and comments. It's a real pleasure to follow those modules and the content provided.
tags:
- Development
keywords: Development
metaTitle: Tuning SQL Server 2012 for SharePoint 2013 Jump Start
metaDescription: Very helpful insights in tuning your SQL Server 2012 for SharePoint 2013. Overall great a Jump Start and lots of funny jokes and comments. It's a real pleasure to follow those modules and the content provided.
image: ''
ogTitle: Tuning SQL Server 2012 for SharePoint 2013 Jump Start
ogDescription: Obviously, I am going to run my 30 days challenge of Microsoft SharePoint a little bit different than some readers might have expected it.
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/tuning-sql-server-2012-for-sharepoint-2013-jump-start/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2013-09-01T14:27:55Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Obviously, I am going to run my 30 days challenge of Microsoft SharePoint a little bit different than some readers might have expected it.
twitterTitle: Tuning SQL Server 2012 for SharePoint 2013 Jump Start
twitterDescription: Obviously, I am going to run my 30 days challenge of Microsoft SharePoint a little bit different than some readers might have expected it.
twitterImage: 
facebookTitle: Tuning SQL Server 2012 for SharePoint 2013 Jump Start
facebookDescription: Obviously, I am going to run my 30 days challenge of Microsoft SharePoint a little bit different than some readers might have expected it.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

![Microsoft SharePoint](https://s.kirstaetter.name/images/sharepoint.png)Obviously, I am going to run my 30 days challenge of Microsoft SharePoint a little bit different than some readers might have expected it.

## []()Start at the end

No, I'm not starting at the 'Chapter 1' of what SharePoint actually is but directly jump into the optimisation of how SharePoint and SQL Server should work together in best terms possible. Out of experience I can tell you that it is quite a bit frustrating to discover at any time later that your installation and configuration of a product is actually messed up out-of-the-box. And that's what actually happens all the time when you start to read a book from start to end; the best practices and optimised parameters for the working environment are only revealed after most of the work has been completed. Time to throw over everything and do it again from scratch but now with 'the expert's advice' at hand. Sticking to the DRY principle I am not a fan of re-doing my stuff all the time but prefer to learn the proper way at the beginning. Getting rid of wrong paradigms is more difficult than to avoid them in the first place.

## []()Today's resource(s)

Okay, let's have a look at what to expect from this great [Jump Start session over at the Microsoft Virtual Academy](https://www.microsoftvirtualacademy.com/training-courses/tuning-sql-server-2012-for-sharepoint-2013-jump-start "Jump Start session over at the Microsoft Virtual Academy"):

> *SQL Server stores most of the data for SharePoint. This Jump Start training focuses on how these two products are integrated. Join two of the industry’s most popular SharePoint experts, Bill Baer and Brian Alderman on an exploration of SQL Server settings, SQL Server system database settings and configuration options that will improve SharePoint 2013 performance, availability and security. Enjoy this demo filled Jump Start to help you optimize SQL Server 2012 deployment to protect your SharePoint environment.*

The Jump Start is split into 4 modules and comes with the slide presentation as additional material. Personally, I like the fact that all four videos are available with closed captions which helps in some occassions to keep track of some words. Very helpful to non-native speakers of English language.

## []()Takeaway

A proper and correct installation of SQL Server is not only essential but very crucial to a successful deployment of SharePoint. Some settings like the default collation setting can be specified during installation only and not changed any time later. Furthermore, due to the amount of databases that SharePoint uses (23 for version 2013) it is compulsory to provide a dedicated SQL instance - either default or named instance - for SharePoint. Modify the default values of initial size and auto-growth in Megabytes (MB) in the model database of SQL Server as this will put less stress and work on the installation during daily usage; or better said it will provide better performance than the default values.

And last but not least have a conversation with your Database Administrator (DBA) to avoid any manual optimisation in a SharePoint SQL instance. The results might (for almost sure) be contra-productive with future service packs, hotfixes or updates of SharePoint as your installation is going off-track from the expected environment by the SharePoint development team. So, don't be surprised in case your SharePoint goes nuts after your DBA applied some 'improvements'.

I'm glad that Bill and Brian provide the ultimate formula to calculate the Maximum Memory Setting: ;-)

` SQL Max Memory = TotalPhyMem - (NumOfSQLThreads * ThreadStackSize) - (1GB * CEILING(NumOfCores/4))  `  
` NumOfSQLThreads = 256 + (NumOfProcessors*- 4) * 8  `  
`ThreadStackSize = 2MB on x64 or 4 MB on 64-bit (IA64) (* If NumOfProcessors > 4, else 0)`

Get your calculators ready. Of course, this all depends on the purpose of your machine and whether it is used exclusively for SharePoint or in correlation with other SQL instances and services running.

Despite having proper or better configuration settings for SQL Server it is also interesting to spent some time on the operating system, mainly the details of your hard drives, like NTFS allocation unit size. According to the experts of the Jump Start newer versions of Windows Server (2008 or higher) already should have a better setting but still run a chkdsk from your administrative command prompt and get to know.

`> chkdsk C:`

Anything different than 64K should be changed (4096 is the usual default value). As for your data drives this might be an easy exercise but your system drive should have the optimal allocation unit size, too. Which in worst case means that you have to re-install the whole system. As I stated above: Do it correctly from the beginning and only once! Anyway, here's the command in order to get your drives ready:

`> format <drive> /Q /FS:NTFS /A:64K /V:<volume> /Y`

In order to get an optimal environment to run a performant installation of Microsoft SharePoint there are quite a number of important settings to have a look at. Not too many after all but still some that need attention prior to installation or during installation of either operating system, SQL Server instance or SharePoint databases and services.

## []()Bullet points

- **Avoid Resume Producing Events** (RPEs) - know what you do, apply best practices and practice!
- Check and apply optimal NTFS Allocation Unit Size to your drives: **64K**
- Use **multiple physical drives** for your SQL Server performance. Improved handling of data storage, SQL log files and backups
  - RAID 10 for live environment
  - RAID 5 for backups
- Set default collate sequence during SQL Server installation to: **Latin1\_General\_CI\_AS\_KS\_WS**
- Change default values of **initial size and auto-growth** in model DB
- Configure **maximum (and minimum) memory configuration** of the SQL instance  
- Use **Full Recovery Model** for your transaction logs and perform full backups With INIT
- Take care of the 3 Ps for backups: Plan, Perform, and Practice (the restore)
- Apply proper naming convention to your databases - especially **'\_DB' suffix** for performance reasons ;-)
- Configure the **default file locations (not on system drive)** and restart the SQL instance
- Control the size of your databases and maximum **number of site collections** per database in SharePoint
- Put a (virtual) sign for your DBA: **Don't Touch This!**

Very helpful insights in tuning your SQL Server 2012 for SharePoint 2013. Overall great a Jump Start and lots of funny jokes and comments. It's a real pleasure to follow those modules and the content provided. Honestly, I hope that Brian had good luck with his choice of hair growth products.

## []()Update(s)

Day 2 - While reading some SharePoint blogs I came across the following whitepaper on [Maximizing SQL 2012 Performance for SharePoint 2013](https://absolute-sharepoint.com/portfolio/spsqlwhitepaper "Maximizing SQL 2012 Performance for SharePoint 2013") by Vlad Catrinescu. Thanks to Stephan Oetzel.
