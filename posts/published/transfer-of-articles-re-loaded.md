---
uid: transfer-of-articles-re-loaded
title: Transfer of articles re-loaded
slug: transfer-of-articles-re-loaded
date: 2008-02-24
status: published
type: post
description: Transfer of articles re-loaded Thanks to my reader&#39;s feedback I modified the conversion routine of the article transfer from the MySQL database to XML. As the content of this blog is now UTF-8 encoded my article content has to fullfil this as well. So, using VFP this takes just another
tags:
- General
keywords: General
metaTitle: Transfer of articles re-loaded
metaDescription: Transfer of articles re-loaded Thanks to my reader&#39;s feedback I modified the conversion routine of the article transfer from the MySQL database to XML. As the content of this blog is now UTF-8 encoded my article content has to fullfil this as well. So, using VFP this takes just another
image: ''
ogTitle: Transfer of articles re-loaded
ogDescription: Thanks to my reader's feedback I modified the conversion routine of the article transfer from the MySQL database to XML. As the content of this blog is now UTF-8 encoded my article content has to...
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
canonicalUrl: https://jochen.kirstaetter.name/transfer-of-articles-re-loaded/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2008-02-24T08:16:57Z
updatedAt: 2018-04-02T08:39:11Z
excerpt: Thanks to my reader's feedback I modified the conversion routine of the article transfer from the MySQL database to XML. As the content of this blog is now UTF-8 encoded my article content has to...
twitterTitle: Transfer of articles re-loaded
twitterDescription: Thanks to my reader's feedback I modified the conversion routine of the article transfer from the MySQL database to XML. As the content of this blog is now UTF-8 encoded my article content has to...
twitterImage: 
facebookTitle: Transfer of articles re-loaded
facebookDescription: Thanks to my reader's feedback I modified the conversion routine of the article transfer from the MySQL database to XML. As the content of this blog is now UTF-8 encoded my article content has to...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Thanks to my reader's feedback I modified the conversion routine of the article transfer from the MySQL database to XML. As the content of this blog is now UTF-8 encoded my article content has to fullfil this as well. So, using VFP this takes just another function call - Strconv() - with the right parameters.  
  
What I did is to change two lines of code in the XML template block for the output:  
```
<Content><<Strtran(Strconv(Strconv(Alltrim(p_summary),1),9), Chr(13)+Chr(10), "&"+"lt;br"+"&"+"gt;"+Chr(13)+Chr(10))>></Content><Title><<Strconv(Strconv(Alltrim(p_title),1),9)>></Title>
```

That's all. Strconv() converts characters into different encodings. You might have a look at the documentation in VFP's help file.  
  
  
Sincerely, JoKi
