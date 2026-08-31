---
uid: upgrade-to-wsl-2
title: Upgrade to WSL 2
date: 2020-06-16
status: draft
type: post
description: Windows PowerShellCopyright (C) Microsoft Corporation. All rights reserved.Try the new cross-platform PowerShell https://aka.ms/pscore6Loading personal and system profiles took 31979ms.PS...
tags: []
keywords: ''
metaTitle: Upgrade to WSL 2
metaDescription: Windows PowerShellCopyright (C) Microsoft Corporation. All rights reserved.Try the new cross-platform PowerShell https://aka.ms/pscore6Loading personal and system profiles took 31979ms.PS...
image: ''
ogTitle: Upgrade to WSL 2
ogDescription: Windows PowerShellCopyright (C) Microsoft Corporation. All rights reserved.Try the new cross-platform PowerShell https://aka.ms/pscore6Loading personal and system profiles took 31979ms.PS...
layout: post
bodyClass: post-template
postClass: post
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
canonicalUrl: https://jochen.kirstaetter.name/upgrade-to-wsl-2/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: ''
updatedAt: 2020-06-16T09:43:53Z
excerpt: Windows PowerShellCopyright (C) Microsoft Corporation. All rights reserved.Try the new cross-platform PowerShell https://aka.ms/pscore6Loading personal and system profiles took 31979ms.PS...
twitterTitle: Upgrade to WSL 2
twitterDescription: Windows PowerShellCopyright (C) Microsoft Corporation. All rights reserved.Try the new cross-platform PowerShell https://aka.ms/pscore6Loading personal and system profiles took 31979ms.PS...
twitterImage: 
facebookTitle: Upgrade to WSL 2
facebookDescription: Windows PowerShellCopyright (C) Microsoft Corporation. All rights reserved.Try the new cross-platform PowerShell https://aka.ms/pscore6Loading personal and system profiles took 31979ms.PS...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Windows PowerShell  
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell [https://aka.ms/pscore6](https://aka.ms/pscore6)

Loading personal and system profiles took 31979ms.  
PS D:\Source\Repos&gt; dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

Deployment Image Servicing and Management tool  
Version: 10.0.19041.329

Image Version: 10.0.19041.329

Enabling feature(s)  
[100.0%]  
The operation completed successfully.  
PS D:\Source\Repos&gt; dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

Deployment Image Servicing and Management tool  
Version: 10.0.19041.329

Image Version: 10.0.19041.329

Enabling feature(s)  
[100.0%]  
The operation completed successfully.  
PS D:\Source\Repos&gt; wsl --list --verbose  
NAME STATE VERSION

- Ubuntu-18.04 Stopped 1  
PS D:\Source\Repos&gt; wsl --set-default-version 2  
WSL 2 requires an update to its kernel component. For information please visit [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)  
PS D:\Source\Repos&gt; refreshenv  
Refreshing environment variables from the registry for powershell.exe. Please wait...  
Finished  
PS D:\Source\Repos&gt; wsl --set-default-version 2  
For information on key differences with WSL 2 please visit [https://aka.ms/wsl2](https://aka.ms/wsl2)  
PS D:\Source\Repos&gt; wsl --list --verbose  
NAME STATE VERSION
- Ubuntu-18.04 Stopped 1  
PS D:\Source\Repos&gt; wsl --set-version ubuntu 2  
There is no distribution with the supplied name.  
PS D:\Source\Repos&gt; wsl --set-version ubuntu-18.04 2  
Conversion in progress, this may take a few minutes...  
For information on key differences with WSL 2 please visit [https://aka.ms/wsl2](https://aka.ms/wsl2)  
Conversion complete.  
PS D:\Source\Repos&gt;