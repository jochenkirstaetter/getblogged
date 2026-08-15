---
uid: modified-hp-router
title: Modified HP Router
slug: modified-hp-router
date: 2010-01-30
status: published
type: post
description: This article provides some minor improvements to the Joomla! extension HP Router. Installation and modification is straight forward and no struggles at all.
tags:
- Development
keywords: Development
metaTitle: Modified HP Router
metaDescription: This article provides some minor improvements to the Joomla! extension HP Router. Installation and modification is straight forward and no struggles at all.
image: ''
ogTitle: Modified HP Router
ogDescription: 'While looking for some improvements of Joomla! native SEF engine I found the following extension quite interesting and easy to use: HP Router of Hannes Papenberg. Installation is straight forward and...'
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
canonicalUrl: https://jochen.kirstaetter.name/modified-hp-router/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2010-01-30T10:17:33Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: 'While looking for some improvements of Joomla! native SEF engine I found the following extension quite interesting and easy to use: HP Router of Hannes Papenberg. Installation is straight forward and...'
twitterTitle: Modified HP Router
twitterDescription: 'While looking for some improvements of Joomla! native SEF engine I found the following extension quite interesting and easy to use: HP Router of Hannes Papenberg. Installation is straight forward and...'
twitterImage: 
facebookTitle: Modified HP Router
facebookDescription: 'While looking for some improvements of Joomla! native SEF engine I found the following extension quite interesting and easy to use: HP Router of Hannes Papenberg. Installation is straight forward and...'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
While looking for some improvements of Joomla! native SEF engine I found the following extension quite interesting and easy to use: [HP Router](https://extensions.joomla.org/extensions/site-management/sef/5973) of Hannes Papenberg. Installation is straight forward and no struggles at all. For best results you might install this extension before starting any kind of search engine optimization for your website.

But after a short time I was confronted with some 'nasty' behaviour in my website that was introduced by this extension. Some articles did not show up properly and ended in an HTTP 404 error message. Well, actually reading the description of HP Router gave me an idea of the problem:

> ATTENTION!! There are a few things you have to keep in mind with this plugin:  
1. You can't have the same alias for two articles, even though they are in different categories. To be precise, you can't have the same alias for any type of content item. As a rule of thumb: If you can get to the list of this type of content items from the administrator menu, you can't use the same alias on two items in that list.

My 404 problem is directly caused by duplicated aliases... but not the obvious way!

The reason here is that the extension (as of writing this article) does not respect the state of the articles in the Joomla! CMS. And due to migration processing from previous blog databases I had a bunch of duplicated topics but deleted. This refers to state -2 instead of published content that has a state of 1.

To correct this problem it is necessary to modify two PHP files of the original HP Router:

- hprouter/com_contentrouter.php
- hprouter/com_contactrouter.php

Almost of the end of each file there are the SQL statements to query the database. After you made a backup of your two files you should change them like so:


```
$db =& JFactory::getDBO();  
if($vars['view'] == 'article')  
{  
$query = 'SELECT id FROM #__content WHERE **state = 1 AND** alias = '.$db->Quote($vars['id']);  
} elseif($vars['view'] == 'category') {
```


*Modified version of hprouter/com_contentrouter.php*


```
$db =& JFactory::getDBO();  
$query = 'SELECT id FROM #__contact_details WHERE **state = 1 AND** alias = '.$db->Quote($vars['id']);
```


*Modified version of hprouter/com_contactrouter.php*

With those modifications the HP Router works as expected and queries only published articles. Currently, I am not using the archive state of articles but in case that you will, just extend those two queries to include the necessary state values.