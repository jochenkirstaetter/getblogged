---
uid: ghost-desktop-wont-start
title: Ghost Desktop on Xubuntu 17.04 won't start
slug: ghost-desktop-wont-start
date: 2017-08-08
status: published
type: post
description: Ghost Desktop won't start on Debian/Ubuntu via the application menu or any other GUI launcher. Check permissions to fix the issue.
tags:
- Linux
- Development
keywords: Linux, Development
metaTitle: Ghost Desktop on Xubuntu 17.04 won't start
metaDescription: Ghost Desktop won't start on Debian/Ubuntu via the application menu or any other GUI launcher. Check permissions to fix the issue.
image: content/images/2017/08/GhostDesktopApp.png
ogTitle: Ghost Desktop on Xubuntu 17.04 won't start
ogDescription: Ghost Desktop won't start on Debian/Ubuntu via the application menu or any other GUI launcher. Check permissions to fix the issue.
layout: post
bodyClass: post-template tag-linux tag-development
postClass: post tag-linux tag-development
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
canonicalUrl: https://jochen.kirstaetter.name/ghost-desktop-wont-start/
imageUrl: https://jochen.kirstaetter.name/content/images/2017/08/GhostDesktopApp.png
twitterImageUrl: https://jochen.kirstaetter.name/content/images/2017/08/GhostDesktopApp.png
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2017/08/GhostDesktopApp.png
featured: false
publishedAt: 2017-08-08T19:50:39Z
updatedAt: 2018-04-02T08:38:43Z
excerpt: Ghost Desktop won't start on Debian/Ubuntu via the application menu or any other GUI launcher. Check permissions to fix the issue.
twitterTitle: Ghost Desktop on Xubuntu 17.04 won't start
twitterDescription: Ghost Desktop won't start on Debian/Ubuntu via the application menu or any other GUI launcher. Check permissions to fix the issue.
twitterImage: 
facebookTitle: Ghost Desktop on Xubuntu 17.04 won't start
facebookDescription: Ghost Desktop won't start on Debian/Ubuntu via the application menu or any other GUI launcher. Check permissions to fix the issue.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Already before the [migration from Joomla to Ghost](xref:migration-joomla-ghost) last weekend I run the [Ghost Desktop](https://ghost.org/downloads/) application on Windows. Now, after the successful completion it was about time to get going on my other machines. You know, the ones away from the main rig... Usually used during the evening hours, just for fun, or experimenting.

Tonight, I decided to give one of my Linux systems some attention, started to upgrade some packages, and installed new software. Among those also [Ghost Desktop App for Linux](https://ghost.org/downloads/). On the Ghost website you get version 1.3.0 (as of writing), and it's a Debian package.

Knowing that the desktop app is an Electron-based application, and I already packaged a few Electron apps myself, it would run on any Ubuntu-based system, too.  
**Note:** This post was written in Ghost Desktop running on Xubuntu 17.04 64bit

## Installation of Ghost Desktop

Either you double-click on the downloaded .deb package and your system will prompt you to open/install the application in Software, or you can run the following command in the Terminal:

```
$ sudo dpkg -i ~/Downloads/ghost-desktop-1.3.0-debian.deb 
```

Ghost Desktop can then be launched via the Application Menu/Launcher under `ghost-desktop` or if you prefer the terminal:

```
$ Ghost
```

## The problem: Ghost Desktop won't start

If you try to launch the application via the menu or any other GUI launcher you won't get any response at all. The software just isn't executed, it seems.

Compared to running it in the Terminal. This might produce the following output:

```
$ Ghost
A JavaScript error occurred in the main process
Uncaught Exception:
Error: Unable to find a valid app
    at Object.<anonymous> (/usr/lib/Ghost/resources/electron.asar/browser/init.js:121:9)
    at Object.<anonymous> (/usr/lib/Ghost/resources/electron.asar/browser/init.js:173:3)
    at Module._compile (module.js:571:32)
    at Object.Module._extensions..js (module.js:580:10)
    at Module.load (module.js:488:32)
    at tryModuleLoad (module.js:447:12)
    at Function.Module._load (module.js:439:3)
    at Module.runMain (module.js:605:10)
    at run (bootstrap_node.js:424:7)
    at startup (bootstrap_node.js:147:9)
```

## The solution: Set permissions

Fortunately, this has been [reported already on GitHub](https://github.com/TryGhost/Ghost-Desktop/issues/274#issuecomment-312337145) by user [letsjustfixit](https://github.com/letsjustfixit). The issue is caused by a missing permission bit on the Electron `app`. A temporary workaround has been documented until the package is going to be fixed.

Run the following `chmod` to set read and execute bits on the Electron app and dependent components. Then launch Ghost Desktop again.

```
$ sudo chmod -R +rx /usr/lib/Ghost/resources/app
$ Ghost 

 ⚡️  Welcome to Ghost  👻

```

Happy blogging!

It's great to see that such issues are handled on GitHub, and the "fix" is easily done.

As maintainer of own Electron-based applications I'm interested in the root cause. So far, I didn't come across a similar problem (touching wood!). Thankfully, I'm going to add this to my notes on Electron.

If you're familiar with this kind of problem regarding Electron packaging on Linux, give it try to fix it. On my side, I already cloned the [Ghost-Desktop](https://github.com/TryGhost/Ghost-Desktop) repository. Let's see whether I'm able to create a pull request for the Ghost community.
