---
uid: taking-web-sites-offline-for-demonstration-on-galaxy-tablet
title: Taking web sites offline for demonstration on Galaxy Tablet
slug: taking-web-sites-offline-for-demonstration-on-galaxy-tablet
date: 2012-10-29
status: published
type: post
description: Using an Android device like the Samsung Galaxy Tab 10.1 for offline demonstration of web sites or product catalogues
tags:
- Android
keywords: Android
metaTitle: Taking web sites offline for demonstration on Galaxy Tablet
metaDescription: Using an Android device like the Samsung Galaxy Tab 10.1 for offline demonstration of web sites or product catalogues
image: ''
ogTitle: Taking web sites offline for demonstration on Galaxy Tablet
ogDescription: 'This article is the Android sequel to the initial article about how to prepare an offline version of your web site for the purpose of demonstration or for exhibitions: Taking web sites offline for...'
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
authorImage: content/images/2018/10/JoKi_StAubin_100px.webp
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/taking-web-sites-offline-for-demonstration-on-galaxy-tablet/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2012-10-29T12:08:55Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: 'This article is the Android sequel to the initial article about how to prepare an offline version of your web site for the purpose of demonstration or for exhibitions: Taking web sites offline for...'
twitterTitle: Taking web sites offline for demonstration on Galaxy Tablet
twitterDescription: 'This article is the Android sequel to the initial article about how to prepare an offline version of your web site for the purpose of demonstration or for exhibitions: Taking web sites offline for...'
twitterImage: 
facebookTitle: Taking web sites offline for demonstration on Galaxy Tablet
facebookDescription: 'This article is the Android sequel to the initial article about how to prepare an offline version of your web site for the purpose of demonstration or for exhibitions: Taking web sites offline for...'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
This article is the Android sequel to the initial article about how to prepare an offline version of your web site for the purpose of demonstration or for exhibitions: [Taking web sites offline for demonstration](xref:taking-web-sites-offline-for-demonstration "Taking web sites offline for demonstration"). If you didn't read the original article, please take some minutes (5 to 10 maximum) to gain a better understanding on the following. Thanks.

I'm going to describe my steps using a Samsung Galaxy Tab 10.1 running on [Ice Cream Sandwich (ICS - version 4.0.4)](https://www.android.com/about/ice-cream-sandwich/ "Ice Cream Sandwich (ICS - version 4.0.4)") but I would assume that any other Android-based device will show more or less the same results.

## Put the prepared archive on your Android device

Well, the choice is yours... simply check out the Play Store for anything that looks like file manager, or explorer and you are up and running. Personally, I use either [ES File Explorer](https://play.google.com/store/apps/details?id=com.estrongs.android.pop "ES File Explorer") or [AirDroid](https://play.google.com/store/apps/details?id=com.sand.airdroid "AirDroid") to transfer files between my tablet and a PC or network, but any app is just fine! The Galaxy Tab doesn't have a slot for memory extensions but this could be an option, too.

After the succesful transfer, I simply extracted the archive in an accessible location and opened the start page of the web site, here index.html. In this case, ES File Explorer offers me to open the file with HTMLViewer, or even to create a Shortcut for faster access. Not too bad, but honestly that HTMLViewer app offers only limited functionality and doesn't provide any navigational buttons, like Back, Forward, Refresh, or Cancel. It's okay for a rough overview and quick check but it lacks some features.

## Know your paths

"Don't think you are, know you are." - Similar to the checks we previously did on the various desktop systems it is also possible to work with special URLs or better said protocols in this case: **file://**

While you are still in your favourite file explorer you should be able to get a proper location of your HTML files. Please, either memorize the path or note it down and open your favourite internet browser. This could be the stock 'Internet' or Chrome on ICS or higher, or Dolphin, or etc. Then you enter the location of your files prefixed with file://mnt/, like so:

```
file://mnt/sdcard/offline/index.html
```

if you are using the internal memory.  
In case of an external SD card or USB pen drive the absolute path might look like so:

```
file://mnt/extStorage/UsbDriveA/offline/index.html
```

Using an absolute URL to your offline HTML files allows you to browse them exactly the same way as if you navigate on a web site. There is no technical difference, and HTML/CSS/Javascript is just the same.

## Browser != Browser != Viewer

Don't be surprised if your offline web site appears differently on the various browser or viewer you are using. Following the same page various browser or viewer:

![Offline version shown in stock browser on ICS](https://s.kirstaetter.name/images/resortwork_android_browser.jpg "Offline version shown in stock browser on ICS")  
  
![Offline version shown in Chrome](https://s.kirstaetter.name/images/resortwork_android_chrome.jpg "Offline version shown in Chrome")  
  
![Offline version shown in HTMLViewer](https://s.kirstaetter.name/images/resortwork_android_htmlviewer.jpg "Offline version shown in HTMLViewer")

It's almost the same situation as on the desktop and there's room for interpretation of HTML and CSS - even on your Droid.

What are your experiences with creating or testing offline versions of web sites on your Android devices?

## Parallel universe: iOS

Eventually, you might be curious about this episode might be on a new iPad running on iOS 6. If so, please feel free to read this article: [Taking web sites offline for demonstration on iPad](xref:taking-web-sites-offline-for-demonstration-on-ipad "Taking web sites offline for demonstration on iPad")