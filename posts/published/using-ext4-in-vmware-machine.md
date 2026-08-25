---
uid: using-ext4-in-vmware-machine
title: Using ext4 in VMware machine
date: 2010-07-29
status: published
type: post
description: Using ext4 as journaling filesystem for your Linux server seems to be a good choice. But definitely not in a VMware virtual machine...
tags:
- Linux
keywords: Linux
metaTitle: Using ext4 in VMware machine
metaDescription: Using ext4 as journaling filesystem for your Linux server seems to be a good choice. But definitely not in a VMware virtual machine...
image: content/images/2010/07/photo-1528823872057-9c018a7a7553.webp
ogImage: content/images/2010/07/photo-1528823872057-9c018a7a7553-og.webp
ogTitle: Using ext4 in VMware machine
ogDescription: First of all, using a journaling filesystems like NTFS, ext4, XFS, or JFS (not to name all of them) is a very good idea and nowadays unthinkable not to do. Linux offers a good variety of different...
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
canonicalUrl: https://jochen.kirstaetter.name/using-ext4-in-vmware-machine/
imageUrl: content/images/2010/07/photo-1528823872057-9c018a7a7553.webp
twitterImageUrl: https://images.unsplash.com/photo-1528823872057-9c018a7a7553?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2010/07/photo-1528823872057-9c018a7a7553.webp
featured: false
publishedAt: 2010-07-29T02:39:38Z
updatedAt: 2019-01-28T02:48:57Z
excerpt: First of all, using a journaling filesystems like NTFS, ext4, XFS, or JFS (not to name all of them) is a very good idea and nowadays unthinkable not to do. Linux offers a good variety of different...
twitterTitle: Using ext4 in VMware machine
twitterDescription: First of all, using a journaling filesystems like NTFS, ext4, XFS, or JFS (not to name all of them) is a very good idea and nowadays unthinkable not to do. Linux offers a good variety of different...
twitterImage: 
facebookTitle: Using ext4 in VMware machine
facebookDescription: First of all, using a journaling filesystems like NTFS, ext4, XFS, or JFS (not to name all of them) is a very good idea and nowadays unthinkable not to do. Linux offers a good variety of different...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
First of all, using a journaling filesystems like NTFS, ext4, XFS, or JFS (not to name all of them) is a very good idea and nowadays unthinkable not to do. Linux offers a good variety of different option as journaling filesystem for your system. Since years I am using [SGI's XFS](https://oss.sgi.com/projects/xfs/ "SGI XFS journaling filesystem") and I am pretty confident with stability, performance and liability of the system. In earlier years I had to struggle with incompatibilities between XFS and the boot loader. Using an ext2 formatted /boot solved this issue. But, wow, that is ages ago!

Lately, I had to setup a fresh Lucid Lynx (Ubuntu 10.04 LTS) system for a change of our internal groupware / messaging system. Therefore, I fired up a new virtual machine with almost standard configuration in VMware Server and run through our network-based PXE boot and installation procedure. At a certain step in this process, Ubuntu asks you about the partitioning of your hard drive(s). Honestly, I have to say that only out of curiousity I sticked to the "default" suggestion and gave my faith and trust into the Ubuntu installation routine... Resulting to have an ext4 based root mount point ( / ). The rest of the installation went on without further concerns or worries.

Note:  
I really can't remember why I chose to go away from my favourite...  
Well, it should turn out to be the wrong decision after all.

Ok, let's continue the story about ext4 in a VMware based virtual machine. After some hours installing additional packages and configuring the new system using LDAP for general authentication and login, I had an "out-of-the-box" usable enterprise messaging system based on [Zarafa 6.40 Community Edition](https://www.zarafa.com/ "Zarafa") inclusive proper SSL-based Webaccess interface and Z-Push extension for ActiveSync with my Nokia mobile. Straightforward and pretty nice for the time spent on the setup.

Having priority on other tasks I let the system just running and didn't pay any further attention at all. Until I run into an upgrade of "Mail for Exchange" on Symbian OS. My mobile did not bother me at all with the upgrade and everything went smooth, but trying to re-establish the ActiveSync connection to the Zarafa messaging system resulted in a frustating situation. So, I shifted my focus back to the Linux system and I was amazed to figure out that the root had been remounted readonly due to hard drive failures or at least ext4 reported errors.

Firing up Google only confirmed my concerns and it seems that using ext4 for VMware based virtual machines does not look like a stable and reliable candidate to me. You might consider reading those external resources:

[ext4 fs corruption under VMWare Server 2.01](https://ubuntuforums.org/showthread.php?t=1231182)  
[Bug #389555 - ext4 filesystem corruption](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/389555)

Well, I learned my lesson and ext{2|3|4} based filesystems are not going to be used on any of my Linux systems or customer installations in the future.

Addendum: I did not try this setup in other virtualization environments like VirtualBox, qemu, kvm, Xen, etc.

<small>Image credit: Daniel Vogel</small>