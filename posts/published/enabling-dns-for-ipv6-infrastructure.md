---
uid: enabling-dns-for-ipv6-infrastructure
title: Enabling DNS for IPv6 infrastructure
slug: enabling-dns-for-ipv6-infrastructure
date: 2014-03-12
status: published
type: post
description: Usually, we would simply use host names in order to communicate with other machines instead of their bare IPv6 addresses. During the following paragraphs we are going to enable our own DNS name server with IPv6 address resolving.
tags:
- Linux
keywords: Linux
metaTitle: Enabling DNS for IPv6 infrastructure
metaDescription: Usually, we would simply use host names in order to communicate with other machines instead of their bare IPv6 addresses. During the following paragraphs we are going to enable our own DNS name server with IPv6 address resolving.
image: content/images/2014/03/photo-1494059980473-813e73ee784b.webp
ogTitle: Enabling DNS for IPv6 infrastructure
ogDescription: After successful automatic distribution of IPv6 address information via DHCPv6 in your local network it might be time to start offering some more services. Usually, we would use host names in order to...
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
canonicalUrl: https://jochen.kirstaetter.name/enabling-dns-for-ipv6-infrastructure/
imageUrl: content/images/2014/03/photo-1494059980473-813e73ee784b.webp
twitterImageUrl: https://images.unsplash.com/photo-1494059980473-813e73ee784b?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=9fdab1a5e303b06cfecf931f069fa3e9
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2014/03/photo-1494059980473-813e73ee784b.webp
featured: false
publishedAt: 2014-03-12T05:34:52Z
updatedAt: 2018-04-02T08:38:44Z
excerpt: After successful automatic distribution of IPv6 address information via DHCPv6 in your local network it might be time to start offering some more services. Usually, we would use host names in order to...
twitterTitle: Enabling DNS for IPv6 infrastructure
twitterDescription: After successful automatic distribution of IPv6 address information via DHCPv6 in your local network it might be time to start offering some more services. Usually, we would use host names in order to...
twitterImage: 
facebookTitle: Enabling DNS for IPv6 infrastructure
facebookDescription: After successful automatic distribution of IPv6 address information via DHCPv6 in your local network it might be time to start offering some more services. Usually, we would use host names in order to...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
After successful automatic distribution of IPv6 address information via DHCPv6 in your local network it might be time to start offering some more services. Usually, we would use host names in order to communicate with other machines instead of their bare IPv6 addresses. During the following paragraphs we are going to enable our own DNS name server with IPv6 address resolving.

- [Configure IPv6 on your Linux system](xref:configure-ipv6-on-ubuntu)
- [DHCPv6: Provide IPv6 information in your local network](xref:dhcpv6-ipv6-in-your-local-network)
- [Enabling DNS for IPv6 infrastructure](xref:enabling-dns-for-ipv6-infrastructure)
- [Accessing your web server via IPv6](xref:accessing-apache2-web-server-via-ipv6)

**Piece of advice**: This is based on my findings on the internet while reading other people's helpful articles and going through a couple of man-pages on my local system.

## What's your name and your IPv6 address?

```
$ sudo service bind9 status
 * bind9 is running
```

If the service is not recognised, you have to install it first on your system. This is done very easy and quickly like so:

```
$ sudo apt-get install bind9
```

Once again, there is no specialised package for IPv6. Just the regular application is good to go.

But of course, it is necessary to enable IPv6 binding in the options. Let's fire up a text editor and modify the configuration file.

```
$ sudo nano /etc/bind/named.conf.options

acl iosnet {
        127.0.0.1;
        192.168.1.0/24;
        ::1/128;
        2001:db8:bad:a55::/64;
};

listen-on { iosnet; };
listen-on-v6 { any; };

allow-query { iosnet; };
allow-transfer { iosnet; };
```

Most important directive is the `listen-on-v6`. This will enable your named to bind to your IPv6 addresses specified on your system. Easiest is to specify any as value, and named will bind to all available IPv6 addresses during start. More details and explanations are found in the man-pages of named.conf.

Save the file and restart the named service. As usual, check your log files and correct your configuration in case of any logged error messages. Using the `netstat` command you can validate whether the service is running and to which IP and IPv6 addresses it is bound to, like so:

```
$ sudo service bind9 restart
$ sudo netstat -lnptu | grep "named\W*$"
tcp        0      0 192.168.1.2:53        0.0.0.0:*               LISTEN      1734/named
tcp        0      0 127.0.0.1:53          0.0.0.0:*               LISTEN      1734/named
tcp6       0      0 :::53                 :::*                    LISTEN      1734/named
udp        0      0 192.168.1.2:53        0.0.0.0:*                           1734/named
udp        0      0 127.0.0.1:53          0.0.0.0:*                           1734/named
udp6       0      0 :::53                 :::*                                1734/named
```

Sweet! Okay, now it's about time to resolve host names and their assigned IPv6 addresses using our own DNS name server.

```
$ host -t aaaa www.6bone.net 2001:db8:bad:a55::2
Using domain server:
    Name: 2001:db8:bad:a55::2
    Address: 2001:db8:bad:a55::2#53
    Aliases: 
    
    www.6bone.net is an alias for 6bone.net.
    6bone.net has IPv6 address 2001:5c0:1000:10::2
```

Alright, our newly configured BIND named is fully operational.

Eventually, you might be more familiar with the dig command. Here is the same kind of IPv6 host name resolve but it will provide more details about that particular host as well as the domain in general.

```
$ dig @2001:db8:bad:a55::2 www.6bone.net. AAAA
```

More details on the Berkeley Internet Name Domain (bind) daemon and IPv6 are available in [Chapter 22.1 of Peter Bieringer's HOWTO on IPv6](https://tldp.org/HOWTO/html_single/Linux+IPv6-HOWTO/#HINTS-DAEMONS-BIND "Chapter 22.1 of Peter Bieringer's HOWTO on IPv6").

## Setting up your own DNS zone

Now, that we have an operational named in place, it's about time to implement and configure our own host names and IPv6 address resolving. The general approach is to create your own zone database below the bind folder and to add AAAA records for your hosts. In order to achieve this, we have to define the zone first in the configuration file named.conf.local.

```
$ sudo nano /etc/bind/named.conf.local

//
// Do any local configuration here
//
zone "ios.mu" {
        type master;
        file "/etc/bind/zones/db.ios.mu";
};
```

Here we specify the location of our zone database file. Next, we are going to create it and add our host names, our IP and our IPv6 addresses.

```
$ sudo nano /etc/bind/zones/db.ios.mu

$ORIGIN .
$TTL 259200     ; 3 days
ios.mu          IN SOA  ios.mu. hostmaster.ios.mu. (
                        2014031101 ; serial
                        28800      ; refresh (8 hours)
                        7200       ; retry (2 hours)
                        604800     ; expire (1 week)
                        86400      ; minimum (1 day)
                        )

NS      server.ios.mu.
$ORIGIN ios.mu.
server                  A       192.168.1.2
server                  AAAA    2001:db8:bad:a55::2
client1                 A       192.168.1.3
client1                 AAAA    2001:db8:bad:a55::3
client2                 A       192.168.1.4
client2                 AAAA    2001:db8:bad:a55::4
```

With a couple of machines in place, it's time to reload that new configuration.

**Note**: Each time you are going to change your zone databases you have to modify the serial information, too. Named loads the plain text zone definitions and converts them into an internal, indexed binary format to improve lookup performance. If you forget to change your serial then named will not use the new records from the text file but the indexed ones. Or you have to flush the index and force a reload of the zone.

This can be done easily by either restarting the named:

```
$ sudo service bind9 restart
```

or by reloading the configuration file using the name server control utility - `rndc`:

```
$ sudo rndc reconfig
```

Check your log files for any error messages and whether the new zone database has been accepted. Next, we are going to resolve a host name trying to get its IPv6 address like so:

```
$ host -t aaaa server.ios.mu. 2001:db8:bad:a55::2
Using domain server:
Name: 2001:db8:bad:a55::2
Address: 2001:db8:bad:a55::2#53
Aliases: 

server.ios.mu has IPv6 address 2001:db8:bad:a55::2
```

Looks good.

Alternatively, you could have just ping'd the system as well using the `ping6` command instead of the regular `ping`:

```
$ ping6 server
PING server(2001:db8:bad:a55::2) 56 data bytes
64 bytes from 2001:db8:bad:a55::2: icmp_seq=1 ttl=64 time=0.615 ms
64 bytes from 2001:db8:bad:a55::2: icmp_seq=2 ttl=64 time=0.407 ms
^C
--- ios1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 0.407/0.511/0.615/0.104 ms
```

That also looks promising to me. How about your configuration?

Next, it might be interesting to extend the range of available services on the network. One [essential service would be to have web sites](xref:accessing-apache2-web-server-via-ipv6) at hand.