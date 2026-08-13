---
uid: side-load-and-read-your-ebooks-on-kindle-for-android
title: Side-load and read your ebooks on Kindle for Android
slug: side-load-and-read-your-ebooks-on-kindle-for-android
date: 2013-04-25
status: published
type: post
description: Using the freely available Kindle reader apps allows to add and read any additional content, not only titles from the Kindle shop.
tags:
- Android
keywords: Android
metaTitle: Side-load and read your ebooks on Kindle for Android
metaDescription: Using the freely available Kindle reader apps allows to add and read any additional content, not only titles from the Kindle shop.
image: ''
ogTitle: Side-load and read your ebooks on Kindle for Android
ogDescription: ''
layout: post
bodyClass: post-template tag-android
postClass: post tag-android
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
canonicalUrl: https://jochen.kirstaetter.name/side-load-and-read-your-ebooks-on-kindle-for-android/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2013-04-25T07:47:49Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: ''
twitterTitle: Side-load and read your ebooks on Kindle for Android
twitterDescription: ''
twitterImage: 
facebookTitle: Side-load and read your ebooks on Kindle for Android
facebookDescription: ''
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

[![](https://jochen.kirstaetter.name/side-load-and-read-your-ebooks-on-kindle-for-android/images/joooid/side-load_and_read_your_ebooks_on_kindle_for_android_screenshot2013042514072711.jpg)](https://www.amazon.com/kindle "Amazon Kindle")

Although, I'm using the freely available [Kindle app for Android](https://play.google.com/store/apps/details?hl=en&id=com.amazon.kindle "Kindle for Android") it only happened recently that I run into the situation to upload an existing ebook in mobi format to my Android tablet. To be more precise, I purchased some titles from [O'Reilly's Ebook](https://shop.oreilly.com/category/ebooks.do "O'Reilly's Ebook") library.

## []()**Upload the ebook to your device**

Well, uploading the file wasn't really the problem. There are multiple apps in the Play Store which either allow you to access your existing network resources, like an SMB-based file share, FTP server or NAS, or turn your device into a server which can be accessed from your desktop machine via network. Just for matters of completion, I'm using ES File Explorer to access my NAS or run Air Droid to directly access my tablet through a browser. Anyway, there are tons of other apps to provide similar features. Maybe you leave a comment on your recommendations.

## []()**Where to store the ebook?**

So, while transferring the ebook to the device isn't really a challenge I started to wonder where to store the file actually? Does the Kindle app scan your directories and possibly include any ebook to its library found? Similar to the Gallery app. Initially, I was hoping for that as I put the file into my regular 'Downloads' folder. Firing up and sync'ing the Kindle app did not produce the expected book cover in my library. Of course, you might think...

Okay, second try: Using my favourite file explorer I browsed through the folder hierarchy on the device.  
This revealed that there are two potential candidates to store the file:

- /sdcard/kindle and  
- /sdcard/data/Android/com.amazon.kindle/files

## []()**Solution: /sdcard/kindle**

Actually, it turns out that the first one is the right one (read: better one) even though both seem to work. Simply copy your mobi-based ebook into that directory and then fire up your Kindle app for Android.  
Unfortunately, any side-loaded ebook is not synchronised with your Amazon Cloud storage and therefore will not appear on any of the other devices you might use to access your Kindle library. In my case, that's not a big deal mainly because I only use my tablet to read ebooks after all.

## []()**Alternative: Send an email to your Kindle account**

Frankly speaking, I haven't tried this approach (yet). The concept here is that Amazon provides a service called '[send to kindle](https://www.amazon.com/gp/sendtokindle/email "send to kindle")' which gives you an unique email address for your Kindle account and allows you to send any kind of documents (mobi, doc, pdf, etc) to yourself and it will be distributed to your Kindle devices and readers, like ie. Kindle app for Android.

Guess, I should give it a try and report soon about the experience.

### Update:

I just did a test run and sent a freely available ebook from [Project Gutenberg](https://www.gutenberg.org/ "Project Gutenberg") as an email attachment to one of my Kindle 'devices'. After a 'Sync & Check for Items' the new title appeared as expected in my library and was downloaded to the device. Unfortunately, it doesn't appear in the cloud library and therefore not on other devices or Kindle reader apps like on iOS or Windows 8. Sorry, my mistake. Eventually, I was too fast last time checking.

Documents sent via email to your Amazon Cloud storage are available on other Kindle devices and readers. At least, I am able to access them on Kindle for iOS on my iPad and the other Android devices. As for the Kindle app on Windows 8 it remains a problem to access those documents.

If you are more likely in the Apple universe, then please read on: [Side-load and read your mobi ebooks on Kindle for iOS](https://jochen.kirstaetter.name/side-load-and-read-your-mobi-ebooks-on-kindle-for-ios/)
