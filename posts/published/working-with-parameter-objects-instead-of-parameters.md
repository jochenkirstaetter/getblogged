---
uid: working-with-parameter-objects-instead-of-parameters
title: Working with 'Parameter objects' instead of parameters
slug: working-with-parameter-objects-instead-of-parameters
date: 2008-06-04
status: published
type: post
description: Working with 'Parameter objects' instead of parameters Yesterday I stumbled over a good article in German language - Arbeiten mit Parameterobjekten - about using a parameter object rather than using parameters to pass information to functions and methods. As you know, I like this concept very much and actually already
tags:
- Development
keywords: Development
metaTitle: Working with 'Parameter objects' instead of parameters
metaDescription: Working with 'Parameter objects' instead of parameters Yesterday I stumbled over a good article in German language - Arbeiten mit Parameterobjekten - about using a parameter object rather than using parameters to pass information to functions and methods. As you know, I like this concept very much and actually already
image: ''
ogTitle: Working with 'Parameter objects' instead of parameters
ogDescription: Yesterday I stumbled over a good article in German language - Arbeiten mit Parameterobjekten - about using a parameter object rather than using parameters to pass information to functions and methods...
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
canonicalUrl: https://jochen.kirstaetter.name/working-with-parameter-objects-instead-of-parameters/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2008-06-04T05:53:14Z
updatedAt: 2018-04-02T08:39:11Z
excerpt: Yesterday I stumbled over a good article in German language - Arbeiten mit Parameterobjekten - about using a parameter object rather than using parameters to pass information to functions and methods...
twitterTitle: Working with 'Parameter objects' instead of parameters
twitterDescription: Yesterday I stumbled over a good article in German language - Arbeiten mit Parameterobjekten - about using a parameter object rather than using parameters to pass information to functions and methods...
twitterImage: 
facebookTitle: Working with 'Parameter objects' instead of parameters
facebookDescription: Yesterday I stumbled over a good article in German language - Arbeiten mit Parameterobjekten - about using a parameter object rather than using parameters to pass information to functions and methods...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Yesterday I stumbled over a good article in German language - [Arbeiten mit Parameterobjekten](https://tomsvfpblog.blogspot.com/2007/11/arbeiten-mit-parameterobjekten.html) - about using a parameter object rather than using parameters to pass information to functions and methods. As you know, I like this concept very much and actually already use it since years in my daily work. See also my other article on this: [Kommentar zu 'Parameterobjekte'](xref:working-with-parameter-objects-instead-of-parameters)  
  
Well, Tom uses blogger and because I don't have an account there I post my comments here in own 'blog space'. In his article Tom shows some code to transfer the value of the properties of the parameter object to the value properties of controls on the form. Well, I think that this could be way easier using the ControlSource property of the control directly. On the one hand the value is then bound to the parameter object and any changes are directly 'transferred' and on the other hand the concept saves you lots of code. Just configure the ControlSource of each control in the Property Window on the form and you are done. No extra code in Init or Destroy methods necessary.  
  
`Text1.ControlSource = Thisform.oParameters.StartDatum`  
  
In case of an error change the value of Thisform.BindControls = .F. and one of your last lines in the form Init method is to set the value to .T.  
  
  
Sincerely, JoKi