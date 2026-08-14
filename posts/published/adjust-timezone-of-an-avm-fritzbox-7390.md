---
uid: adjust-timezone-of-an-avm-fritzbox-7390
title: Adjust timezone of an AVM Fritz!Box 7390
slug: adjust-timezone-of-an-avm-fritzbox-7390
date: 2013-07-30
status: published
type: post
description: Lately, I had some spare time to address an issue in my Fritz!Box, and the following article describes how to adjust the timezone settings in general.
tags:
- General
keywords: General
metaTitle: Adjust timezone of an AVM Fritz!Box 7390
metaDescription: Lately, I had some spare time to address an issue in my Fritz!Box, and the following article describes how to adjust the timezone settings in general.
image: content/images/2013/07/photo-1519354754184-e1d9c46182c0.webp
ogTitle: Adjust timezone of an AVM Fritz!Box 7390
ogDescription: It's been a while that I purchased an AVM Fritz!Box 7390 but since I'm using this 'PABX' here in Mauritius, I'm not really happy about the wrong time in the logs or handsets connected. Lately, I had...
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
canonicalUrl: https://jochen.kirstaetter.name/adjust-timezone-of-an-avm-fritzbox-7390/
imageUrl: content/images/2013/07/photo-1519354754184-e1d9c46182c0.webp
twitterImageUrl: https://images.unsplash.com/photo-1519354754184-e1d9c46182c0?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2013/07/photo-1519354754184-e1d9c46182c0.webp
featured: false
publishedAt: 2013-07-30T04:19:16Z
updatedAt: 2019-01-07T22:39:54Z
excerpt: It's been a while that I purchased an AVM Fritz!Box 7390 but since I'm using this 'PABX' here in Mauritius, I'm not really happy about the wrong time in the logs or handsets connected. Lately, I had...
twitterTitle: Adjust timezone of an AVM Fritz!Box 7390
twitterDescription: It's been a while that I purchased an AVM Fritz!Box 7390 but since I'm using this 'PABX' here in Mauritius, I'm not really happy about the wrong time in the logs or handsets connected. Lately, I had...
twitterImage: 
facebookTitle: Adjust timezone of an AVM Fritz!Box 7390
facebookDescription: It's been a while that I purchased an AVM Fritz!Box 7390 but since I'm using this 'PABX' here in Mauritius, I'm not really happy about the wrong time in the logs or handsets connected. Lately, I had...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
It's been a while that I purchased an AVM Fritz!Box 7390 but since I'm using this 'PABX' here in Mauritius, I'm not really happy about the wrong time in the logs or handsets connected. Lately, I had some spare time to address this issue, and the following article describes how to adjust the timezone settings in general. The original idea came from an [FAQ found in c't 21/11](https://www.heise.de/ct/hotline/Fritzbox-in-anderer-Zeitzone-1344317.html "FAQ found in c't 21/11 - Fritzbox in anderer Zeitzone") (for a 7270 written in German language) but I added a couple of things based on other resources online.

The following tutorial may be valid for other models, too. Use your common sense and think before you act.

## []()Brief introduction to AVM Fritz!Box devices

The [Fritz!Box series of AVM](https://www.fritzbox.eu/ "Fritz!Box series of AVM") has been around for more than a decade and those little 'red boxes' have a high level of versatility for your small office or home.

> *High-speed connections, secure WLAN and convenient telephony make a home network out of any network. Whether it's a computer, tablet or smartphone, any device can be connected to the FRITZ!Box. And best of all, installation is so simple that users will be online in a matter of minutes.*

If you want to have peace of your mind in your small network then a Fritz!Box is the easiest way to achieve that. I'm using my box primarly as WiFi access point, VoIP gateway and media server but only because it came in second after my Linux system.

## []()Limitations in the administrative Web UI

Unfortunately, there are no possibilities to adjust the timezone settings in the Web UI at all - even not in Expert mode. I assume that this is part of the 'simplification' provided by AVM's design team. That's okay, as long as you reside in Central Europe, and the implicit time handling is correct for your location.

## []()Adjusting the timezone

I got my device through an order at Amazon Germany already some time ago, and honestly I wasn't bothered too much about the pre-configured (fixed) timezone setting - CET or CEST depending on daylight saving. But you know, it's that kind of splinter at the back of your head that keeps nagging and bothering you indirectly. So, finally I sat down yesterday evening and did a quick research on how to change the timezone. Even though there are a number of results, I read the FAQ from the c't magazine first, as I consider this as a trusted and safe source of information. Of course, it is most important to avoid to 'brick' your device.

## []()You've been warned - No support

Tinkering with the configuration of any AVM devices seems to be a violation of their official support channels. So, be warned and continue only in case that you're sure about what you are going to do. The following solutions are 'as-is' and they worked for my box flawlessly but may cause an issue in your case. Don't blame me...

## []()Solution 1 - Backup, modify and restore

That's the way as described in the c't article and a couple of other forum postings I found online, mainly from Australia. Login the administrative Web UI and navigate to 'System =&gt; Einstellungen sichern' (System =&gt; Backup configuration) and store your current configuration to a local file on your machine. Despite some online postings it is not necessary to specify a password in order to secure or encrypt your backup. IMHO, this only adds another unnecessary layer of complexity to the process. Anyway, next you should create a another copy of your settings and keep it unmodified. That's our safety net to restore the current settings in case that we might have to issue a factory setting reset to the box.

Now, open the configuration file with an advanced text editor which is capable to deal with Unix carriage returns properly - Windows Notepad doesn't do the job but Wordpad or Notepad++. Personally, I don't care and simply use geany, gedit or nano on Linux. In total there are 3 modifications that we have to apply to the configuration file - one new line and two adjustments.

First, we have to add an instruction near the top of file that overrides the device internal checksum validation. Without this line, your settings won't be accepted. Caution: The directives are case-sensitve and your outcome should read something like this:

> `**** FRITZ!Box Fon WLAN 7390 CONFIGURATION EXPORT`  
`Password=$$$$<ignore>`  
`FirmwareVersion=84.05.52`  
`CONFIG_INSTALL_TYPE=iks_16MB_xilinx_4eth_2ab_isdn_nt_te_pots_wlan_usb_host_dect_64415`  
`OEM=avm`  
`Country=049`  
`Language=de`  
**`NoChecks=yes`**  
`**** CFGFILE:ar7.cfg`  
`/*`  
` * /var/flash/ar7.cfg`  
` * Mon Jul 29 10:49:18 2013`  
` */`  
  
`ar7cfg {`  
`...`

Then search for the expression 'timezone' and you should find a section like this one (~ line 1113):

> `timezone_manual {`  
`        enabled = no;`  
`        offset = 0;`  
`        dst_enabled = no;`  
`        TZ_string = "";`  
`        name = "";`  
`}`

We would like to manually handle the timezone setting in our device and therefore we have to enable it and set the proper value for Mauritius. The configuration block should like so afterwards:

> `timezone_manual {`  
`        enabled = yes;`  
`        offset = 0;`  
`        dst_enabled = no;`  
`        TZ_string = "MUT-4";`  
`        name = "";`  
`}`

We specify the designation and the offset in hours of the timezone we would like to have. Caution: The offset indicates the value one has to add to the local time to arrive at UTC. More details are described in the [Explanation of TZ strings](https://www.di-mgt.com.au/wclock/tz.html#explain "Explanation of TZ strings"). Mauritius has GMT+4 which means that we have to substract 4 hours from the local time to have UTC.

Finally, we restore the modified configuration file via the administrative Web UI under 'System =&gt; Einstellungen sichern =&gt; Wiederherstellen' (System =&gt; Backup configuration =&gt; Restore). This triggers a reboot of the device, so please be patient and wait until the Web UI displays the login dialog again.

Good luck!

## []()Solution 2 - Telnet

**Update #1:** Thanks to a [comment made by Frank](/adjust-timezone-of-an-avm-fritzbox-7390#comment-2266663144) it should be noted that Telnet service seems to be removed starting firmware 6.30.

A more elegant, read: technically interesting, way to adjust configuration settings in your Fritz!Box is to access it directly through Telnet. By default AVM disables that protocol channel and you have to enable it with a connected telephone. In order to activate the telnet service dial the following combination:

> #96\*7\*
>
> #96\*8\* (to disable telnet again after work has been completed)

If you're using an AVM handset like the Fritz!Fon then you will receive a confirmation message on the display like so:

> telnetd ein

Next, depending on your favourite operating system, you either launch a Command prompt in Windows or a terminal in Linux, get your Admin password ready, and you connect to your box like so:

> $ telnet fritz.box
>
> Trying 192.168.1.1...  
Connected to fritz.box.  
Escape character is '^]'.  
password:  
  
  
BusyBox v1.19.3 (2012-10-12 14:52:09 CEST) built-in shell (ash)  
Enter 'help' for a list of built-in commands.  
  
ermittle die aktuelle TTY  
tty is "/dev/pts/0"  
Console Ausgaben auf dieses Terminal umgelenkt  
#

That's it, you are connected and we can continue to change the configuration manually. In order to adjust the timezone setting we have to open the ar7.cfg file. As we are now operating in a specialised environment, we only have limited capabilities at hand. One of those is a reduced version of vi - nvi. Let's open a second browser window with the [fine manual page of nvi](https://linux.die.net/man/1/nvi "fine manual page of nvi") and start to edit our configuration file:

> # nvi /var/flash/ar7.cfg

In our configuration file, we have to navigate to the timezone directives. The easiest way is to search for the expression 'timezone' by typing in the following:

> /timezone (press Enter/Return)

Now, we should see the exact lines of code like in the backed up version:

> timezone\_manual {  
enabled = no;  
offset = 0;  
dst\_enabled = no;  
TZ\_string = "";  
name = "";  
}

And of course, we apply the same changes as described in the previous section:

> timezone\_manual {  
enabled = **yes**;  
offset = 0;  
dst\_enabled = no;  
TZ\_string = "**MUT-4**";  
name = "";  
}

Finally, we have to write our changes back to the file and apply the new settings.

> :wq (press Enter/Return)
>
> # ar7cfgchanged

That's it! Finally, close the telnet session by pressing **Ctrl+]** and enter '**quit**'.

## []()Additional ideas...

There are a couple of more possibilities to enhance and to extend the usability of a Fritz!Box. There are lots of resources available on the net, but I'd like to name a few here. Especially for Linux users it is essential to be able to connect to any device remotely in a safe and secure way. And the [installation of a SSH server](https://www.64k-tec.de/2010/01/fritzbox-tuning-part-1-enable-remote-access-over-ssh/ "Enable remote access over ssh") on the box would be a first step to improve this situation, also to avoid to run telnet after all.

Sometimes, there might be problems in your VoIP connections, feel free to [adjust the settings of codecs](https://dandreadis.blogspot.com/2013/01/fritzbox-7360-hacks.html "adjust the settings of codecs") and connection handling, too.

I guess, you'll get the idea... The only frontiers are in your mind.