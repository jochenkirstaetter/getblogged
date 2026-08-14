---
uid: solaar-linux-logitech-unifying-receiver
title: Solaar - Managing Logitech Unifying Receiver peripherals
slug: solaar-linux-logitech-unifying-receiver
date: 2013-08-29
status: published
type: post
description: With Solaar you get access to the battery status and more configuration settings of your Logitech Unifying Receiver peripherals on Linux.
tags:
- Linux
keywords: Linux
metaTitle: Solaar - Managing Logitech Unifying Receiver peripherals
metaDescription: With Solaar you get access to the battery status and more configuration settings of your Logitech Unifying Receiver peripherals on Linux.
image: content/images/2013/08/photo-1503495731986-41d521ecbb32.webp
ogTitle: Solaar - Managing Logitech Unifying Receiver peripherals
ogDescription: "Despite the fact that I'm using Logitech products since ages it is only now that I accidentally came across a Linux application that allows me to configure their Unifying devices: Solaar"
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
canonicalUrl: https://jochen.kirstaetter.name/solaar-linux-logitech-unifying-receiver/
imageUrl: content/images/2013/08/photo-1503495731986-41d521ecbb32.webp
twitterImageUrl: https://images.unsplash.com/photo-1503495731986-41d521ecbb32?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2013/08/photo-1503495731986-41d521ecbb32.webp
featured: false
publishedAt: 2013-08-29T03:35:04Z
updatedAt: 2019-01-07T22:37:59Z
excerpt: "Despite the fact that I'm using Logitech products since ages it is only now that I accidentally came across a Linux application that allows me to configure their Unifying devices: Solaar"
twitterTitle: Solaar - Managing Logitech Unifying Receiver peripherals
twitterDescription: "Despite the fact that I'm using Logitech products since ages it is only now that I accidentally came across a Linux application that allows me to configure their Unifying devices: Solaar"
twitterImage: 
facebookTitle: Solaar - Managing Logitech Unifying Receiver peripherals
facebookDescription: "Despite the fact that I'm using Logitech products since ages it is only now that I accidentally came across a Linux application that allows me to configure their Unifying devices: Solaar"
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
Despite the fact that I'm using Logitech products since ages it is only now that I accidentally came across a Linux application that allows me to configure their Unifying devices: [Solaar](https://pwr.github.io/Solaar/index.html "Solaar")

> *Solaar is a Linux device manager for Logitech's [Unifying Receiver](https://logitech.com/en-us/66/6079 "Unifying Receiver") peripherals. It is able to pair/unpair devices to the receiver, and for most devices read battery status.*
>
> *It comes in two flavors, command-line and GUI. Both are able to list the devices paired to a Unifying Receiver, show detailed info for each device, and also pair/unpair supported devices with the receiver.*

Sounds great, or? And finally, the tool gives you some comfort compared to the existing application available for Windows or Mac OS, like battery status indicator or the ability to pair devices to the receiver you would like to have them (in case that you use multiple receiver at the same time).

![Solaar system tray indicator shows battery status of connected devices](../content/images/2013/08/solaar-traymenu.webp)  
*Solaar system tray indicator shows battery status of connected devices*

![Solaar displays the connected Logitech Unifying Receiver](../content/images/2013/08/solaar-receiver.webp)  
*Solaar displays the connected Logitech Unifying Receiver*

![Some Logitech devices can be configured with Solaar](../content/images/2013/08/solaar-config.webp)  
*Some Logitech devices can be configured with Solaar*

## []()Supported devices

I got my Laptop peripherals as part of a laptop set, namely K340 keyboard and M505 mouse, which are listed as supported devices. In case that you are not sure, check whether your USB hardware is supported by Solaar. You can check that by running the following in a console or terminal application:

`$ lsusb -d 046d:`  
`Bus 001 Device 005: ID 046d:c52b Logitech, Inc. Unifying Receiver`

The output should be similar to mine.

There is an extensive [list of supported devices and supported additional features](https://pwr.github.io/Solaar/devices.html "list of supported devices and supported additional features") on the Solaar site. Don't miss that one.

## []()Installation of Solaar

There are either pre-built packages for some distributions available or you can get the sources to compile it on your system. Have a look at GitHub for more details. Running Ubuntu (or any Ubuntu-based flavour) the installation is fairly easy. Add the existing PPA to your list of software repositories, update and install:

`$ sudo add-apt-repository ppa:daniel.pavel/solaar`  
`$ sudo apt-get update && sudo apt-get install solaar`

After that you'll have a new shortcut in the Accessories menu. On the first launch, I got a message that Solaar doesn't have the userrights to access the USB devices. Simply pull out your receivers and plug them back in - that resolves the issue.

## []()Console application

Solaar is both - a graphical tool as well as a console application. This might come in quite handy even though I'm not sure how. Anyway, you can get information about your Logitech devices, pair/unpair and configure your peripherals via solaar-cli command. Following is the output of my system:

`$ solaar-cli show`  
`Unifying Receiver [/dev/hidraw2:13F19F3F] with 2 devices`  
` 1: Wireless Mouse M505 [M505/B605:0255918D]  `  
`2: Wireless Keyboard K340 [K340:001074B7]`

Surprisingly, nothing that we didn't know already. The help switch (-h) provides a brief overview of what can be done.

Please, feel free to leave a comment about how solaar-cli could be helpful compared to the UI version of the tool.

## But what happened to dasKeyboard?

Read more about that in separate article about [How to choose the right keyboard for coding](xref:the-right-keyboard-for-coding "How to choose the right keyboard for coding").

**Solaar** is a Linux device manager for Logitech’s [Unifying Receiver](https://logitech.com/en-us/66/6079) peripherals. It is able to pair/unpair devices to the receiver, and for most devices read battery status.

It comes in two flavors, command-line and GUI. Both are able to list the devices paired to a Unifying Receiver, show detailed info for each device, and also pair/unpair supported devices with the receiver.
