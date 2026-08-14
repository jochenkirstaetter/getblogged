---
uid: vmware-player-50-or-vmware-workstation-90-after-upgrade-to-ubuntu-1210
title: VMware Player 5.0 or VMware Workstation 9.0 after upgrade to Ubuntu 12.10
slug: vmware-player-50-or-vmware-workstation-90-after-upgrade-to-ubuntu-1210
date: 2012-10-23
status: published
type: post
description: Patching kernel 3.5.0 in Ubuntu 12.10 (Quantal Quetzal) to get VMware Player 5.x and VMware Workstation 9.x running.
tags:
- Linux
keywords: Linux
metaTitle: VMware Player 5.0 or VMware Workstation 9.0 after upgrade to Ubuntu 12.10
metaDescription: Patching kernel 3.5.0 in Ubuntu 12.10 (Quantal Quetzal) to get VMware Player 5.x and VMware Workstation 9.x running.
image: ''
ogTitle: VMware Player 5.0 or VMware Workstation 9.0 after upgrade to Ubuntu 12.10
ogDescription: 'Upgrading Ubuntu 12.04 to latest version 12.10 - aka Quantal Quetzal - is straight forward and you only need to follow the offical upgrade instructions. Short version on the console looks like this:'
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
canonicalUrl: https://jochen.kirstaetter.name/vmware-player-50-or-vmware-workstation-90-after-upgrade-to-ubuntu-1210/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2012-10-23T11:15:48Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: 'Upgrading Ubuntu 12.04 to latest version 12.10 - aka Quantal Quetzal - is straight forward and you only need to follow the offical upgrade instructions. Short version on the console looks like this:'
twitterTitle: VMware Player 5.0 or VMware Workstation 9.0 after upgrade to Ubuntu 12.10
twitterDescription: 'Upgrading Ubuntu 12.04 to latest version 12.10 - aka Quantal Quetzal - is straight forward and you only need to follow the offical upgrade instructions. Short version on the console looks like this:'
twitterImage: 
facebookTitle: VMware Player 5.0 or VMware Workstation 9.0 after upgrade to Ubuntu 12.10
facebookDescription: 'Upgrading Ubuntu 12.04 to latest version 12.10 - aka Quantal Quetzal - is straight forward and you only need to follow the offical upgrade instructions. Short version on the console looks like this:'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
## The upgrade process

Upgrading Ubuntu 12.04 to latest version 12.10 - aka [Quantal Quetzal](https://www.ubuntu.com/ubuntu/whats-new "Quantal Quetzal") - is straight forward and you only need to follow the offical upgrade instructions. Short version on the console looks like this:

```
sudo do-release-upgrade
```

This will update the repository entries, and start the upgrade process. After some minutes or hours of download and installation, you have to reboot your system once to get the new kernel loaded. As time of writing, I'm on '3.5.0-17-generic'. And as with any modification of the kernel version, you have to compile the necessary kernel modules to get VMware Player or Workstation up and running. Usually, this happens the first time you try start your VMware software and that's it. Well, again not so this time.

## Getting the kernel patch

Luckily, the community over VMware is very active and you can get a new kernel patch in the [online forums here](https://communities.vmware.com/message/2103172#2103172 "online forums here"). Get the download and put in a folder have write permissions. Then you extract the archive on the console like so:

```
tar -xjvf vmware9_kernel35_patch.tar.bz2
```

Then you change into the newly created folder:

```
cd vmware9_kernel3.5_patch/
```

And you execute the available shell script as root (superuser) like so:

```
sudo ./patch-modules_3.5.0.sh
```

This will stop any running instances of VMware software, patches the source files and runs the compile process for your active environment. This might take some time depending on your machine, and once completed you can start VMware Player or Workstation as previously.

In case that you are going to apply the patch again, the script will simply quit with the following output:

```
/usr/lib/vmware/modules/source/.patched found. You have already patched your sources. Exiting
```

You might remove the .patched file in case that you upgraded/changed your kernel and you need to apply the patch again.

Disclaimer: The patch is "as-is" and the patcher is originally created by Artem S. Tashkinov, and later modified by An\_tony. Please refer to the VMware forum in case of questions or problems. There are also patches available for older versions of VMware Player or Workstation.