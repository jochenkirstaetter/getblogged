---
uid: vmware-kernel-module-updater-hangs-on-ubuntu-1304
title: VMware Kernel Module Updater hangs on Ubuntu 13.04
slug: vmware-kernel-module-updater-hangs-on-ubuntu-1304
date: 2013-05-21
status: published
type: post
description: Usually, the dialog of VMware Kernel Module Updater pops up, asks for root access authentication, and completes the compilation. In theory this is supposed to work flawlessly but in reality there are pitfalls occassionally.
tags:
- Linux
keywords: Linux
metaTitle: VMware Kernel Module Updater hangs on Ubuntu 13.04
metaDescription: Usually, the dialog of VMware Kernel Module Updater pops up, asks for root access authentication, and completes the compilation. In theory this is supposed to work flawlessly but in reality there are pitfalls occassionally.
image: content/images/2013/05/photo-1532622785990-d2c36a76f5a6.webp
ogImage: content/images/2013/05/photo-1532622785990-d2c36a76f5a6-og.webp
ogTitle: VMware Kernel Module Updater hangs on Ubuntu 13.04
ogDescription: VMware Player has a nice auto-detection of kernel changes, and requests the user to compile the required modules in order to load them. This happens from time to time after a regular update of your...
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
authorImage: content/images/2018/10/JoKi_StAubin_100px.webp
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/vmware-kernel-module-updater-hangs-on-ubuntu-1304/
imageUrl: content/images/2013/05/photo-1532622785990-d2c36a76f5a6.webp
twitterImageUrl: https://images.unsplash.com/photo-1532622785990-d2c36a76f5a6?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2013/05/photo-1532622785990-d2c36a76f5a6.webp
featured: false
publishedAt: 2013-05-21T02:19:24Z
updatedAt: 2019-01-28T02:51:19Z
excerpt: VMware Player has a nice auto-detection of kernel changes, and requests the user to compile the required modules in order to load them. This happens from time to time after a regular update of your...
twitterTitle: VMware Kernel Module Updater hangs on Ubuntu 13.04
twitterDescription: VMware Player has a nice auto-detection of kernel changes, and requests the user to compile the required modules in order to load them. This happens from time to time after a regular update of your...
twitterImage: 
facebookTitle: VMware Kernel Module Updater hangs on Ubuntu 13.04
facebookDescription: VMware Player has a nice auto-detection of kernel changes, and requests the user to compile the required modules in order to load them. This happens from time to time after a regular update of your...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
VMware Player has a nice auto-detection of kernel changes, and requests the user to compile the required modules in order to load them. This happens from time to time after a regular update of your system. Usually, the dialog of VMware Kernel Module Updater pops up, asks for root access authentication, and completes the compilation.

![vmware-kernel-module-updater-info](../content/images/2013/05/vmware-kernel-module-updater-info.webp)  
*VMware Player or Workstation checks if modules for the active kernel are available.*

In theory this is supposed to work flawlessly but in reality there are pitfalls occassionally. With the recent upgrade to Ubuntu 13.04 Raring Ringtail and the latest kernel 3.8.0-21 the actual VMware Kernel Module Updater simply disappeared and the application wouldn't start as expected. When you launch VMware Player as super user (root) the dialog would stall like so:

![vmware-kernel-module-updater-compile](../content/images/2013/05/vmware-kernel-module-updater-compile.webp)  
*VMware Kernel Module Updater stalls while stopping the services*

Prior to version 5.x of VMware Player or version 7.x of VMware Workstation you would run a command like:

> $ sudo vmware-config.pl

to resolve the module version conflict but this doesn't work anyway.

## []()Solution

Instead, you have to execute the following line in a terminal or console window:

> $ sudo vmware-modconfig --console --install-all

Those switches are (as of writing this article) not documented in the output of the --help switch. But VMware already documented this procedure in their knowledge base: [VMware Workstation stops functioning after updating the kernel on a Linux host (1002411)](https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1002411 "VMware Workstation stops functioning after updating the kernel on a Linux host (1002411)").

## []()Update

As of today I had the first kernel upgrade to version 3.8.0-22 in Ubuntu 13.04. Don't even try it without vmware-modconfig...

<small>Image credit: Kaleidico</small>