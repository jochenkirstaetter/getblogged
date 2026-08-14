---
uid: upgrade-to-windows-server-update-services-3-0-sp1
title: Upgrade to Windows Server Update Services 3.0 SP1
slug: upgrade-to-windows-server-update-services-3-0-sp1
date: 2008-02-25
status: published
type: post
description: Upgrade to Windows Server Update Services 3.0 SP1 Already last week I upgraded our local Windows Server Update Services (WSUS) from version 2.0 to version 3.0 Service Pack 1. This step wasn&#39;t really neccessary but after having a look at the new features and capabilities of version 3.0 I decided
tags:
- Community
keywords: Community
metaTitle: Upgrade to Windows Server Update Services 3.0 SP1
metaDescription: Upgrade to Windows Server Update Services 3.0 SP1 Already last week I upgraded our local Windows Server Update Services (WSUS) from version 2.0 to version 3.0 Service Pack 1. This step wasn&#39;t really neccessary but after having a look at the new features and capabilities of version 3.0 I decided
image: ''
ogTitle: Upgrade to Windows Server Update Services 3.0 SP1
ogDescription: Already last week I upgraded our local Windows Server Update Services (WSUS) from version 2.0 to version 3.0 Service Pack 1. This step wasn't really neccessary but after having a look at the new...
layout: post
bodyClass: post-template tag-community
postClass: post tag-community
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
canonicalUrl: https://jochen.kirstaetter.name/upgrade-to-windows-server-update-services-3-0-sp1/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2008-02-25T07:55:39Z
updatedAt: 2018-04-02T08:39:11Z
excerpt: Already last week I upgraded our local Windows Server Update Services (WSUS) from version 2.0 to version 3.0 Service Pack 1. This step wasn't really neccessary but after having a look at the new...
twitterTitle: Upgrade to Windows Server Update Services 3.0 SP1
twitterDescription: Already last week I upgraded our local Windows Server Update Services (WSUS) from version 2.0 to version 3.0 Service Pack 1. This step wasn't really neccessary but after having a look at the new...
twitterImage: 
facebookTitle: Upgrade to Windows Server Update Services 3.0 SP1
facebookDescription: Already last week I upgraded our local Windows Server Update Services (WSUS) from version 2.0 to version 3.0 Service Pack 1. This step wasn't really neccessary but after having a look at the new...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Already last week I upgraded our local [Windows Server Update Services (WSUS)](https://www.microsoft.com/wsus) from version 2.0 to version 3.0 Service Pack 1. This step wasn't really neccessary but after having a look at the new features and capabilities of version 3.0 I decided to upgrade. So far, it was a good decission. Following the deployment and upgrade documentation on TechNet the whole process worked like a charm and I had no problems.  
  
As we are running WSUS on a Small Business Server 2003 R2, the upgrade routine deinstalled the existing SQL Server 2000 Desktop Engine (&lt;Servername&gt;WSUS) and therefore installed the Windows Internal Database. Well, this is something that I didn't understand properly. As there are instances of SQL Server 2005 already available on this machine, I really wonder why the setup didn't offer to choose one of these instances instead. Anyways, doesn't really matter.  
  
My first sight and impression on WSUS 3.0 SP1 is ok. The only thing that I'm missing is the web interface, or better said, I'm still searching for the WSUS 3.0 client Microsoft Management Console (MMC) application to regain remote access in order to manage the server from my Windows Vista. But this is not a real drawback as Terminal Services in administrative mode work also like a charm. And using this option I'm also able to operate the WSUS from alternative operating systems, like my freshly installed [Xubuntu Linux](https://www.xubuntu.org/).  
  
Interesting is also the fact that the attached clients get a newer Windows Update (WU) client software to communicate with the WSUS 3.0. That's nice as we had some minor problems before. Checking the computer reports shows me that these problems are solved. Apropos, reports... it's a really nice feature that WSUS 3.0 now sends status reports by mail. This reduces the number of unneccessary checks and approval as the server now reports on its own that the administrator is needed to do something.  
  
After all and up to now, I don't regret the upgrade. Following the documentation on TechNet:  
- Check integrity of your database with 'dbcc checkdb'
- Backup your existing database 'SUSDB'
- Run the WSUS 3.0 setup routine
- Update the WU software on the clients

This upgrade was really easy and took only a short time.  
  
So, just in case that you're asking yourself 'What is WSUS?' and 'Why should I use it?'.  
Well, the answer to question #1 is quite easy: [Read this](https://go.microsoft.com/fwlink/?LinkId=71266).  
  
The answer to question #2 is based on practical experiences with Microsoft updates and hotfixes. :) Well, to be serious on answer #2.  
Mauritius' internet connection to the rest of the world is quite limited and slow. And so, it is absolutely neccessary to run and operate a 'cache system' for all those downloads that Microsoft provides almost weekly (ie. Windows Defender definition files of approx. 16 MB file size). And as we are running more than one Windows OS in this company, we try to reduce our download traffic as much as possible. In this constellation we finally have only one download from the internet onto the local WSUS server that provides the updates to the clients. And also important, IMHO more important to the download aspect, is the fact that the administrator has a controlled environment and status information on all attached Windows systems. This is really a huge benefit compared to the jungle of software versions that your users may create. And running a WSUS gives you also the opportunity to delay or even decline updates from Microsoft on your machines. Isn't that nice?  
  
It's also very handsome during the installation of fresh machines. Within a blink of your eyes you can upgrade a fresh installation to the latest version of patches and upgrades. This is especally interesting while maintaining several virtual machines in either VMware or Virtual Server (or Virtual PC).  
  
Do you run WSUS on your sites? If yes, what are your experiences? Do you have useful resources on WSUS other than the information Microsoft provides?  
  
  
Sincerely, JoKi
