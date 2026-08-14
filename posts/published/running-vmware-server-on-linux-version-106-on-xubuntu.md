---
uid: running-vmware-server-on-linux-version-106-on-xubuntu
title: Running VMware Server on Linux (version 1.0.6 on xubuntu)
slug: running-vmware-server-on-linux-version-106-on-xubuntu
date: 2008-06-03
status: published
type: post
description: Running VMware Server on Linux (version 1.0.6 on xubuntu) After the last article about Running VMware Player on Linux I thought that it would be very nice to be able to create new and modify existing machines. Ergo, let's try the latest version of VMware Server on the same machine.
tags:
- Linux
keywords: Linux
metaTitle: Running VMware Server on Linux (version 1.0.6 on xubuntu)
metaDescription: Running VMware Server on Linux (version 1.0.6 on xubuntu) After the last article about Running VMware Player on Linux I thought that it would be very nice to be able to create new and modify existing machines. Ergo, let's try the latest version of VMware Server on the same machine.
image: ''
ogTitle: Running VMware Server on Linux (version 1.0.6 on xubuntu)
ogDescription: After the last article about Running VMware Player on Linux I thought that it would be very nice to be able to create new and modify existing machines. Ergo, let's try the latest version of VMware...
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
canonicalUrl: https://jochen.kirstaetter.name/running-vmware-server-on-linux-version-106-on-xubuntu/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2008-06-03T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: After the last article about Running VMware Player on Linux I thought that it would be very nice to be able to create new and modify existing machines. Ergo, let's try the latest version of VMware...
twitterTitle: Running VMware Server on Linux (version 1.0.6 on xubuntu)
twitterDescription: After the last article about Running VMware Player on Linux I thought that it would be very nice to be able to create new and modify existing machines. Ergo, let's try the latest version of VMware...
twitterImage: 
facebookTitle: Running VMware Server on Linux (version 1.0.6 on xubuntu)
facebookDescription: After the last article about Running VMware Player on Linux I thought that it would be very nice to be able to create new and modify existing machines. Ergo, let's try the latest version of VMware...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
After the last article about [Running VMware Player on Linux](xref:running-vmware-player-on-linux-xubuntu-hardy-heron) I thought that it would be very nice to be able to create new and modify existing machines. Ergo, let's try the latest version of [VMware Server](https://register.vmware.com/content/download-106.html) on the same machine. Well, this installation doesn't need any modifications in source code but it is also not without pains.  
  
The main difference for sure is that the VMware server runs as a service - well, actually it is invoked by xinetd - and can be administrated locally and remotely. But let's focus on the installation first. As mentioned we need xinetd on our system. This is done via apt, aptitude or any other APT install client that you prefer:  
  
sudo apt-get install xinetd  
  
After that we just run the standard procedure. Unpacking the archive and running the installation script like so:  
  
tar xvzf VMware-server-1.0.6-91891.tar.gz  
cd vmware-server-distrib  
sudo ./vmware-install.pl  
  
The installation process is nearly the same as for the VMware Player. Additionally you have to agree the EULA and enter the serial number for the server. The serial number is provided by the registration on VMware's website.  
  
Alright, everything looks fine and we can try to fire up the VMware Server Console from the Applications :: System menu. In case that you don't get any reaction or feedback, open a terminal and run the command:  
  
vmware  
  
to see what's happening behind the scenes. I got several errors according to wrong version of gcc:  
  
/usr/lib/vmware/bin/vmware: /usr/lib/vmware/lib/libgcc_s.so.1/libgcc_s.so.1: version ` GCC_3.4' not found (required by /usr/lib/libcairo.so.2)<br />/usr/lib/vmware/bin/vmware: /usr/lib/vmware/lib/libgcc_s.so.1/libgcc_s.so.1: version  `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6)  
/usr/lib/vmware/bin/vmware: /usr/lib/vmware/lib/libgcc_s.so.1/libgcc_s.so.1: version ` GCC_3.4' not found (required by /usr/lib/libcairo.so.2)<br />/usr/lib/vmware/bin/vmware: /usr/lib/vmware/lib/libgcc_s.so.1/libgcc_s.so.1: version  `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6)  
/usr/lib/vmware/bin/vmware: /usr/lib/vmware/lib/libgcc_s.so.1/libgcc_s.so.1: version ` GCC_3.4' not found (required by /usr/lib/libcairo.so.2)<br />/usr/lib/vmware/bin/vmware: /usr/lib/vmware/lib/libgcc_s.so.1/libgcc_s.so.1: version  `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6)  
  
and therefore I did a short research on the web to find [a nice solution](https://communities.vmware.com/thread/148107):  
  
cd /usr/lib/vmware/lib/libgcc_s.so.1  
sudo mv libgcc_s.so.1 libgcc_s.so.1.org  
cd ../libpng12.so.0  
sudo mv libpng12.so.0 libpng12.so.0.org  
  
Attention: The destination paths on your system might vary depending on your entries during the installation procedure. Renaming the library files provides access to the existing library files of your Linux system.  
  
After this little tweak I could run the VMware Server Console directly from the console and from the menu without any problems. Now, it is your time to enjoy and operate your virtual machines with VMware Server.  
  
  
Sincerely, JoKi