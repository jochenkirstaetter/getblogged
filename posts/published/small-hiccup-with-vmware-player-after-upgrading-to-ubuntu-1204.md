---
uid: small-hiccup-with-vmware-player-after-upgrading-to-ubuntu-1204
title: Small hiccup with VMware Player after upgrading to Ubuntu 12.04
slug: small-hiccup-with-vmware-player-after-upgrading-to-ubuntu-1204
date: 2012-04-30
status: published
type: post
description: Comprehensive description to patch VMware Workstation 8 or Player 4 after upgrade of Ubuntu to 12.04 LTS (Precise Pangolin)
tags:
- Linux
keywords: Linux
metaTitle: Small hiccup with VMware Player after upgrading to Ubuntu 12.04
metaDescription: Comprehensive description to patch VMware Workstation 8 or Player 4 after upgrade of Ubuntu to 12.04 LTS (Precise Pangolin)
image: ''
ogTitle: Small hiccup with VMware Player after upgrading to Ubuntu 12.04
ogDescription: Finally, it was time to upgrade to a new LTS version of Ubuntu - 12.04 aka Precise Pangolin. I scheduled the weekend for this task and despite the nickname of Mauritius (Cyber Island) it took roughly...
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
canonicalUrl: https://jochen.kirstaetter.name/small-hiccup-with-vmware-player-after-upgrading-to-ubuntu-1204/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2012-04-30T05:43:32Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Finally, it was time to upgrade to a new LTS version of Ubuntu - 12.04 aka Precise Pangolin. I scheduled the weekend for this task and despite the nickname of Mauritius (Cyber Island) it took roughly...
twitterTitle: Small hiccup with VMware Player after upgrading to Ubuntu 12.04
twitterDescription: Finally, it was time to upgrade to a new LTS version of Ubuntu - 12.04 aka Precise Pangolin. I scheduled the weekend for this task and despite the nickname of Mauritius (Cyber Island) it took roughly...
twitterImage: 
facebookTitle: Small hiccup with VMware Player after upgrading to Ubuntu 12.04
facebookDescription: Finally, it was time to upgrade to a new LTS version of Ubuntu - 12.04 aka Precise Pangolin. I scheduled the weekend for this task and despite the nickname of Mauritius (Cyber Island) it took roughly...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
## The upgrade process  
Finally, it was time to upgrade to a new LTS version of [Ubuntu](https://www.ubuntu.com/ "https://www.ubuntu.com/ - Ubuntu") - 12.04 aka Precise Pangolin. I scheduled the weekend for this task and despite the nickname of Mauritius (Cyber Island) it took roughly 6 hours to download nearly 2.400 packages. No problem in general, as I have spare machines to work on, and it was weekend anyway. All went very smooth and only a few packages required manual attention due to local modifications in the configuration. With the new kernel 3.2.0-24 it was necessary to reboot the system and compared to the last upgrade, I got my graphical login as expected.

## Compilation of VMware Player 4.x fails

A quick test on the installed applications, Firefox, Thunderbird, Chromium, Skype, CrossOver, etc. reveils that everything is fine in general. Firing up VMware Player displays the known kernel mod dialog that requires to compile the modules for the newly booted kernel. Usually, this isn't a big issue but this time I was confronted with the situation that vmnet didn't compile as expected ("Failed to compile module vmnet"). Luckily, this issue is already well-known, even though with "Failed to compile module vmmon" as general reason but nevertheless it was very easy and quick to find the solution to this problem. In [VMware Communities](https://communities.vmware.com/message/1902218#1902218 "Patch for recent compilation issue") there are several forum threads related to this topic and VMware provides the necessary [patch file](https://communities.vmware.com/servlet/JiveServlet/download/1902218-80055/vmware802fixlinux320.tar.gz "Patch for VMware Workstation 8 or Player 4 on kernel 3.2.0") for Workstation 8.0.2 and Player 4.0.2. In case that you are still on Workstation 7.x or Player 3.x there is [another patch file](https://weltall.heliohost.org/wordpress/wp-content/uploads/2012/01/vmware715fixlinux320.tar.gz "Patch for Workstation 7 or Player 3 on kernel 3.2.0") available.

After download extract the file like so:

```
tar -xzvf vmware802fixlinux320.tar.gz  
```

and run the patch script as super-user:

```
sudo ./patch-modules_3.2.0.sh
```

This will alter the existing installation and source files of VMware Player on your machine.

As last step, which isn't described in many other resources, you have to restart the vmware service, or for the heart-fainted, just reboot your system:

```
sudo service vmware restart
```

This will load the newly created kernel modules into your userspace, and after that VMware Player will start as usual.

## Summary

Upgrading any derivate of Ubuntu, in my case Xubuntu, is quick and easy done but it might hold some surprises from time to time. Nonetheless, it is absolutely worthy to go for it. Currently, this patch for VMware is the only obstacle I had to face so far and my system feels and looks better than before. Happy upgrade!

## Resources

I used the following links based on Google search results:

[https://communities.vmware.com/message/1902218#1902218](https://communities.vmware.com/message/1902218#1902218)[  
https://weltall.heliohost.org/wordpress/2012/01/26/vmware-workstation-8-0-2-player-4-0-2-fix-for-linux-kernel-3-2-and-3-3/](https://weltall.heliohost.org/wordpress/2012/01/26/vmware-workstation-8-0-2-player-4-0-2-fix-for-linux-kernel-3-2-and-3-3/)

## Update on VMware Player 4.0.3

Please continue to read on [my follow-up article in case that you upgraded either VMware Workstation 8.0.3 or VMware Player 4.0.3](xref:update-kernel-patch-for-vmware-player-403 "How to patch and compile VMware Player 4.0.3 on kernel 3.2.0").

## Update on VMware Player 4.0.4

[And once again, please read on this article for VMware Player 4.0.4](xref:and-again-vmware-player-404-on-ubuntu-1204-precise-pangolin)

## Update on VMware Player 5.0.0

[Please read this article for VMware Player 5.0.0 in Ubuntu 12.10](xref:vmware-player-50-or-vmware-workstation-90-after-upgrade-to-ubuntu-1210 "Please read this article for VMware Player 5.0.0 in Ubuntu 12.10")
