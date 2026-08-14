---
uid: update-kernel-patch-for-vmware-player-403
title: Update kernel patch for VMware Player 4.0.3
slug: update-kernel-patch-for-vmware-player-403
date: 2012-05-04
status: published
type: post
description: Modifying the patch for VMware Player 4.0.2 to use it against Player 4.0.3 is no serious issue, just change the version indicator and run it.
tags:
- Linux
keywords: Linux
metaTitle: Update kernel patch for VMware Player 4.0.3
metaDescription: Modifying the patch for VMware Player 4.0.2 to use it against Player 4.0.3 is no serious issue, just change the version indicator and run it.
image: ''
ogTitle: Update kernel patch for VMware Player 4.0.3
ogDescription: As I stated some days ago, after upgrading to Ubuntu Precise Pangolin, aka 12.04 LTS, I had a minor obstacle with VMware products. Today, VMware offered to upgrade to Player 4.0.3 due to...
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
canonicalUrl: https://jochen.kirstaetter.name/update-kernel-patch-for-vmware-player-403/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2012-05-04T08:42:07Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: As I stated some days ago, after upgrading to Ubuntu Precise Pangolin, aka 12.04 LTS, I had a minor obstacle with VMware products. Today, VMware offered to upgrade to Player 4.0.3 due to...
twitterTitle: Update kernel patch for VMware Player 4.0.3
twitterDescription: As I stated some days ago, after upgrading to Ubuntu Precise Pangolin, aka 12.04 LTS, I had a minor obstacle with VMware products. Today, VMware offered to upgrade to Player 4.0.3 due to...
twitterImage: 
facebookTitle: Update kernel patch for VMware Player 4.0.3
facebookDescription: As I stated some days ago, after upgrading to Ubuntu Precise Pangolin, aka 12.04 LTS, I had a minor obstacle with VMware products. Today, VMware offered to upgrade to Player 4.0.3 due to...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
As [I stated some days ago](xref:small-hiccup-with-vmware-player-after-upgrading-to-ubuntu-1204 "Patch for kernel 3.2.0 to compile VMware Player 4.0.2"), after upgrading to [Ubuntu](https://www.ubuntu.com/) Precise Pangolin, aka 12.04 LTS, I had a minor obstacle with [VMware](https://www.vmware.com/) products. Today, VMware offered to upgrade to Player 4.0.3 due to security-related reasons.

Initially, I thought that this update might have the patch for kernel 3.2.0 integrated but sadly that is not the case.

## 'Hacking' the kernel patch

My first intuitive try to run the existing patch against the sources of VMware Player 4.0.3 failed, as the patch by Stefano Angeleri (weltall) is originally written explicitely against Workstation 8.0.2 and Player 4.0.2.

But this is nothing to worry about seriously. Just fire up your favourite editor of choice and modify the version signature for VMware Player, like so:

```
nano patch-modules_3.2.0.sh
```

And update line 8 for the new version:

```
plreqver=4.0.3
```

Save the shell script and run it as super-user (root):

```
sudo ./patch-modules_3.2.0.sh
```

In case that you previously patched your VMware sources you have to remove some artifacts beforehand. Otherwise, the patch script will inform you like so:

```
/usr/lib/vmware/modules/source/.patched found. You have already patched your sources. Exiting
```

In that case, simply remove the 'hidden' file and run the shell script again:

```
sudo rm /usr/lib/vmware/modules/source/.patched  
sudo ./patch-modules_3.2.0.sh
```

To finalise your installation either restart the vmware service or reboot your machine. On first start VMware will present you their EULA which you have to accept, and everything gets back to normal operation mode. Currently, I would assume that in case of VMware Workstation 8.0.3 you can follow the same steps as just described.

## Update on VMware Player 4.0.4

[Please read this article for VMware Player 4.0.4](xref:and-again-vmware-player-404-on-ubuntu-1204-precise-pangolin)

## Update on VMware Player 5.0.0

[Please read this article for VMware Player 5.0.0 in Ubuntu 12.10](xref:vmware-player-50-or-vmware-workstation-90-after-upgrade-to-ubuntu-1210 "Please read this article for VMware Player 5.0.0 in Ubuntu 12.10")
