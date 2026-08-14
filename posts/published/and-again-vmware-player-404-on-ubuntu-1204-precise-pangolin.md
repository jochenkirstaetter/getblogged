---
uid: and-again-vmware-player-404-on-ubuntu-1204-precise-pangolin
title: And again... VMware Player 4.0.4 on Ubuntu 12.04 (Precise Pangolin)
slug: and-again-vmware-player-404-on-ubuntu-1204-precise-pangolin
date: 2012-06-15
status: published
type: post
description: Even with the new version of VMware Player 4.0.4 you are still required to patch their sources. So, same game as last month.
tags:
- Linux
keywords: Linux
metaTitle: And again... VMware Player 4.0.4 on Ubuntu 12.04 (Precise Pangolin)
metaDescription: Even with the new version of VMware Player 4.0.4 you are still required to patch their sources. So, same game as last month.
image: ''
ogTitle: And again... VMware Player 4.0.4 on Ubuntu 12.04 (Precise Pangolin)
ogDescription: Even with the new version of VMware Player 4.0.4 you are still required to patch their sources. So, same game as last month. Just changing the value of the required version in the kernel patch script...
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
canonicalUrl: https://jochen.kirstaetter.name/and-again-vmware-player-404-on-ubuntu-1204-precise-pangolin/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2012-06-15T07:02:43Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Even with the new version of VMware Player 4.0.4 you are still required to patch their sources. So, same game as last month. Just changing the value of the required version in the kernel patch script...
twitterTitle: And again... VMware Player 4.0.4 on Ubuntu 12.04 (Precise Pangolin)
twitterDescription: Even with the new version of VMware Player 4.0.4 you are still required to patch their sources. So, same game as last month. Just changing the value of the required version in the kernel patch script...
twitterImage: 
facebookTitle: And again... VMware Player 4.0.4 on Ubuntu 12.04 (Precise Pangolin)
facebookDescription: Even with the new version of VMware Player 4.0.4 you are still required to patch their sources. So, same game as last month. Just changing the value of the required version in the kernel patch script...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Even with the new version of [VMware Player](https://www.vmware.com/products/player/overview.html "Desktop virtualization with VMware Player") 4.0.4 you are still required to patch their sources. [So, same game as last month.](xref:update-kernel-patch-for-vmware-player-403 "Update kernel patch for VMware Player 4.0.3") Just changing the value of the required version in the kernel patch script of Stefano Angeleri (weltall) and you are done:

```
nano patch-modules_3.2.0.sh
```

Please change line 8 at the top of the script like so:

```
plreqver=4.0.4
```

Save your modification and then run the following commands:

```
sudo rm /usr/lib/vmware/modules/source/.patched  
sudo ./patch-modules_3.2.0.sh  
sudo service vmware restart
```

And again, on first start VMware will present you their EULA which you have to accept, and everything gets back to normal operation mode.

Interestingly, one day ago the [Ubuntu](https://www.ubuntu.com/ "Ubuntu Linux") repositories provided a newer kernel version 3.2.0-25, so everything is running fine for now.
