---
uid: apache-reverse-proxy
title: Using Apache HTTP as reverse proxy
slug: apache-reverse-proxy
date: 2019-01-10
status: published
type: post
description: The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. This article explains briefly how to set up Apache as a reverse proxy to a web site in an internal network.
tags:
- Linux
- Development
keywords: Linux, Development
metaTitle: Using Apache HTTP as reverse proxy
metaDescription: The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. This article explains briefly how to set up Apache as a reverse proxy to a web site in an internal network.
image: content/images/2019/01/photo-1525081905268-fc0b46e9d786.webp
ogTitle: Using Apache HTTP as reverse proxy
ogDescription: The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. This article explains briefly how to set up Apache as a reverse proxy to a web site in an internal network.
layout: post
bodyClass: post-template tag-linux tag-development
postClass: post tag-linux tag-development
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
canonicalUrl: https://jochen.kirstaetter.name/apache-reverse-proxy/
imageUrl: content/images/2019/01/photo-1525081905268-fc0b46e9d786.webp
twitterImageUrl: https://images.unsplash.com/photo-1525081905268-fc0b46e9d786?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2019/01/photo-1525081905268-fc0b46e9d786.webp
featured: false
publishedAt: 2019-01-10T06:45:00Z
updatedAt: 2019-01-10T06:45:00Z
excerpt: The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. This article explains briefly how to set up Apache as a reverse proxy to a web site in an internal network.
twitterTitle: Using Apache HTTP as reverse proxy
twitterDescription: The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. This article explains briefly how to set up Apache as a reverse proxy to a web site in an internal network.
twitterImage: 
facebookTitle: Using Apache HTTP as reverse proxy
facebookDescription: The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. This article explains briefly how to set up Apache as a reverse proxy to a web site in an internal network.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. This article explains briefly how to set up Apache as a reverse proxy to a web site in an internal network.

To set the expectations in this article. I'm not going to explain you how to install Apache web server or how to get it operational on your system. There are [thousands of tutorials](http://bfy.tw/Lg5K) including my own [Accessing your web server via IPv6](xref:accessing-apache2-web-server-via-ipv6) on the Internet that already cover that step.

In case more information about the configuration directives used below is needed, I recommend to consult the [official documentation](https://httpd.apache.org/docs/2.4/) of a particular keyword.

## The scenario

I have a web site running on a system in an internal network. This could be either a full-fledged Windows/Linux server or an IoT device running on a single board computer (SBC), like i.e. a Raspberry Pi, an Arduino, ESP8266 chipset.

![A reverse proxy taking requests from the Internet and forwarding them to servers in an internal network. Source: [Wikipedia](https://en.wikipedia.org/wiki/Reverse_proxy)](../content/images/2019/01/Reverse_proxy_h2g2bob.svg)

Now, I want to enable access from the Internet to that internal server using Apache.

## Configuring Apache as reverse proxy

In order to complete our task we need to look into the features of the mod\_proxy module for Apache. Here, we get a directive called `ProxyPass` which does the job as expected. According to Apache's [Reverse Proxy Guide](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html) the simplest example proxies all requests (`"/"`) to a single backend:

```
ProxyPass "/"  "http://www.example.com/"
```

Additionally, to hide any reference to the system on the internal network it is required to specify the directive `ProxyPassReverse` to modify certain HTTP header values in the response, and use the proxy data instead.

Following is a working example of how to set up a virtual host in Apache that provides reverse proxy capabilities.

```
<VirtualHost *:80>
        ServerName mediacentre.kirstaetter.name

        ProxyRequests On
        ProxyPreserveHost On
        ProxyVia full

        <Proxy *>
                Order deny,allow
                Allow from all
        </Proxy>

        ProxyPass               /       http://10.0.240.4:8080/
        ProxyPassReverse        /       http://10.0.240.4:8080/
</VirtualHost>
```

The host system on IP address 10.0.240.4 is part of an OpenVPN infrastructure and therefore accessible from the proxy system.

## Multiple proxies possible

No problem with Apache. You can configure and run as many reverse proxies as would like to. One has to pay attention to avoid overlaps either via `ServerName` directive or by using different port numbers to bind to. Although I have only one reverse proxy running on Apache I configured multiple scenarios using nginx. More details are described in [Using nginx as reverse proxy](xref:nginx-reverse-proxy).

Do you have any interesting use cases or active configurations of Apache as reverse proxy? If yes, please use the comment section below give me and other readers more details. Thanks!

<small>Image credit: Nick Fewing</small>
