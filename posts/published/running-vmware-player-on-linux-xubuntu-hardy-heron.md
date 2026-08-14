---
uid: running-vmware-player-on-linux-xubuntu-hardy-heron
title: Running VMware Player on Linux (xubuntu Hardy Heron)
slug: running-vmware-player-on-linux-xubuntu-hardy-heron
date: 2008-05-28
status: published
type: post
description: For developing purposes I installed VMware Player and therefore run virtual machines with Windows XP and Windows Vista. That's way more practical then a multiboot system.
tags:
- Linux
keywords: Linux
metaTitle: Running VMware Player on Linux (xubuntu Hardy Heron)
metaDescription: For developing purposes I installed VMware Player and therefore run virtual machines with Windows XP and Windows Vista. That's way more practical then a multiboot system.
image: ''
ogTitle: Running VMware Player on Linux (xubuntu Hardy Heron)
ogDescription: A new article since a long time. Sorry, I was and still am very busy on my job but I need to write these lines first.
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
canonicalUrl: https://jochen.kirstaetter.name/running-vmware-player-on-linux-xubuntu-hardy-heron/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2008-05-28T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: A new article since a long time. Sorry, I was and still am very busy on my job but I need to write these lines first.
twitterTitle: Running VMware Player on Linux (xubuntu Hardy Heron)
twitterDescription: A new article since a long time. Sorry, I was and still am very busy on my job but I need to write these lines first.
twitterImage: 
facebookTitle: Running VMware Player on Linux (xubuntu Hardy Heron)
facebookDescription: A new article since a long time. Sorry, I was and still am very busy on my job but I need to write these lines first.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
A new article since a long time. Sorry, I was and still am very busy on my job but I need to write these lines first.  
Since last month I modified my main development system a little bit and instead of running a native Windows operating system I gave xubuntu 7.10 a try. For developing purposes I installed VMware Player and therefore run virtual machines with Windows XP and Windows Vista. That's way more practical then a multiboot system. By the way, you can do this as well under Windows directly and use Microsoft Virtual PC instead of VMware, too.

As said, I started with xubuntu 7.10 and upgraded recently to 8.04 (Hardy Heron). Everything went smooth but VMware Player didn't start anymore. Fine, as VMware comes with predefined kernel modules which none of them fits for kernel version 2.6.24-16-generic you have to initiate the compile process yourself. No problem at all. Well, in general...



Sadly, the compile did not finish and interrupted with an error message according to a wrongly included header file. So, I looked around a bit and found a [nice step-by-step guide](https://communities.vmware.com/message/897137#897137) on the VMware website to get it up and running. Here are the steps:

- cd /usr/lib/vmware/modules/source
- cp vmmon.tar vmmon.tar.orig
- sudo tar xvf vmmon.tar
- cd vmmon-only/include/
- sudo nano vcpuset.h (or use any other editor you prefer)  
- change line 74 from: #include "asm/bitops.h" to: #include "linux/bitops.h"
- rm vmmon.tar (return to the folder where you decompressed the tar file)
- sudo tar cvf vmmon.tar vmmon-only/
- sudo rm -rf vmmon-only/
- sudo vmware-config.pl

If you try to install a fresh tarball of VMware Player then the path to the vmmon.tar archive varies depending on your download.

- cd &lt;path/to/your/dir&gt;/vmware-player-distrib/lib/modules/source/

The modification is the same but the last steps differ:

- cd ../../../  
- sudo ./vmware-install.pl  
This process should work for VMware Server and Workstation as well.

And this morning I had to do the same steps again due to an 'sudo apt-get dist-upgrade' that installed a new kernel version 2.6.24-17-generic. So, after all and now that you know how to get your VMware Player to fly, it's not a big deal.  
  
Sincerely, JoKi