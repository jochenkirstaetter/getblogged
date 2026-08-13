---
uid: nginx-reverse-proxy
title: Using nginx as reverse proxy
slug: nginx-reverse-proxy
date: 2019-01-08
status: published
type: post
description: 'Nginx (read: engine-x) has versatile options to set up web sites and more advanced configurations. This article explains briefly how to set up nginx as a reverse proxy to a web site in an internal network.'
tags:
- Linux
- Development
keywords: Linux, Development
metaTitle: Using nginx as reverse proxy
metaDescription: 'Nginx (read: engine-x) has versatile options to set up web sites and more advanced configurations. This article explains briefly how to set up nginx as a reverse proxy to a web site in an internal network.'
image: https://images.unsplash.com/photo-1521704042371-f13409bf0e6d?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
ogTitle: Using nginx as reverse proxy
ogDescription: 'Nginx (read: engine-x) has versatile options to set up web sites and more advanced configurations. This article explains briefly how to set up nginx as a reverse proxy to a web site in an internal network.'
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/nginx-reverse-proxy/
imageUrl: https://images.unsplash.com/photo-1521704042371-f13409bf0e6d?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
twitterImageUrl: https://images.unsplash.com/photo-1521704042371-f13409bf0e6d?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: https://images.unsplash.com/photo-1521704042371-f13409bf0e6d?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
featured: false
publishedAt: 2019-01-08T08:00:00Z
updatedAt: 2019-01-10T06:48:56Z
excerpt: 'Nginx (read: engine-x) has versatile options to set up web sites and more advanced configurations. This article explains briefly how to set up nginx as a reverse proxy to a web site in an internal network.'
twitterTitle: Using nginx as reverse proxy
twitterDescription: 'Nginx (read: engine-x) has versatile options to set up web sites and more advanced configurations. This article explains briefly how to set up nginx as a reverse proxy to a web site in an internal network.'
twitterImage: 
facebookTitle: Using nginx as reverse proxy
facebookDescription: 'Nginx (read: engine-x) has versatile options to set up web sites and more advanced configurations. This article explains briefly how to set up nginx as a reverse proxy to a web site in an internal network.'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Nginx (read: engine-x) has versatile options to set up web sites and more advanced configurations. This article explains briefly how to set up nginx as a reverse proxy to a web site in an internal network.

[NGINX](https://nginx.org/) is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server. Source: [https://www.nginx.com/resources/wiki/](https://www.nginx.com/resources/wiki/)

## The scenario

I have a web site running on a system in an internal network. This could be either a full-fledged Windows/Linux server or an IoT device running on a single board computer (SBC), like i.e. a Raspberry Pi, an Arduino, ESP8266 chipset.

![A reverse proxy taking requests from the Internet and forwarding them to servers in an internal network. Source: [Wikipedia](https://en.wikipedia.org/wiki/Reverse_proxy)](../content/images/2019/01/Reverse_proxy_h2g2bob.svg)

Now, I want to enable access from the Internet to that internal server using nginx.

## Setting up nginx

In order to set up the solution you need to have a public facing web server on the Internet. Most probably it already runs nginx to serve your web site or blogging software.

I'm running a root server on Debian/GNU Linux and nginx is already installed. You can check your own system quickly like so for any running process:

```
$ ps fax | grep nginx
```

Or if you prefer a bit more details like so:

```
$ sudo service nginx status
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
   Active: active (running) since Do 2019-01-03 03:28:11 CET; 4 days ago
     Docs: man:nginx(8)
  Process: 29505 ExecStop=/sbin/start-stop-daemon --quiet --stop --retry QUIT/5 --pidfile /run/nginx.pid (code=exited, status=0/SUCCESS)
  Process: 29537 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
  Process: 29535 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
 Main PID: 29539 (nginx)
   CGroup: /system.slice/nginx.service
           ├─29539 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           ├─29540 nginx: worker process
           ├─29541 nginx: worker process
           ├─29542 nginx: worker process
           └─29543 nginx: worker process
```

In case that nginx is not even installed on your system you could look up the package information like so:

```
$ apt search ^nginx
```

And install the web server using apt-get like so:

```
$ sudo apt-get install nginx-full
```

Which will then install nginx web/proxy server and all its dependencies on your server.

## Configuring nginx as reverse proxy

Now, we have an operational installation of nginx on our Internet-facing system. We are going to create a new configuration file that defines the necessary proxy information to access our service on the internal network.

First create a new file below nginx configuration folder using your preferred text editor.

```
$ cd /etc/nginx/sites-available/
$ sudo nano raspberry
```

The file name should be relevant to either the kind of services or the system that you are going to shield using nginx as proxy.

Next, write the following server definition into your configuration file. Of course, you would adjust the server name and the IP address according to your environment:

```
server {
    listen 80;
    listen [::]:80;
    
    server_name raspberry.kirstaetter.name;
    server_tokens off;

    location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass 10.0.240.3;
    }
}
```

That is the minimal configuration you would have to specify in order to run nginx as a reverse proxy to a system on your internal network. The given IP address needs to be accessible from your public web server, i.e. using a VPN infrastructure based on [OpenVPN](http://openvpn.net/).

After saving and closing the new nginx configuration it is time to enable and check the syntax for any errors. To enable an available configuration you need to either place it or link it into the folder `sites-enabled` of nginx.

```
$ cd ../sites-enabled
$ sudo ln -s /etc/nginx/sites-available/raspberry raspberry
```

Now, to avoid any unexpected shutdowns or better said launching issues you should *always* run a configuration test before restarting the nginx service. This can be done quickly using the following command:

```
$ sudo service nginx configtest
[ ok ] Testing nginx configuration:.
```

Should your configuration file have any unknown directives and errors the output of `configtest` looks like this:

```
$ sudo service nginx configtest
[FAIL] Testing nginx configuration: failed!
```

You will find more details about the nature of the problem and the line number in the error log file below /var/log, i.e. here:

```
$ sudo cat /var/log/nginx/error.log
2019/01/07 13:50:07 [emerg] 21662#21662: unknown directive "server_?name" in /etc/nginx/sites-enabled/raspberry:5
```

Only when all problems have been resolved and you have a positive response from the configtest you should restart the nginx service.

```
$ sudo service nginx restart
```

## Resolve a domain name

The above described sample is very basic, and sometimes it might be necessary to avoid using an IP address for internal service. Luckily, this can configured using the `resolver` directive in an nginx configuration file like so:

```
server {
    listen 80;
    listen [::]:80;
    
    server_name raspberry.kirstaetter.name;
    server_tokens off;

    resolver 127.0.0.1;
    
    location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass rasp01.local;
    }
}
```

The change in our configuration file now assumes that I have a DNS server running on the local machine which knows how to handle and resolve the specified domain name `rasp01.local`.

Again, this article covers the basics of reverse proxying using nginx only. There are more interesting scenario like setting your own DNS server on the internal network to provide public access to an internal resource.

Perhaps, you might want to proxy an existing service with your own custom domain, in case that the service provide does not offer this option. Using a public DNS server like [Cloudflare's 1.1.1.1](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/), [Google Public DNS](https://developers.google.com/speed/public-dns/) (8.8.8.8), or [OpenDNS](https://www.opendns.com/) as resolver should give you some ideas.

## Provide secure access using SSL

Let's take the following scenario into consideration. Your internal resource might not be configurable with an SSL certificate but you would like to enable HTTPS protocol communication from the Internet. Setting up nginx with an SSL certificate is well-documented and to combine this with the above described proxy features is a breeze to achieve.

Following you will get a more complete configuration file based on the previous example, now SSL-enabled using a Let's Encrypt certificate.

```
server {
    listen 80;
    listen [::]:80;
    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    server_name raspberry.kirstaetter.name;
    server_tokens off;
    server_name_in_redirect off;

    client_max_body_size 50m;

    ssl on;
    ssl_certificate         /etc/letsencrypt/live/raspberry.kirstaetter.name/fullchain.pem;
    ssl_certificate_key     /etc/letsencrypt/live/raspberry.kirstaetter.name/privkey.pem;

    # modern configuration. tweak to your needs.
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256';
    ssl_prefer_server_ciphers on;

    # HTTP headers
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-XSS-Protection "1; mode=block";
    add_header Referrer-Policy no-referrer-when-downgrade;

    root /var/www/raspberry;
    access_log /var/log/nginx/raspberry.kirstaetter.name.access_log gzip;
    error_log /var/log/nginx/raspberry.kirstaetter.name.error_log info;

    resolver 127.0.0.1;
    
    location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass rasp01.local;
    }

    location ~ /.well-known {
        allow all;
    }
}
```

The specified SSL options in regards to protocols and ciphers are an arbitrary choice of mine. If you have suggestions on how to improve the SSL setup, please leave a comment below.

Eventually the `http2` directive might be an issue. Either check that you are using a recent version of nginx that has HTTP/2 support backed in or remove the value from the `listen` directive in the configuration file.

## Multiple proxies

No problem with nginx. You can configure and run as many reverse proxies as would like to. Right now, I think I have three or four proxies running. Interestingly, one of them is an older set up based on Apache HTTP Server which I wrote about in a [Using Apache HTTP as reverse proxy](https://jochen.kirstaetter.name/apache-reverse-proxy/).

Do you have any interesting use cases or active configurations of nginx as reverse proxy? If yes, please use the comment section below give me and other readers more details. Thanks!

<small>Image credit: Otto Norin</small>
