---
uid: openssh-on-windows
title: OpenSSH on Windows natively (Draft)
slug: openssh-on-windows
date: 2018-10-17
status: draft
type: post
description: Inspired by an article dubbed 'Installing OpenSSH on Windows 2012 R2 through PowerShell' by fellow blogger Nitin I had a closer at the current situation regarding OpenSSH on Windows 10.
tags:
- Windows
- Linux
- Development
keywords: Windows, Linux, Development
metaTitle: OpenSSH on Windows natively
metaDescription: Inspired by an article dubbed 'Installing OpenSSH on Windows 2012 R2 through PowerShell' by fellow blogger Nitin I had a closer at the current situation regarding OpenSSH on Windows 10.
image: ''
ogTitle: OpenSSH on Windows natively
ogDescription: Inspired by an article dubbed 'Installing OpenSSH on Windows 2012 R2 through PowerShell' by fellow blogger Nitin I had a closer at the current situation regarding OpenSSH on Windows 10.
layout: post
bodyClass: post-template tag-windows tag-linux tag-development
postClass: post tag-windows tag-linux tag-development
isPost: true
isPage: false
isDraft: true
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
canonicalUrl: https://jochen.kirstaetter.name/openssh-on-windows/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: ''
updatedAt: 2019-01-09T21:56:09Z
excerpt: Inspired by an article dubbed 'Installing OpenSSH on Windows 2012 R2 through PowerShell' by fellow blogger Nitin I had a closer at the current situation regarding OpenSSH on Windows 10.
twitterTitle: OpenSSH on Windows natively
twitterDescription: Inspired by an article dubbed 'Installing OpenSSH on Windows 2012 R2 through PowerShell' by fellow blogger Nitin I had a closer at the current situation regarding OpenSSH on Windows 10.
twitterImage: 
facebookTitle: OpenSSH on Windows natively
facebookDescription: Inspired by an article dubbed 'Installing OpenSSH on Windows 2012 R2 through PowerShell' by fellow blogger Nitin I had a closer at the current situation regarding OpenSSH on Windows 10.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Inspired by an article dubbed '[Installing OpenSSH on Windows 2012 R2 through PowerShell](https://tunnelix.com/installing-openssh-on-windows-2012-r2-through-powershell/)' by fellow blogger Nitin I had a closer at the current situation regarding OpenSSH on my Windows 10 systems.

Turns out that at least the client tools are actually pre-installed and available since the April update 2018.

# [Using the OpenSSH Beta in Windows 10 Fall Creators Update and Windows Server 1709](%20https://blogs.msdn.microsoft.com/powershell/2017/12/15/using-the-openssh-beta-in-windows-10-fall-creators-update-and-windows-server-1709/)

# [OpenSSH arrives in Windows 10 Spring Update](https://www.zdnet.com/article/openssh-arrives-in-windows-10-spring-update/)

## [*Open*SSH](https://www.openssh.com/index.html) [Manual Pages](https://www.openssh.com/manual.html)

## SSH client in Window Subsystem for Linux

```
jochen@IOSi7:~$ ssh -V
OpenSSH_7.6p1 Ubuntu-4ubuntu0.1, OpenSSL 1.0.2n  7 Dec 2017
```

## SSH client built into Windows 10

```
C:\Users\joki>ssh -V
OpenSSH_for_Windows_7.7p1, LibreSSL 2.6.5
```

```
C:\Users\joki>ssh
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
           [-i identity_file] [-J [user@]host[:port]] [-L address]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
           [-w local_tun[:remote_tun]] destination [command]

```