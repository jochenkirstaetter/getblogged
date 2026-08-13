---
uid: configure-ipv6-on-ubuntu
title: Configure IPv6 on your Linux system (Ubuntu)
slug: configure-ipv6-on-ubuntu
date: 2014-03-10
status: published
type: post
description: Using IPv6 network addresses on your Linux system, here Ubuntu, is fairly easy to configure. This article will guide you through the basic steps.
tags:
- Linux
keywords: Linux
metaTitle: Configure IPv6 on your Linux system (Ubuntu)
metaDescription: Using IPv6 network addresses on your Linux system, here Ubuntu, is fairly easy to configure. This article will guide you through the basic steps.
image: https://images.unsplash.com/photo-1456428746267-a1756408f782?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=219d7355f55ac13fdf580c5222e76a54
ogTitle: Configure IPv6 on your Linux system (Ubuntu)
ogDescription: After the presentation on IPv6 at the first event of the Emtel Knowledge Series and some recent discussion on social media networks with other geeks and Linux interested IT people here in Mauritius, I...
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/configure-ipv6-on-ubuntu/
imageUrl: https://images.unsplash.com/photo-1456428746267-a1756408f782?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=219d7355f55ac13fdf580c5222e76a54
twitterImageUrl: https://images.unsplash.com/photo-1456428746267-a1756408f782?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=219d7355f55ac13fdf580c5222e76a54
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: https://images.unsplash.com/photo-1456428746267-a1756408f782?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=219d7355f55ac13fdf580c5222e76a54
featured: false
publishedAt: 2014-03-10T07:12:26Z
updatedAt: 2018-04-02T08:38:44Z
excerpt: After the presentation on IPv6 at the first event of the Emtel Knowledge Series and some recent discussion on social media networks with other geeks and Linux interested IT people here in Mauritius, I...
twitterTitle: Configure IPv6 on your Linux system (Ubuntu)
twitterDescription: After the presentation on IPv6 at the first event of the Emtel Knowledge Series and some recent discussion on social media networks with other geeks and Linux interested IT people here in Mauritius, I...
twitterImage: 
facebookTitle: Configure IPv6 on your Linux system (Ubuntu)
facebookDescription: After the presentation on IPv6 at the first event of the Emtel Knowledge Series and some recent discussion on social media networks with other geeks and Linux interested IT people here in Mauritius, I...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

After the presentation on IPv6 at the [first event of the Emtel Knowledge Series](https://jochen.kirstaetter.name/emtel-knowledge-series-no1/) and some recent discussion on social media networks with other geeks and Linux interested IT people here in Mauritius, I thought that I should give it a try (finally) and tweak my local network infrastructure. Honestly, I have been to busy with contractual project work and it never really occurred to me to set up IPv6 in my LAN. Well, the following paragraphs are going to shed some light on those aspects of modern computer and network technology.

This is the first article in a series on IPv6 configuration:

- [Configure IPv6 on your Linux system](https://jochen.kirstaetter.name/configure-ipv6-on-ubuntu/)
- [DHCPv6: Provide IPv6 information in your local network](https://jochen.kirstaetter.name/dhcpv6-ipv6-in-your-local-network/)
- [Enabling DNS for IPv6 infrastructure](https://jochen.kirstaetter.name/enabling-dns-for-ipv6-infrastructure/)
- [Accessing your web server via IPv6](https://jochen.kirstaetter.name/accessing-apache2-web-server-via-ipv6/)

**Piece of advice**: This is based on my findings on the internet while reading other people's helpful articles and going through a couple of man-pages on my local system.

## Let's embrace IPv6

The basic configuration on Linux is actually very simple as the kernel, operating system, and user-space programs support that protocol natively. If your system is ready to go for IP (aka: IPv4), then you are good to go for anything else. At least, I didn't have to install any additional packages on my system(s). We are going to assign a static IPv6 address to the system. Hence, we have to modify the definition of interfaces and check whether we have an inet6 entry specified. Open your favourite text editor and check the following entries (it should be at least similar to this):

```
$ sudo nano /etc/network/interfaces

auto eth0
# IPv4 configuration
iface eth0 inet static
  address 192.168.1.2
  network 192.168.1.0
  netmask 255.255.255.0
  broadcast 192.168.1.255

# IPv6 configuration
iface eth0 inet6 static
  pre-up modprobe ipv6
  address 2001:db8:bad:a55::2
  netmask 64
```

Of course, you might have to adjust your interface device (eth0) or you might be interested to have multiple directives for additional devices (eth1, eth2, etc.). The `auto` instruction takes care that your device is enabled and configured during the booting phase. The use of the pre-up directive depends on your kernel configuration but in most scenarios this might be an optional line. Anyways, it doesn't hurt to have it enabled after all - just to be on the safe side.

Next, either restart your network subsystem like so:

```
$ sudo service networking restart
```

Or you might prefer to do it manually with identical parameters, like so:

```
$ sudo ifconfig eth0 inet6 add 2001:db8:bad:a55::2/64
```

In case that you're logged in remotely into your PC (ie. via ssh), it is highly advised to opt for the second choice and add the device manually.

You can check your configuration afterwards with one of the following commands (depends on whether it is installed):

```
$ sudo ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 00:21:5a:50:d7:94  
          inet addr:192.168.160.2  Bcast:192.168.160.255  Mask:255.255.255.0
          inet6 addr: fe80::221:5aff:fe50:d794/64 Scope:Link
          inet6 addr: 2001:db8:bad:a55::2/64 Scope:Global
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1

$ sudo ip -6 address show eth0
3: eth0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qlen 1000
    inet6 2001:db8:bad:a55::2/64 scope global 
       valid_lft forever preferred_lft forever
    inet6 fe80::221:5aff:fe50:d794/64 scope link 
       valid_lft forever preferred_lft forever
```

In both cases, it confirms that our network device has been assigned a valid IPv6 address.

That's it in general for your setup on one system. But of course, you might be interested to enable more services for IPv6, especially if you're already running a couple of them in your IP network. More details are available on the [official Ubuntu Wiki](https://wiki.ubuntu.com/IPv6).

Continue to configure your network to [provide IPv6 address information automatically](https://jochen.kirstaetter.name/dhcpv6-ipv6-in-your-local-network/) in your local infrastructure.
