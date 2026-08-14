---
uid: synergy-easy-share-of-keyboard-and-mouse-between-multiple-computers
title: Synergy - easy share of keyboard and mouse between multiple computers
slug: synergy-easy-share-of-keyboard-and-mouse-between-multiple-computers
date: 2012-07-23
status: published
type: post
description: An ode to Synergy - a tool that lets you easily share your mouse and keyboard between multiple computers on your desk, and it's Free and Open Source.
tags:
- General
keywords: General
metaTitle: Synergy - easy share of keyboard and mouse between multiple computers
metaDescription: An ode to Synergy - a tool that lets you easily share your mouse and keyboard between multiple computers on your desk, and it's Free and Open Source.
image: content/images/2018/02/synergy_banner.webp
ogTitle: Synergy - easy share of keyboard and mouse between multiple computers
ogDescription: Did you ever have the urge to share one set of keyboard and mouse between multiple machines? If so, please read on...
layout: post
bodyClass: post-template tag-general
postClass: post tag-general
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
canonicalUrl: https://jochen.kirstaetter.name/synergy-easy-share-of-keyboard-and-mouse-between-multiple-computers/
imageUrl: content/images/2018/02/synergy_banner.webp
twitterImageUrl: https://jochen.kirstaetter.name/content/images/2018/02/synergy_banner.png
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2018/02/synergy_banner.webp
featured: false
publishedAt: 2012-07-23T18:00:00Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Did you ever have the urge to share one set of keyboard and mouse between multiple machines? If so, please read on...
twitterTitle: Synergy - easy share of keyboard and mouse between multiple computers
twitterDescription: Did you ever have the urge to share one set of keyboard and mouse between multiple machines? If so, please read on...
twitterImage: 
facebookTitle: Synergy - easy share of keyboard and mouse between multiple computers
facebookDescription: Did you ever have the urge to share one set of keyboard and mouse between multiple machines? If so, please read on...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Did you ever have the urge to share one set of keyboard and mouse between multiple machines? If so, please read on...

## Using multiple machines

Honestly, as a software craftsman it is my daily business to run multiple machines - either physical or virtual - to be able to solve my customers' requirements. Recent hardware equipment allows this very easily. For laptops it's a no-brainer to attach a second or even a third screen in order to extend your native display. This works quite handy and in my case I used to attached two additional screens - one via HD15 connector, the other via HDMI. But... as it's a laptop and therefore a mobile unit there are slight restrictions. Detaching and re-attaching all cables when changing locations is one of them but hardware limitations, too. After all, it's a laptop and not a workstation.

I guess, that anyone working in IT (or ICT) has more than one machine at their workplace or their home office and at least I find it quite annoying to have multiple sets of keyboard and mouse conquering my remaining space on my desk. Despite the ugly looks of all those cables and whatsoever 'chaos of distraction' I prefer a more clean solution and working environment. This allows me to actually focus on my work and tasks to do rather than to worry about choosing the right combination of keyboard/mouse.

![JoKi's workspace since June 2012](https://s.kirstaetter.name/images/workspace_201207.jpg "JoKi's workspace since June 2012")

My current workplace is a patch work of various pieces of hardware (approx. 2-3 years):

- DIY desktop on [Ubuntu 12.04 64-bit](https://www.ubuntu.com/ "Ubuntu 12.04 64-bit"), Core2 Duo (E7400, 2.8GHz), 4GB RAM, 2x 250GB HDD, nVidia GPU 512MB
- Dell Inspiron 1525 on [Windows 8 64-bit](https://windows.microsoft.com/ "Windows 8 64-bit"), 4GB RAM, 200GB HDD
- HP Compaq 6720s on Windows Vista 32-bit, Core2 Duo (T5670, 1.8GHz), 2GB RAM, 160GB HDD
- Mac mini on [Mac OS X 10.7](https://www.apple.com/ "Mac OS X 10.7"), Core i5 (2.3 GHz), 2GB RAM, 500GB HDD

I know... Not the latest and greatest but a decent combination to work with. New system(s) is/are already on the shopping list but I live in the 'wrong' country to buy computer hardware. So, the next trip abroad will provide me with some new stuff.

## Using multiple operating systems

The list of hardware above already names different operating systems, and actually I have only one preference: Linux. But still my job as a software craftsman for Visual FoxPro and .NET development requires other OSes, too. Not a big deal, it's just like this. Additionally to those physical machines, there are a bunch of virtual machines around. Most of them running either Windows XP or Windows 7. Since years I have the practice that each development for one customer is isolated into its own virtual machine and environment. This keeps it clean and version-safe.

But as you can easily imagine with that setup there are a couple of constraints referring to keyboard and mouse. Usually, those systems require their own pieces of hardware attached. As stated, I don't like clutter on my desk's surface, so a cross-platform solution has to come in here. In the past, I tried it with various applications, hardware or network protocols like X11, RDP, NX, TeamViewer, RAdmin, KVM switch, etc. but the problem in this case is that they either allow you to remotely connect to the other system or exclusively 'bind' your peripherals to the active system. Not optimal after all.

## [Synergy](https://synergy-project.org/ "Synergy") to the rescue

Quote from their website: *"Synergy lets you easily share your mouse and keyboard between multiple computers on your desk, and it's Free and Open Source. Just move your mouse off the edge of one computer's screen on to another. You can even share all of your clipboards. All you need is a network connection. Synergy is cross-platform (works on Windows, Mac OS X and Linux)."*

Yep, that's it! All I need for my setup here...

Actually, I couldn't believe it myself that I didn't stumble over synergy earlier but 'Get over it' and there we go. And despite the fact that it is Open Source, no, it's also for free. Donations for the developers are very welcome and recently they introduced [Synergy Premium](https://synergy-foss.org/download/ "Synergy Premium"). A possibility to buy so-called premium votes that can be used to put more weight / importance on specific issues or bugs that you would like the developers to look into.

## Installation and configuration

Simply download the installation packages for your systems of choice, run the installer and enter some minor information about your network setup. I chose my desktop machine for the role of the Synergy server and configured my screen setup as follows:

![Configuration of machines in Synergy server](https://s.kirstaetter.name/images/synergy_server_screens.png "Configuration of machines in Synergy server")

The screen setup allows you currently to build or connect up to 15 machines. The number of screens can be higher as those machine might have multiple screens physically attached. Synergy takes this into the overall calculations and simply works as expected. I tried it for fun with a second monitor each connected to both laptops to have a total number of 6 active screens. No flaws after all - stunning!

All the other machines are configured as clients like so:

![Client configuration of Synergy, here Windows 8](https://s.kirstaetter.name/images/synergy_client_window.png "Client configuration of Synergy, here Windows 8")

Side note: The screenshot was taken on Windows 8 and pasted via clipboard into Gimp running on Ubuntu.

## Resume

Synergy is now definitely in my box of tools for my daily work, and amongst the first pieces of software I install after the operating system. It just simplifies my life and cleans my desk. Never again without Synergy!  
Now, only waiting for an Android version to integrate my Galaxy Tab 10.1, too. ;-)

Please, check out that superb product and enjoy sharing one keyboard, one mouse and one clipboard between your various machines and operating systems.