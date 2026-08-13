---
uid: lets-rock-with-my-and-maria
title: Lets rock with MySQL and MariaDB
slug: lets-rock-with-my-and-maria
date: 2015-01-02
status: published
type: post
description: MariaDB is an inplace-replacement for MySQL. In case that you're operating your website or blog on MySQL you can simply install and use MariaDB instead of. It works flawlessly.
tags:
- Linux
keywords: Linux
metaTitle: Lets rock with MySQL and MariaDB
metaDescription: MariaDB is an inplace-replacement for MySQL. In case that you're operating your website or blog on MySQL you can simply install and use MariaDB instead of. It works flawlessly.
image: https://images.unsplash.com/photo-1470305585628-a7d2cb18efa2?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=46fd51fecd6c84e0c6fa8b4b81fa3f32
ogTitle: Lets rock with MySQL and MariaDB
ogDescription: Some weeks months ago...
layout: post
bodyClass: post-template tag-linux
postClass: post tag-linux
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
canonicalUrl: https://jochen.kirstaetter.name/lets-rock-with-my-and-maria/
imageUrl: https://images.unsplash.com/photo-1470305585628-a7d2cb18efa2?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=46fd51fecd6c84e0c6fa8b4b81fa3f32
twitterImageUrl: https://images.unsplash.com/photo-1470305585628-a7d2cb18efa2?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=46fd51fecd6c84e0c6fa8b4b81fa3f32
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: https://images.unsplash.com/photo-1470305585628-a7d2cb18efa2?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=46fd51fecd6c84e0c6fa8b4b81fa3f32
featured: false
publishedAt: 2015-01-02T21:00:00Z
updatedAt: 2018-04-02T08:38:43Z
excerpt: Some weeks months ago...
twitterTitle: Lets rock with MySQL and MariaDB
twitterDescription: Some weeks months ago...
twitterImage: 
facebookTitle: Lets rock with MySQL and MariaDB
facebookDescription: Some weeks months ago...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

[![Logo of MariaDB Sealion mascot](https://s.kirstaetter.name/images/MariaDB_Logo_Full_WhiteBck_Lettering.png)](https://mariadb.com "MariaDB homepage")Some weeks months ago...

## What happens on Facebook

I saw an announcement made by Ronny on Facebook that he's about to [organise a meeting about MySQL and MariaDB](https://www.facebook.com/events/331059563716694/ "Lets rock with Maria DB and MySQL"). Well, I have to admit that I didn't have that much contact with Ronny but I knew that he was involved in the initiation of the [Linux User Group of Mauritius (LUGM)](https://lugm.org "Linux User Group of Mauritius (LUGM)"), and that [Ish](https://hacklog.in/) already mentioned his name a couple of times, mostly because of the inspirational approach and other funny things. Well, long story short. Ronny mentioned that one of his friends will be around on the island for some vacation and that said person agreed to do a session on the history, the (eventual) future and some technical aspects of MySQL and MariaDB. Sounds great and having an expert from abroad doesn't happen too often...

Okay, next Ronny was looking for a decent location and I suggested to him that he might his luck at The Flying Dodo Brewery in Bagatelle. In general not a problem but those guys over there speak money and in order to get their side room with some conference aspirations they wouldn't agree on the usual deal for user groups. Meaning: Room for attendees consuming food & drinks. As I had personal interest in this session to happen, I backed Ronny's intentions to go forward with it and to let me know in case that there financial constraints to be expected. Running your business provides you with some benefits and allowances. Anyway, there was a little fee for the evening to be paid, and I was glad to cover those expenses through my business: [IOS Indian Ocean Software Ltd.](https://www.ios.mu/ "IOS Indian Ocean Software Ltd.")

## Lets rock with MySQL and MariaDB

The "event" was scheduled for the evening hours, and after the official part it was commonly agreed that we are going to leverage the location and have a decent after-meeting session at the brewery. It's always nice to combine work with pleasure - particularly in that specific order.

Our presenter, an international consultant for MySQL and MariaDB working at SkySQL AB at that time, named Joffrey Michaie did a great job during the evening. First, he gave us a brief history lesson about the origins of MySQL, then elaborated on the recent purchase event during the last couple of years and went over the actual reasons why MariaDB has been created. Well, Sun and Oracle did a great job to get quite a number of good developers on MySQL as well as the community on their feet. The fork of MySQL into MariaDB is reasonable given that Oracle doesn't need to support two opposing RDBMS within the same company - astounishingly that's a very familiar constellation seeing Microsoft SQL Server and Microsoft Visual FoxPro (VFP) in the past. Anyway, approximately 90% (and more) of the original MySQL developers quit their job and went over to a company called SkySQL AB - which is solely temporarily and [there had been a press release recently](https://mariadb.com/news-events/press-releases/skysql-become-mariadb-corporation), that it's now officially MariaDB AB. Monty Widenius had his coup and the core development team is back to its roots.

And... best of all: **MariaDB is an inplace-replacement for MySQL**. In case that you're operating your website or blog on MySQL you can simply install and use MariaDB instead of. It works flawlessly.

Next, Jojo gave us some corner data about the wide-spread use of MySQL/MariaDB. Actually some big internet companies or better said their websites (like Facebook, SAP, Xing, etc.) are driven by MySQL installations spread over hundreds or even over thousands of machines. Of course, this requires some interesting architecture not only regarding the physical setup of machines and networks but also in terms of storage and replication features. High-availability (HA) is the magical keyword in this case. At a certain size you have to switch towards DB clusters and Joffrey gave us good information about one could setup such clusters using Galera. He also gave us a brief overview of some specialised storage engines available in MySQL/MariaDB which definitely go far beyond the capabilities of the standard types like MyISAM or InnoDB.

## Full screen entertainment for geeks

The full presentation of a whooping 107 slides is available on SlideShare - Thanks to Joffrey and the LUGM!

<iframe src="https://www.slideshare.net/slideshow/embed_code/38047472" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border: 1px solid #CCC; border-width: 1px; margin-bottom: 5px; max-width: 100%;" allowfullscreen="true"> </iframe>

**[MariaDB Presentation by Joffrey Michaie](https://www.slideshare.net/ishwon/mariadb-prez-by-joffrey-michaie "MariaDB Prez by Joffrey Michaie")** **[  
](//www.slideshare.net/ishwon)**

On my side, I have to admit that I was a bit interruptive as I had a good number of questions regarding certain features I'm used to using either VFP or SQL Server. Especially given the fact that I was involved in the software architecture and development of client-server applications that run on roughly 100 instances of SQL Server including different types of data replication. Yes, we did partitioning and the database has a variety of replication scenarios for different tables; including typical master-slave replication but also enhanced 2-way replication. Also dealing with data volumes in 2-digit and even 3-digit regions is not unusual with my clients. And there is quite a difference between writing and running queries against a low amount of records compared to tables with 15+ million records. Not to forget about write and update operations. Patiently, Joffrey took note of my questions and he had very good answers how certain setups and requirements could be solved and handled with MariaDB. One of the interesting topics was the discussion about data types of "uniqueidentifier" versus "UUID" versus "Global Transaction ID (GTID)". Well, basically they are the same... Whereas SQL Server handles replication based on that specific data type, MySQL or MariaDB remains on dealing with integer-based column data types (comparable to Auto-Increment in SQL Server) - which I find problematic.

![MariaDB Enterprise Architecture v3.1](https://s.kirstaetter.name/images/mariadb_enterprise_architecture_v3.1.png)  
*MariaDB is not just the database anymore; it's a platform for application developers and database administrators*

Anyway, the evening had some interesting chunks of information for me and I enjoyed the whole presentation. Joffrey knows how to keep the audience focused and engaged into the topic. And shamelessly we extending the scheduled 1-hour session by at least 30 minutes or so. Until all questions have been asked and answered. And after all this talking and listening it was time to move over to the social aspects of the evening and to get some refreshments.

## Networking session and future activities

Later on I managed to have a little smalltalk with Jojo and even though the meeting was under the aegis of the LUGM, I informed him about the existence, goals and intentions of the [Mauritius Software Craftsmanship Community (MSCC)](https://www.meetup.com/MauritiusSoftwareCraftsmanshipCommunity/ "Mauritius Software Craftsmanship Community (MSCC)"). Dunno, how he took it but since then we are still in touch on social media networks, and have a chat from time to time. On my part I'm looking forward to the next opportunity to hear about [MariaDB](https://mariadb.com/)from Joffrey - and of course I won't hesitate to act as a sponsor again.

Oh, and thanks for the goodies - I really like that black MariaDB 10 T-Shirt.

Disclaimer: Images are courtesy of MariaDB Corporation Ab. MariaDB is a trademark or registered trademarks of MariaDB Corporation Ab in the European Union and United States of America and/or other countries. MySQL is a trademark of Oracle Corporation Inc.
