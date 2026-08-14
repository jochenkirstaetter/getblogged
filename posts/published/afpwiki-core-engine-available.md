---
uid: afpwiki-core-engine-available
title: AfpWiki Core Engine available
slug: afpwiki-core-engine-available
date: 2006-04-06
status: published
type: post
description: AfpWiki Core Engine available Hi,just published the core engine of AfpWiki. The code is reuseable for own purposes - whether it is web development or desktop development...Message from news://news.prolib.de/prolib.public.afp.englishHello AFP coderz,I&#39;d like to share my code fragments of the AfpWiki core engine with you all. Attached to this message you&#39;ll
tags:
- Development
keywords: Development
metaTitle: AfpWiki Core Engine available
metaDescription: AfpWiki Core Engine available Hi,just published the core engine of AfpWiki. The code is reuseable for own purposes - whether it is web development or desktop development...Message from news://news.prolib.de/prolib.public.afp.englishHello AFP coderz,I&#39;d like to share my code fragments of the AfpWiki core engine with you all. Attached to this message you&#39;ll
image: ''
ogTitle: AfpWiki Core Engine available
ogDescription: Hi,just published the core engine of AfpWiki. The code is reuseable for own purposes - whether it is web development or desktop development...Message from...
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
canonicalUrl: https://jochen.kirstaetter.name/afpwiki-core-engine-available/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-04-06T08:57:52Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: Hi,just published the core engine of AfpWiki. The code is reuseable for own purposes - whether it is web development or desktop development...Message from...
twitterTitle: AfpWiki Core Engine available
twitterDescription: Hi,just published the core engine of AfpWiki. The code is reuseable for own purposes - whether it is web development or desktop development...Message from...
twitterImage: 
facebookTitle: AfpWiki Core Engine available
facebookDescription: Hi,just published the core engine of AfpWiki. The code is reuseable for own purposes - whether it is web development or desktop development...Message from...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Hi,  
  
just published the core engine of AfpWiki. The code is reuseable for own purposes - whether it is web development or desktop development...  
  
Message from [news://news.prolib.de/prolib.public.afp.english](news://news.prolib.de/prlib.public.afp.english)  
  
Hello AFP coderz,  
  
I'd like to share my code fragments of the AfpWiki core engine with you  
all. Attached to this message you'll receive a ZIP archive with a sample  
and procedure file to run AfpWiki comparable solutions.  
  
It's a standalone sample and will be a sample of future releases of AFP.  
Just drop it into a web folder and call afpwiki.afp in your browser. This  
sample requires HTML Plugin for Active FoxPro Pages.  
  
If you're going to integrate the code in your existing AFP applications  
you have to do these steps:  
  
- Include the procedure file into your AFP application ([xxx.afpa.code]  
or [xxx.afp.code]):  
\*!&lt;[INCLUDE: "afpwiki.code"]&gt;  
  
- Call the function wikinize:  
m.lcValue = Wikinize(m.lcValue)  
  
The core engine is just the break down core engine of AfpWiki. It has no  
storage or versioning capabilities as AfpWiki provides.  
  
I would be very nice if you send in any questions and improvements on the  
code. Either send replies to this thread, or drop me a mail at  
[jochenk@prolib.de](mailto:jochenk@prolib.de) / [joki@afpfaq.de](mailto:joki@afpfaq.de)  
  
Disclaimer: The code is provided "as-is" and you are using it at your own  
risk. ;-)  
  
Kind regards, JoKi
