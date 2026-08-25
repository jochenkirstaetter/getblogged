---
uid: umts-mauritius
title: Using 3G/UMTS in Mauritius
date: 2010-10-20
status: published
type: post
description: how to setup, configure and use 3G/UMTS connections on Linux here in Mauritius. Personally, I can only share my experience with Emtel Ltd. but try to give some clues about how to configure Orange as well.
tags:
- Linux
keywords: Linux
metaTitle: Using 3G/UMTS in Mauritius
metaDescription: how to setup, configure and use 3G/UMTS connections on Linux here in Mauritius. Personally, I can only share my experience with Emtel Ltd. but try to give some clues about how to configure Orange as well.
image: ''
ogTitle: Using 3G/UMTS in Mauritius
ogDescription: After some conversation, threads in online forum and mailing lists I thought about writing this article on how to setup, configure and use 3G/UMTS connections on Linux here in Mauritius. Personally, I...
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
canonicalUrl: https://jochen.kirstaetter.name/umts-mauritius/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2010-10-20T08:12:17Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: After some conversation, threads in online forum and mailing lists I thought about writing this article on how to setup, configure and use 3G/UMTS connections on Linux here in Mauritius. Personally, I...
twitterTitle: Using 3G/UMTS in Mauritius
twitterDescription: After some conversation, threads in online forum and mailing lists I thought about writing this article on how to setup, configure and use 3G/UMTS connections on Linux here in Mauritius. Personally, I...
twitterImage: 
facebookTitle: Using 3G/UMTS in Mauritius
facebookDescription: After some conversation, threads in online forum and mailing lists I thought about writing this article on how to setup, configure and use 3G/UMTS connections on Linux here in Mauritius. Personally, I...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
After some conversation, threads in online forum and mailing lists I thought about writing this article on how to setup, configure and use 3G/UMTS connections on Linux here in Mauritius. Personally, I can only share my experience with Emtel Ltd. but try to give some clues about how to configure Orange as well.

### Emtel 3G/UMTS surf stick

Emtel provides different surf sticks from Huawei. Back in 2007, I started with an E220 that wouldn't run on Windows Vista either. Nowadays, you just plug in the surf stick (ie. E169) and usually the Network Manager will detect the new broadband modem. Nothing to worry about. The Linux Network Manager even provides a connection profile for Emtel here in Mauritius and establishing the Internet connection is done in less than 2 minutes... even quicker.

### Using wvdial

Old-fashioned Linux users might not take Network Manager into consideration but feel comfortable with wvdial. Although that wvdial is primarily used with serial port attached modems, it can operate on USB ports as well. Following is my configuration from /etc/wvdial.conf:

```
[Dialer Defaults]  
Phone = *99#  
Username = emtel  
Password = emtel  
New PPPD = yes  
Stupid Mode = 1  
Dial Command = ATDT  
  
[Dialer emtel]  
Modem = /dev/ttyUSB0  
Baud = 3774000  
Init2 = ATZ  
Init3 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0  
Init4 = AT+cgdcont=1,"ip","web"  
ISDN = 0  
Modem Type = Analog Modem  
```

The values of user name and password are optional and can be configured as you like. In case that your SIM card is protected by a pin - which is highly advised, you might another dialer section in your configuration file like so:

```
[Dialer pin]  
Modem = /dev/ttyUSB0  
Init1 = AT+CPIN=0000  
```

This way you can "daisy-chain" your command to establish your Internet connection like so:

wvdial pin emtel

And it works auto-magically.  
Depending on your group assignments (dialout), you might have to sudo the wvdial statement like so:

sudo wvdial pin emtel

### Orange parameters

As far as I could figure out without really testing it myself, it is also necessary to set the Access Point (AP) manually with Orange. Well, although it is pretty obvious a lot of people seem to struggle. The AP value is "orange".

```
[Dialer orange]  
Modem = /dev/ttyUSB0  
Baud = 3774000  
Init2 = ATZ  
Init3 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0  
Init4 = AT+cgdcont=1,"ip","orange"  
ISDN = 0  
Modem Type = Analog Modem  
```

And you are done.

### Official Linux support from providers

It's just simple: **Forget it!**

The people at the Emtel call center are completely focused on the hardware and Mobile Connect software application provided by Huawei and are totally lost in case that you confront them with other constellations. For example, my wife's netbook has an integrated 3G/UMTS modem from Ericsson. Therefore, no need to use the Huawei surf stick at all and of course we use the existing software named Wireless Manager instead of. Now, imagine to mention at the help desk: "Ehm, sorry but what's Mobile Connect?"

And Linux after all might give the call operator sleepless nights... Who knows?

Anyways, I hope that my article and configuration could give you a helping hand and that you will be able to connect your Linux box with 3G/UMTS surf sticks here in Mauritius.