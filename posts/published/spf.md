---
uid: spf
title: 'Good to know: Sender Policy Framework'
date: 2014-12-12
status: published
type: post
description: The Sender Policy Framework (SPF) is an open standard specifying a technical method to prevent sender address forgery. More precisely, the current version of SPF — called SPFv1 or SPF Classic — protects the envelope sender address, which is used for the delivery of messages.
tags:
- Development
keywords: Development
metaTitle: 'Good to know: Sender Policy Framework'
metaDescription: The Sender Policy Framework (SPF) is an open standard specifying a technical method to prevent sender address forgery. More precisely, the current version of SPF — called SPFv1 or SPF Classic — protects the envelope sender address, which is used for the delivery of messages.
image: content/images/2014/12/photo-1485182708500-e8f1f318ba72.webp
ogImage: content/images/2014/12/photo-1485182708500-e8f1f318ba72-og.webp
ogTitle: 'Good to know: Sender Policy Framework'
ogDescription: Today, I ran into a "funny" situation where I got caught by my own mail server and DNS configuration. Actually, I'm referring to the Sender Policy Framework (SPF) and it disallowed that an email would...
layout: post
bodyClass: post-template tag-development
postClass: post tag-development
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
canonicalUrl: https://jochen.kirstaetter.name/spf/
imageUrl: content/images/2014/12/photo-1485182708500-e8f1f318ba72.webp
twitterImageUrl: https://images.unsplash.com/photo-1485182708500-e8f1f318ba72?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=19c3505de9f879d697ec3dfb142f2105
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2014/12/photo-1485182708500-e8f1f318ba72.webp
featured: false
publishedAt: 2014-12-12T16:03:07Z
updatedAt: 2018-04-02T08:38:43Z
excerpt: Today, I ran into a "funny" situation where I got caught by my own mail server and DNS configuration. Actually, I'm referring to the Sender Policy Framework (SPF) and it disallowed that an email would...
twitterTitle: 'Good to know: Sender Policy Framework'
twitterDescription: Today, I ran into a "funny" situation where I got caught by my own mail server and DNS configuration. Actually, I'm referring to the Sender Policy Framework (SPF) and it disallowed that an email would...
twitterImage: 
facebookTitle: 'Good to know: Sender Policy Framework'
facebookDescription: Today, I ran into a "funny" situation where I got caught by my own mail server and DNS configuration. Actually, I'm referring to the Sender Policy Framework (SPF) and it disallowed that an email would...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
[![Sender Policy Framework](../content/images/2014/12/spf-logo-medium.webp)](https://www.openspf.org/ "Sender Policy Framework")Today, I ran into a "funny" situation where I got caught by my own mail server and DNS configuration. Actually, I'm referring to the [Sender Policy Framework (SPF)](https://www.openspf.org/) and it disallowed that an email would have been delivered on my behalf.

## Delivery Status Notification

Earlier on I wanted to share a document on OneDrive with my client, and was surprised that he didn't get any invitation by email within the usual 5 to 10 minutes. Well, it turned out that the email had been declined with a Delivery Status Notification (SMTP 550):

```
Reporting-MTA: dns;DUB004-OMC2S4.hotmail.com
Received-From-MTA: dns;DUB131-DS14
Arrival-Date: Fri, 12 Dec 2014 03:22:13 -0800

Final-Recipient: rfc822;client@example.com
Action: failed
Status: 5.7.1
Diagnostic-Code: smtp;550 5.7.1 <client@example.com>: Recipient address rejected: Please see https://www.openspf.net/Why?s=mfrom;id=....
```

That's good!

## SPF is configured via DNS

Although SPF is used for mail transfers it is configured in the DNS records of a domain. There you should specify an SPF record, or at least a TXT record with similar content to this:

```
v=spf1 a mx a:kirstaetter.name ptr:smtp.kirstaetter.name mx:smtp.kirstaetter.name -all
```

The explanation of the various mechanisms for the configuration of an outbound mail server is available in the [Sender Policy Framework Record Syntax](https://www.openspf.org/SPF_Record_Syntax). And it is actually not too hard to learn and apply.

## Rather be safe than sorry

In case that you didn't configure SPF for your domain(s) yet. Please, go ahead and do yourself and mainly other internauts a favour and set-up your DNS records accordingly. It doesn't take that much time but improves your reputation as an outbound mail host.