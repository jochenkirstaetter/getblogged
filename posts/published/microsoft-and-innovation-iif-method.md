---
uid: microsoft-and-innovation-iif-method
title: 'Microsoft and innovation: IIF() method'
slug: microsoft-and-innovation-iif-method
date: 2013-10-06
status: published
type: post
description: Microsoft keeps on re-inventing the wheel. Whether it is features from competitors or from its own products, like Visual FoxPro
tags:
- Development
keywords: Development
metaTitle: 'Microsoft and innovation: IIF() method'
metaDescription: Microsoft keeps on re-inventing the wheel. Whether it is features from competitors or from its own products, like Visual FoxPro
image: ''
ogTitle: 'Microsoft and innovation: IIF() method'
ogDescription: This Saturday I was watching a couple of eLearning videos from TrainSignal (thanks to the subscription I have with Pluralsight) on Querying Microsoft SQL Server 2012 (exam 70-461).
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/microsoft-and-innovation-iif-method/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2013-10-06T11:10:30Z
updatedAt: 2018-04-02T08:38:44Z
excerpt: This Saturday I was watching a couple of eLearning videos from TrainSignal (thanks to the subscription I have with Pluralsight) on Querying Microsoft SQL Server 2012 (exam 70-461).
twitterTitle: 'Microsoft and innovation: IIF() method'
twitterDescription: This Saturday I was watching a couple of eLearning videos from TrainSignal (thanks to the subscription I have with Pluralsight) on Querying Microsoft SQL Server 2012 (exam 70-461).
twitterImage: 
facebookTitle: 'Microsoft and innovation: IIF() method'
facebookDescription: This Saturday I was watching a couple of eLearning videos from TrainSignal (thanks to the subscription I have with Pluralsight) on Querying Microsoft SQL Server 2012 (exam 70-461).
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

This Saturday I was watching a couple of eLearning videos from [TrainSignal](https://www.trainsignal.com/) (thanks to the subscription I have with [Pluralsight](https://www.pluralsight.com/)) on [Querying Microsoft SQL Server 2012 (exam 70-461)](https://www.trainsignal.com/course/180/sql-server-2012-querying-70-461).

## []()'Innovation' by Microsoft

I kept myself busy learning 'new' things about Microsoft SQL Server 2012 and some best practices. It was incredible 'innovative' to see that there is an additional logic function called IIF() available now:

> Returns one of two values depending on the value of a logical expression.
>
> ```
> IIF(lExpression, eExpression1, eExpression2)
> ```

Ups, my bad... That's actually taken from the syntax [page of Visual FoxPro 9.0 SP 2](https://msdn.microsoft.com/en-us/library/7ttt15k6%28v=vs.80%29.aspx "IIF() method syntax in VFP"). And tada, at least seven (7+) years later, there's the recent [IIF() Transact-SQL version](https://technet.microsoft.com/en-us/library/hh213574.aspx "IIF() method in SQL Server 2012 Transact-SQL version") of that function:

> Returns one of two values, depending on whether the Boolean expression evaluates to true or false in SQL Server 2012.

> ```
> IIF ( boolean_expression, true_value, false_value )
> ```

Now, that's what I call innovation! But we all know what happened to Visual FoxPro... It has been reincarnated in form of Visual Studio LightSwitch (and SQL Server).

Enough ranting... Happy coding!
