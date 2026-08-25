---
uid: alc4-cloud-challenge
title: ALC 4.0 Cloud Challenge I
date: 2019-10-18
status: published
type: post
description: Solving the Andela 4.0 Cloud Challenge described in multiple, individual steps
tags:
- Development
- Activity
- Andela
keywords: Development, Activity, Andela
metaTitle: ALC 4.0 Cloud Challenge I
metaDescription: Solving the Andela 4.0 Cloud Challenge described in multiple, individual steps
image: content/images/2019/10/alc4cloudchallengedns.webp
ogImage: content/images/2019/10/alc4cloudchallengedns-og.webp
ogTitle: ALC 4.0 Cloud Challenge I
ogDescription: Solving the Andela 4.0 Cloud Challenge described in multiple, individual steps
layout: post
bodyClass: post-template tag-development tag-activity tag-andela
postClass: post tag-development tag-activity tag-andela
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
canonicalUrl: https://jochen.kirstaetter.name/alc4-cloud-challenge/
imageUrl: content/images/2019/10/alc4cloudchallengedns.webp
twitterImageUrl: https://jochen.kirstaetter.name/content/images/2019/10/alc4cloudchallengedns.png
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2019/10/alc4cloudchallengedns.webp
featured: false
publishedAt: 2019-10-18T19:06:31Z
updatedAt: 2023-08-28T15:29:19Z
excerpt: Solving the Andela 4.0 Cloud Challenge described in multiple, individual steps
twitterTitle: ALC 4.0 Cloud Challenge I
twitterDescription: Solving the Andela 4.0 Cloud Challenge described in multiple, individual steps
twitterImage: 
facebookTitle: ALC 4.0 Cloud Challenge I
facebookDescription: Solving the Andela 4.0 Cloud Challenge described in multiple, individual steps
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Today I finally found a few chunks of time to run through the challenge. It was an interesting journey with some minor hiccups.

I documented all steps as a thread on Twitter, starting in the morning:

> Working on the current Google Cloud Challenge I[#100DaysOfExam](https://x.com/hashtag/100DaysOfExam?src=hash&ref_src=twsrc%5Etfw)[#150DaysOfALC4](https://x.com/hashtag/150DaysOfALC4?src=hash&ref_src=twsrc%5Etfw) [#GoogleAfricaDeveloperScholarship](https://x.com/hashtag/GoogleAfricaDeveloperScholarship?src=hash&ref_src=twsrc%5Etfw)  
  
✔ Create repo on GitHub  
✔ Create app  
✔ Init local git repo  
✔ Add GitHub remote  
✔ Push to master  
🐱‍🏍 Code...  
  
cc: [@andela_alc](https://x.com/andela_alc?ref_src=twsrc%5Etfw)
>
> — Jochen Kirstätter (JoKi) (@JKirstaetter) [October 18, 2019](https://x.com/JKirstaetter/status/1185021590947282945?ref_src=twsrc%5Etfw)

Consider the Twitter thread as a high-level roadmap that came together during the day while actually doing my daily chores in regards to contracted software development. The challenge was done in several chunks, almost identical to the content tweets.

The whole resulting implementation is publicly available on GitHub here: [https://github.com/jochenkirstaetter/andela-cloud-challenge](https://github.com/jochenkirstaetter/andela-cloud-challenge)

And the final result can be seen here: [https://alc4cloud.kirstaetter.name/](https://alc4cloud.kirstaetter.name/)

I'll see that I'll be able to document each of those steps in a blog article. With proper explanation, commands executed, errors observed and resolved, and a couple of extras I added to it. Have a look at the log/timeline in the GitHub repository...

## Break-down of the challenge

Given the amount of information and instructional steps the actual implementation is split into multiple articles.

- [Create React App](xref:alc4-cloud-react)
- [Working with Docker](xref:alc4-cloud-docker)
- [Google Kubernetes Engine (GKE)](xref:alc4-cloud-k8s)
- [Considerations for production readiness](xref:alc4-cloud-ready)

Each article can be read independently with minor references between each other.

## Bonus content

With the actual challenge completed I ventured into a few other options available on the Google Cloud Platform and wrote about it. This has been inspired by posts of other ALC 4.0 learners.

- [Working with Cloud Build](xref:alc4-cloud-build)
- [Using Cloud Run instead of GKE](xref:alc4-cloud-run)

Those articles describe alternative ways to build and deploy the React app on Google Cloud Platform.