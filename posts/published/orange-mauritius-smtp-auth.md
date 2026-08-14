---
uid: orange-mauritius-smtp-auth
title: Some mail details about Orange Mauritius
slug: orange-mauritius-smtp-auth
date: 2011-02-11
status: published
type: post
description: Being an internet service provider is not easy after all for a lot of companies. Luckily, there are quite some good international operators in this world.
tags:
- General
keywords: General
metaTitle: Some mail details about Orange Mauritius
metaDescription: Being an internet service provider is not easy after all for a lot of companies. Luckily, there are quite some good international operators in this world.
image: content/images/2011/02/photo-1518309913525-82928de3a51f.webp
ogTitle: Some mail details about Orange Mauritius
ogDescription: Being an internet service provider is not easy after all for a lot of companies. Luckily, there are quite some good international operators in this world. For example Orange Mauritius aka Mauritius...
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
canonicalUrl: https://jochen.kirstaetter.name/orange-mauritius-smtp-auth/
imageUrl: content/images/2011/02/photo-1518309913525-82928de3a51f.webp
twitterImageUrl: https://images.unsplash.com/photo-1518309913525-82928de3a51f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2011/02/photo-1518309913525-82928de3a51f.webp
featured: false
publishedAt: 2011-02-11T05:34:36Z
updatedAt: 2019-01-28T02:55:45Z
excerpt: Being an internet service provider is not easy after all for a lot of companies. Luckily, there are quite some good international operators in this world. For example Orange Mauritius aka Mauritius...
twitterTitle: Some mail details about Orange Mauritius
twitterDescription: Being an internet service provider is not easy after all for a lot of companies. Luckily, there are quite some good international operators in this world. For example Orange Mauritius aka Mauritius...
twitterImage: 
facebookTitle: Some mail details about Orange Mauritius
facebookDescription: Being an internet service provider is not easy after all for a lot of companies. Luckily, there are quite some good international operators in this world. For example Orange Mauritius aka Mauritius...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
imageAttribution: "Photo on Unsplash"
---
Being an internet service provider is not easy after all for a lot of companies. Luckily, there are quite some good international operators in this world. For example [Orange Mauritius](https://www.orange.mu/ "Orange Mauritius") aka [Mauritius Telecom](https://www.mauritiustelecom.com/ "Mauritius Telecom") aka Wanadoo(?) aka [MyT](https://www.mauritiustelecom.com/myt/ "MyT") here in Mauritius.

The local circumstances give them a quasi-monopol position on fixed lines for telephony and therefore cable-based DSL internet connectivity. So far, not bad but as usual... the details. Just for the records, I am only using the services of Orange for mobile but friends and customers are bound, eh stuck, with other services of Orange Mauritius. And usually, being the IT guy, they get in touch with me to complain about problems or to ask questions on either their ADSL / MyT connection, mail services or whatever. Most of those issues are user-related and easily to solve by tweaking the configuration of their computer a little bit but sometimes it's getting weird.

## Using Orange ADSL... somewhere else  
Now, let's imagine we are an Orange ADSL customer for ages and we are using their mail services with our very own mail address like "ficticious@intnet.mu". We configured our mail client like Thunderbird, Outlook Express, Outlook or Windows Mail as publicly described, and we are able to receive and send emails like a champion. No problems at all, the world is green. Did I mention that we have a laptop? Ok, let's take our movable piece of information technology and visit a friend here on the island. Not surprising, he is also customer of Orange, so we can read and answer emails. But Orange is not the online internet service provider and one day, we happen to hang out with someone that uses [Emtel via WiMAX or UMTS](https://www.emtel-ltd.com/data.php?category=13 "Emtel via WiMAX or UMTS")..

And the fun starts... We can still receive and read emails from our Orange mail account and the IT world is still bright but try to send mails to someone outside the domain "@intnet.mu" or "@orange.mu". Your mail client will deny sending mail with SMTP message 5.1.0 "blah not allowed". First guess, there is problem with the mail client, maybe magically the configuration changed over-night. But no it is still working at home... So, there is for sure a problem with the guy's internet connection. At least, it is his fault not to have Orange internet services, so it can not work properly...

## The Orange Mail FAQ  
After some more frustation we finally checkout the [Orange Mail FAQ](https://www.orange.mu/internet/faqs.php#faq3 "Orange Mail FAQ") to see whether this (obviously?) common problem has been described already. Sorry, but those FAQ entries are even more confusing as it is not really clear how to handle this scenario. Best of all is that most of the entries are still refering to use servers of the domain "intnet.mu". I mean Orange will disable those systems in favour of the domain "orange.mu" in the near future and does not amend their FAQs. Come on, guys!

Ok, settings for POP3 are there. Hm, what about the secure version POP3S? No signs at all... Even changing your mail client to use password encryption with STARTTLS is not allowed at all. Use "bow.intnet.mu" for incoming mail... Ahhh, pretty obvious host name. I mean, at least something like pop.intnet.mu or pop3.intnet.mu would have been more accurate. Funny of all, the hostname "pop.orange.mu" is accessible to receive your mail account. Alright, checking SMTP options for authentication or other like POP-before-SMTP or whatever well-known and established mechanism to send emails are described. I guess that spotting a whale or shark in Mauritian waters would be easier. Trial and error on SMTP settings reveal that neither STARTTLS or any other connection / password encryption is available. Using SSL/TLS on SMTP only reveals that there is no service answering your request.

## Calling customer service  
So, we have to bite into the bitter apple and get in touch with Orange customer service and complain/explain them our case and ask for advice. After some hiccups, we finally manage to get hold of someone competent in mail services and we receive the golden spoon of mail configuration made by Orange Mauritius:

SMTP hostname: **smtpauth.intnet.mu**

And the world of IT is surprisingly green again.

## Customer satisfaction?  
Dear Orange Mauritius, what's the problem with this information? Are you scared of mail spammer? Why isn't there any case in your FAQs?

Ok, talking about your FAQs - simply said: they are badly outdated!

Configure your mail client to use server name based in the domain intnet.mu but specify your account username with orange.mu as domain part. Although, that there are servers available on the domain orange.mu after all. So, why don't you provide current information like this:

POP3 server name: pop.orange.mu  
SMTP server name: smtp.orange.mu  
SMTP authenticated: smtpauth.orange.mu

It's not difficult, is it? In my humble opinion not really and you would provide clean, consistent and up-to-date information for your customers. This would produce less frustation and so less traffic on your customer service lines. Which after all, would improve the total user experience and satisfaction level on both sides.

Without knowing these facts. Now, imagine you would take your laptop abroad and have to use other internet service providers to be able to be online... Calling your customer service would be unnecessary expensive!

<small>Image credit: Kaitlyn Chow</small>