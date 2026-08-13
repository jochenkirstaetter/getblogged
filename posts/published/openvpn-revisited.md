---
uid: openvpn-revisited
title: OpenVPN re-visited
slug: openvpn-revisited
date: 2018-08-28
status: published
type: post
description: Earlier versions of OpenVPN are vulnerable to SWEET32. The attack vector can be mitigated by changing the default cipher. OpenVPN currently recommends using AES-256-CBC or AES-128-CBC.
tags:
- Linux
- Personal
keywords: Linux, Personal
metaTitle: OpenVPN re-visited
metaDescription: Earlier versions of OpenVPN are vulnerable to SWEET32. The attack vector can be mitigated by changing the default cipher. OpenVPN currently recommends using AES-256-CBC or AES-128-CBC.
image: https://images.unsplash.com/photo-1508416163602-e4eb39645e86?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=df89fd00920df727218842cce7113c14
ogTitle: OpenVPN re-visited
ogDescription: Earlier versions of OpenVPN are vulnerable to SWEET32. The attack vector can be mitigated by changing the default cipher. OpenVPN currently recommends using AES-256-CBC or AES-128-CBC.
layout: post
bodyClass: post-template tag-linux tag-personal
postClass: post tag-linux tag-personal
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
canonicalUrl: https://jochen.kirstaetter.name/openvpn-revisited/
imageUrl: https://images.unsplash.com/photo-1508416163602-e4eb39645e86?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=df89fd00920df727218842cce7113c14
twitterImageUrl: https://images.unsplash.com/photo-1508416163602-e4eb39645e86?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=df89fd00920df727218842cce7113c14
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: https://images.unsplash.com/photo-1508416163602-e4eb39645e86?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=df89fd00920df727218842cce7113c14
featured: false
publishedAt: 2018-08-28T13:23:05Z
updatedAt: 2018-08-29T04:43:26Z
excerpt: Earlier versions of OpenVPN are vulnerable to SWEET32. The attack vector can be mitigated by changing the default cipher. OpenVPN currently recommends using AES-256-CBC or AES-128-CBC.
twitterTitle: OpenVPN re-visited
twitterDescription: Earlier versions of OpenVPN are vulnerable to SWEET32. The attack vector can be mitigated by changing the default cipher. OpenVPN currently recommends using AES-256-CBC or AES-128-CBC.
twitterImage: 
facebookTitle: OpenVPN re-visited
facebookDescription: Earlier versions of OpenVPN are vulnerable to SWEET32. The attack vector can be mitigated by changing the default cipher. OpenVPN currently recommends using AES-256-CBC or AES-128-CBC.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

It's been a very long time since I set up the VPN infrastructure at the office using OpenVPN. Today, I came across an interesting log entry that I would like to document quickly.

![OpenVPN is commonly used to establish virtual private networks world-wide](../content/images/2018/08/OpenVPN.png)

At the time of writing I have OpenVPN 2.4.6 running on my Windows 10 machine. The existing infrastructure though is on a different version, and this morning I observed the following entries in the log file:

```
Tue Aug 28 08:50:09 2018 WARNING: INSECURE cipher with block size less than 128 bit (64 bit).  This allows attacks like SWEET32.  Mitigate by using a --cipher with a larger block size (e.g. AES-256-CBC).
Tue Aug 28 08:50:09 2018 WARNING: INSECURE cipher with block size less than 128 bit (64 bit).  This allows attacks like SWEET32.  Mitigate by using a --cipher with a larger block size (e.g. AES-256-CBC).
Tue Aug 28 08:50:09 2018 WARNING: cipher with small block size in use, reducing reneg-bytes to 64MB to mitigate SWEET32 attacks.
```

Curious about those entries I found [Sweet32: Birthday attacks on 64-bit block ciphers in TLS and OpenVPN](https://sweet32.info/) as an informative reference on the documented vulnerabilities CVE-2016-2183 and CVE-2016-6329. There I found the connection back to OpenVPN. Which is also described on the official wiki: [OpenVPN and SWEET32](https://community.openvpn.net/openvpn/wiki/SWEET32)

> The default encryption for the transport protocol of OpenVPN is Blowfish – a 64-bit cipher – with the CBC mode.

Meaning, the default encryption of OpenVPN prior to version 2.4 is `BF-CBC` which doesn't provide enough security in recent times. Newer versions of OpenVPN though are using `AES-256-CBC` as default cipher.

## Upgrade your cipher suite and block size

For your own sake and safety of your network(s) you should check and change your OpenVPN infrastructure right away, and if needed upgrade your defined cipher to a more secure encryption and larger block size.

> OpenVPN users can change the cipher from the default Blowfish to AES

First, check which ciphers are available on your server and clients using the `--show-ciphers` option like so:

```
$ sudo openvpn --show-ciphers
The following ciphers and cipher modes are available
for use with OpenVPN.  Each cipher shown below may be
used as a parameter to the --cipher option.  The default
key size is shown as well as whether or not it can be
changed with the --keysize directive.  Using a CBC mode
is recommended.

DES-CBC 64 bit default key (fixed)
RC2-CBC 128 bit default key (variable)
DES-EDE-CBC 128 bit default key (fixed)
DES-EDE3-CBC 192 bit default key (fixed)
DESX-CBC 192 bit default key (fixed)
BF-CBC 128 bit default key (variable)
RC2-40-CBC 40 bit default key (variable)
CAST5-CBC 128 bit default key (variable)
RC2-64-CBC 64 bit default key (variable)
AES-128-CBC 128 bit default key (fixed)
AES-192-CBC 192 bit default key (fixed)
AES-256-CBC 256 bit default key (fixed)
CAMELLIA-128-CBC 128 bit default key (fixed)
CAMELLIA-192-CBC 192 bit default key (fixed)
CAMELLIA-256-CBC 256 bit default key (fixed)
SEED-CBC 128 bit default key (fixed)
```

Depending on your underlying Linux system the list might be more or less exhaustive. Have a look and then choose a key length of at least 128 bit.

> OpenVPN currently recommends using AES-256-CBC or AES-128-CBC.

Following the article on [OpenVPN and SWEET32](https://community.openvpn.net/openvpn/wiki/SWEET32) I chose to use `AES-256-CBC` cipher suite for my existing infrastructure. This seems to give me the largest compatibility between OpenVPN installations on various clients, including Raspberry Pi.

## Change your OpenVPN configuration

Independent of the OpenVPN version installed, you can specify the `cipher` directive in your configuration files - server and client likewise. Usually that directive is either not present or commented, meaning it uses the compiled default value. Change it to your needs like so:

```
# Select a cryptographic cipher.
# This config item must be copied to
# the client config file as well.
;cipher BF-CBC        # Blowfish (default)
;cipher AES-128-CBC   # AES
cipher AES-256-CBC
```

This needs to be applied on the OpenVPN server first as well as on all OpenVPN clients. Save your configuration file and reload the new settings.

```
$ sudo service openvpn reload
```

Perhaps, you might like to publish your updated client configuration file(s) a bit earlier. With the newly set cipher any connecting client will be rejected now, if the cipher suites do not match. Monitor your syslog output on the OpenVPN server for that kind of entries:

```
Aug 28 07:33:26 smtp ovpn-server[18351]: 1.2.3.4:47081 WARNING: 'cipher' is used inconsistently, local='cipher AES-256-CBC', remote='cipher BF-CBC'
Aug 28 07:33:26 smtp ovpn-server[18351]: 1.2.3.4:47081 WARNING: 'keysize' is used inconsistently, local='keysize 256', remote='keysize 128'
...
Aug 28 07:34:08 smtp ovpn-server[18351]: client/1.2.3.4:47081 Authenticate/Decrypt packet error: cipher final failed
```

This way you are able to find out which clients are still running on the previous configuration and therefore would need a little bit of assistance.

## Other OpenVPN appliances

Thanks to some of the clients of my company IOS Indian Ocean Software Ltd. it happens that I have to connect to their networks via VPN from time to time. Given the changed cipher of my own OpenVPN infrastructure I wanted to see what others are using.

According to my own article [Connecting Linux to WatchGuard Firebox SSL (OpenVPN client)](xref:connecting-linux-to-watchguard-firebox-ssl) one of the client configuration files reads like this:

```
cipher AES-256-CBC
```

Whereas for another client who is using a firewall from Sophos, the chosen cipher suite looks like this:

```
cipher AES-128-CBC
```

Well, looks like I'm in good company with my new option.

## Security is a process, not a state

Again, lesson learned. Although running services on Linux is mainly about setting them up properly at the beginning, it surely doesn't mean to forget about them in the long run. Regular reviews and audits help to mitigate newer issues and threats to your network infrastructure.

If you are an active OpenVPN user please use the comment section to share other security related configuration settings and hardening tips on OpenVPN. That would be much appreciated by myself and other readers. Thanks!
