---
uid: install-adobe-air-on-ubuntu-linux
title: Install Adobe AIR on Ubuntu/Linux
slug: install-adobe-air-on-ubuntu-linux
date: 2010-03-19
status: published
type: post
description: Since quite some time Adobe Technologies released the Linux version of Adobe AIR to bring web applications and widgets to your desktop. Installing new applications on a Linux system is not always as easy as switching the computer on. The following instructions might be helpful to install Adobe AIR on any Linux system.
tags:
- Linux
keywords: Linux
metaTitle: Install Adobe AIR on Ubuntu/Linux
metaDescription: Since quite some time Adobe Technologies released the Linux version of Adobe AIR to bring web applications and widgets to your desktop. Installing new applications on a Linux system is not always as easy as switching the computer on. The following instructions might be helpful to install Adobe AIR on any Linux system.
image: content/images/2019/02/adobeair.webp
ogTitle: Install Adobe AIR on Ubuntu/Linux
ogDescription: Since quite some time Adobe Technologies released the Linux version of Adobe AIR to bring web applications and widgets to your desktop. Installing new applications on a Linux system is not always as...
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
canonicalUrl: https://jochen.kirstaetter.name/install-adobe-air-on-ubuntu-linux/
imageUrl: content/images/2019/02/adobeair.webp
twitterImageUrl: https://jochen.kirstaetter.name/content/images/2019/02/adobeair.png
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2019/02/adobeair.webp
featured: false
publishedAt: 2010-03-19T12:32:04Z
updatedAt: 2019-02-13T03:07:55Z
excerpt: Since quite some time Adobe Technologies released the Linux version of Adobe AIR to bring web applications and widgets to your desktop. Installing new applications on a Linux system is not always as...
twitterTitle: Install Adobe AIR on Ubuntu/Linux
twitterDescription: Since quite some time Adobe Technologies released the Linux version of Adobe AIR to bring web applications and widgets to your desktop. Installing new applications on a Linux system is not always as...
twitterImage: 
facebookTitle: Install Adobe AIR on Ubuntu/Linux
facebookDescription: Since quite some time Adobe Technologies released the Linux version of Adobe AIR to bring web applications and widgets to your desktop. Installing new applications on a Linux system is not always as...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Since quite some time Adobe Technologies released the Linux version of Adobe AIR to bring web applications and widgets to your desktop. Installing new applications on a Linux system is not always as easy as switching the computer on. The following instructions might be helpful to install Adobe AIR on any Linux system.

First of all, get the latest installer of [Adobe AIR](https://get.adobe.com/air/ "Installer of Adobe AIR") from https://get.adobe.com/air/ - as of writing this article the file name is **AdobeAIRInstaller.bin**. Save the download in your preferred folder.

Now, there are two ways to run the installer - visual style or console style.

## Visual Installation

Launch your favorite or standard file manager like thunar or nautilus and browse to the folder where the AdobeAIRInstaller.bin has been saved.

- Right click on the file and choose 'Properties' in the context menu
- Set 'Execute' permissions and confirm modifications with OK
- Rename file into AdobeAIRInstaller
- Double click and follow the instructions



## Using the console  
- Open a terminal like xterm
- Change into the directory where you stored the download
- Run this command:  
`chmod +x AdobeAIRInstaller.bin`
- Now run this command:  
`sudo ./AdobeAIRInstaller.bin`



The normal installer will open, install it. From now whenever you download a .air file, just double click it and it will be installed.

## Troubleshooting

In case that the installation does not start properly, try to install via console. This gives you more details about the reasons. Should you run into something like this:

`AdobeAIRInstaller.bin: 1: Syntax error: "(" unexpected`

Double check the execute permission of the installer file and try again.