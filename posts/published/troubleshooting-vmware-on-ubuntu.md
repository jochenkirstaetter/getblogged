---
uid: troubleshooting-vmware-on-ubuntu
title: Troubleshooting VMware on Ubuntu
date: 2010-04-16
status: published
type: post
description: Summary of different problems while using VMware products on Ubuntu.
tags:
- Linux
keywords: Linux
metaTitle: Troubleshooting VMware on Ubuntu
metaDescription: Summary of different problems while using VMware products on Ubuntu.
image: ''
ogTitle: Troubleshooting VMware on Ubuntu
ogDescription: Summary of different problems while using VMware products on Ubuntu. This article is going to be updated from time to time with new information about running VMware products more or less smoothly on...
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
canonicalUrl: https://jochen.kirstaetter.name/troubleshooting-vmware-on-ubuntu/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2010-04-16T03:24:10Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Summary of different problems while using VMware products on Ubuntu. This article is going to be updated from time to time with new information about running VMware products more or less smoothly on...
twitterTitle: Troubleshooting VMware on Ubuntu
twitterDescription: Summary of different problems while using VMware products on Ubuntu. This article is going to be updated from time to time with new information about running VMware products more or less smoothly on...
twitterImage: 
facebookTitle: Troubleshooting VMware on Ubuntu
facebookDescription: Summary of different problems while using VMware products on Ubuntu. This article is going to be updated from time to time with new information about running VMware products more or less smoothly on...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Summary of different problems while using VMware products on Ubuntu. This article is going to be updated from time to time with new information about running VMware products more or less smoothly on Ubuntu.

Following are links to existing articles:

- [Running VMware Player on Linux (xubuntu Hardy Heron)](xref:troubleshooting-vmware-on-ubuntu)
- [Running VMware Server on Linux (version 1.0.6 on xubuntu)](xref:troubleshooting-vmware-on-ubuntu)
- [Using ext4 in VMware machine](xref:troubleshooting-vmware-on-ubuntu)
- [Small hiccup with VMware Player after upgrading to Ubuntu 12.04](xref:small-hiccup-with-vmware-player-after-upgrading-to-ubuntu-1204)
- [Update kernel patch for VMware Player 4.0.3](xref:update-kernel-patch-for-vmware-player-403)
- [And again... VMware Player 4.0.4 on Ubuntu 12.04 (Precise Pangolin)](xref:and-again-vmware-player-404-on-ubuntu-1204-precise-pangolin)
- [VMware Player 5.0 or VMware Workstation 9.0 after upgrade to Ubuntu 12.10](xref:vmware-player-50-or-vmware-workstation-90-after-upgrade-to-ubuntu-1210)

## VMware mouse grab/ungrab problem

(Source: [LinuxInsight](https://www.linuxinsight.com/vmware-mouse-grab-ungrab-problem.html "VMware mouse grab/ungrab problem"))

Upgrading GTK library in Ubuntu since Karmic Koala gives you a strange mouse behaviour. Even if you have "Grab when cursor enters window" option set, VMware won't grab your pointer when you move mouse into the VMware window. Also, if you use Ctrl-G to capture the pointer, VMware window will release it as soon as you move mouse around a little bit. Quite annoying behavior...

Fortunately, there's a simple workaround that can fix things until VMware resolves incompatibilities with the new GTK library. VMware Workstation ships with many standard libraries including libgtk, so the only thing you need to do is to force it to use it's own versions. The simplest way to do that is to add the following line to the end of the `/etc/vmware/bootstrap` configuration file and restart the Workstation.  
`  
export VMWARE_USE_SHIPPED_GTK="force"  
`  
The interface will look slightly odd, because older version of GTK is being used, but at least it will work properly.

**Note:** After upgrading a new Linux kernel, it is necessary to compile the VMware modules, this requires to temporarily comment the export line in /etc/vmware/bootstrap.