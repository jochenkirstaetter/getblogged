---
uid: alc4-slack-questions
title: ALC 4.0 Cloud - Slack questions
slug: alc4-slack-questions
date: 2019-08-10
status: published
type: post
description: A collection of questions that popped up in Slack recently. I'm going to give my opinion based on the knowledge I have gained so far. Surely, this is not going to be complete and there are different...
tags:
- Community
- Andela
keywords: Community, Andela
metaTitle: ALC 4.0 Cloud - Slack questions
metaDescription: A collection of questions that popped up in Slack recently. I'm going to give my opinion based on the knowledge I have gained so far. Surely, this is not going to be complete and there are different...
image: https://images.unsplash.com/photo-1531206715517-5c0ba140b2b8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
ogTitle: ALC 4.0 Cloud - Slack questions
ogDescription: A collection of questions that popped up in Slack recently. I'm going to give my opinion based on the knowledge I have gained so far. Surely, this is not going to be complete and there are different...
layout: post
bodyClass: post-template tag-community tag-andela
postClass: post tag-community tag-andela
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
canonicalUrl: https://jochen.kirstaetter.name/alc4-slack-questions/
imageUrl: https://images.unsplash.com/photo-1531206715517-5c0ba140b2b8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
twitterImageUrl: https://images.unsplash.com/photo-1531206715517-5c0ba140b2b8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: https://images.unsplash.com/photo-1531206715517-5c0ba140b2b8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
featured: false
publishedAt: 2019-08-10T08:49:18Z
updatedAt: 2019-09-03T18:46:48Z
excerpt: A collection of questions that popped up in Slack recently. I'm going to give my opinion based on the knowledge I have gained so far. Surely, this is not going to be complete and there are different...
twitterTitle: ALC 4.0 Cloud - Slack questions
twitterDescription: A collection of questions that popped up in Slack recently. I'm going to give my opinion based on the knowledge I have gained so far. Surely, this is not going to be complete and there are different...
twitterImage: 
facebookTitle: ALC 4.0 Cloud - Slack questions
facebookDescription: A collection of questions that popped up in Slack recently. I'm going to give my opinion based on the knowledge I have gained so far. Surely, this is not going to be complete and there are different...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

A collection of questions that popped up in Slack recently. I'm going to give my opinion based on the knowledge I have gained so far. Surely, this is not going to be complete and there are different experiences and points of view.

Feel free to join the conversation in the comment section below.

## The Questions...

> I got some questions if you don't mind  
1. What do you think of Microsoft Azure, AWS compared to GCP? (services they provide, security, availability e.t.c) Since you have an MVP in Azure.  
Since I see in your bio that you're a software craftsman:  
2.Could you please share your journey to software engineering?  
3. What advises you will give to people who are getting started in this field?  
4. If you're starting this journey today, what are the roadmaps or things you will do and don't do to becoming a software engineer?

*Update 03. September 2019*

> What can you say about the time you spent learning Microsoft Azure and the time you are now spending learning GCP?

## Azure or AWS or GCP?

Regarding Q1 I would like to clarify first that [I have been awarded Microsoft MVP](https://mvp.microsoft.com/en-US/MVP/profile/53d40e60-fe70-490e-8e73-2185b648f26f) in the category Developer Technologies. Additionally, I have successfully [passed various exams regarding Microsoft Azure](https://www.youracclaim.com/users/jkirstaetter/badges).

Coming back to the actual question. All cloud infrastructures are great and they all offer immense opportunities, features and functionality to address any kind of software related project. Personally, I'm quite familiar with [Microsoft Azure](https://azure.microsoft.com/) given the experience gained in contracted work for customers as well as a number of experiments over the past years. We have successfully conducted `Lift & Shift` operations for multiple clients. The flexibility of cloud infrastructure and services is superior in general.

As for [Google Cloud Platform (GCP)](https://cloud.google.com/) I have to admit that it is only since my participation in the ALC 4.0 program that I'm exploring this cloud platform. Before that, I did Azure only. My observations and activities in using GCP compared to Azure have been positive so far. My main obstacle at the beginning was to get into the naming conventions, eg. services and their features, and into the taxonomy of each. Overall it's a bit different to Azure - in a neutral sense - and it took me some time to disconnect my way of thinking and approaching certain aspects from Azure. Sometimes, I'm missing the Azure blade functionality in the web application but then it's solely about using the CLI and template approach to work with any cloud in a professional manner.

Using [Cloud Shell](https://cloud.google.com/shell/) or the [Cloud SDK](https://cloud.google.com/sdk/) locally gives you a sleek and powerful access point to operate your cloud resources. Tools like `gcloud`, `gsutil` and `bq` are really powerful and with the extensibility of components they give you a high grade of flexibility, too. Which is similar to Azure's tools, namely the PowerShell cmdlets and `azcli`.

Speaking of [Amazon Web Services (AWS)](https://aws.amazon.com/), well, I have to pass on this one. Until now, I did not explore any cloud services on AWS yet. Okay, I'm aware of features like S3 and others but I did not use of those AWS services in a contracted project or for any side-gig fun stuff. Looking forward to change that some day.

To wrap up my answer I would say that I'm currently still biased towards Azure. Although there are some aspects in GCP, like networking and resource tagging, that seem to be more intuitive and easier to use as it abstracts a lot of the design aspects of infrastructure planning from the user. It's a high level view on the project and it seems to work more smooth than resource groups in Azure.

Either way, my advice would be to explore all available cloud options and not to restrict yourself or your application to a single vendor. Given an architecture of microservices one should consider that they can run across multiple clouds in order to provide the best service and features compared to sticking to a single choice.

## My journey into software engineering

Answering Q2 is a short journey down memory lane as I officially started working as a professional software developer in April 1999. Although I was already writing software; mainly web development, back then already with JavaScript (and JScript) and bash scripts before that date, it marks the beginning of being a paid software developer. And for the record, I never attended any formalised courses on software engineering or computer science at the university. Actually, I studied a few years of [applied chemistry at the university](https://www.chemie.uni-kl.de/en/) before a lucrative job offer and cloudy future job prognosis in the chemical industry changed my mind.

From then on I enjoyed the daily learning experience and the satisfaction to actually create something other people would use in their daily activities. I have been involved in various customer-specific software projects that partly are still running nowadays. Around 2001 I got more involved with user groups and software communities. This and the development of a new product launch at my then employer also kicked off my activities in [public speaking](xref:speaking) in [2002](xref:speaker-at-the-german-visual-foxpro-developer-conference-2002). With increasing passion, deepening knowledge of the programming language and ongoing assistance in public forums I gratefully have been [awarded Microsoft Most Valuable Professional (MVP)](https://mvp.microsoft.com/en-US/MVP/profile/53d40e60-fe70-490e-8e73-2185b648f26f) first in 2006.

Learning never stopped for me and it's my motivation to discover something new every day.

## How to get started in this field?

Hmm, this is very personal and I can only share my own experience. Perhaps this might give you an indication what to look for...

First of all, find your inner voice and passion. Independently whether it is for a certain programming language, a field of technology, or solving problems in general to improve your or others daily struggle. It's that passion and drive that keeps you going every single day. And gives you the motivation to excel your own boundaries. Speaking of which, you should never doubt your dreams and ideas. They are achievable for you, maybe it might take a bit more time than anticipated, but keep going and you might be surprised about how much you can achieve over a certain period with continuous effort.

Start with the fundamentals. Get a solid understanding of good practices and principles in the field. And in this case I'm actually talking about the following:

- Learn how to **touch-type**.  
Seriously, with increased speed to manifest your thoughts into the computer you'll find it more satisfying at the end of the day than having to search every keystroke.
- Develop the ability to **read information properly**  
Referring back to the ALC 4.0 program and the amount of screenshots with clear error messages that have been posted, gave me to think about this trade.
- Explore **additional references**  
Don't stop at the material in front of you. Look for referred sources and additional content to dig deeper into a specific technology or concept. Do not settle with a status quo but ask for more. In lack of information run a search on relevant keywords and enjoy thousands of resources, ie. blog articles, documentation, forum threads, etc.
- **Practice**, practice, and practice more  
None of the grandmasters in any field were born with the ability to do great things. They all started at the basics and went through years of scrutinizing practice. This procedure also separates you from the mere mortal peers. Practice your skills every day. See yourself as a computer athlete and you might understand the approach.

Last but not least, don't let others tell you what you're capable of or not.

> The only frontiers are in your mind.

It is only you that possibly would be able to limit yourself. Nobody else.

## A revised roadmap

There is no universal answer to Q4 though. Again, I'm going to answer this given my own experience so far. If I would start a career in software engineering today...

I would lay out an actionable plan towards a very specific achievement. And then trace back all activities and effort involved into reaching that goal. Let's take my participation in the ALC 4.0 program as a reference. As described in answer #1 I joined the program for one particular reason only: To start with and learn more about the Google Cloud Platform. The current ultimate goal is to sit and pass at least one Google exam and to achieve a specific certification. Access to the video courses on Pluralsight and the sponsored access to the Qwiklabs are the foundation of this roadmap.

Over the past weeks, I noticed that some of my knowledge in Microsoft Azure and Linux in particular transpires nicely into GCP. This gave me a certain advantage compared to other learners in regards that I could focus more on the finer differences and advantages GCP offers than having to deal, *read: struggle*, with the basics of using Linux commands in Google Cloud Shell.

This means that creating a proficient knowledge of Linux should be placed onto that roadmap we started. According to a statement by Scott Hanselman back in October 2018 more than 50% of services on Azure are operated on Linux.

> Microsoft: “50% of Azure runs Linux.”  
Also Microsoft: \*releases DOS as open source under MIT\*[https://t.co/ETq4onW4Cs](https://t.co/ETq4onW4Cs)  
  
Clearly there’s only one conclusion! CLOUD-SCALE CONTAINERIZED DOS AS A SERVICE Y’ALL
>
> — Scott Hanselman (@shanselman) [October 3, 2018](https://twitter.com/shanselman/status/1047619111277146112?ref_src=twsrc%5Etfw)

Given the free (as in beer) access to the various Linux distributions one should definitely venture deeper into that area and sharpen a number of skills on the terminal. This shall be part of your fundamental knowledge in cloud computing.

Apart from this, I would again get in touch with local, regional and global user groups. The ability to meet on- and offline with other like-minded people in the field is invaluable to your career. You learn most by observing and watching other more experienced developers / engineers. They share their experiences and help you to avoid a good number of pitfalls in your personal growth. In case there is none in your surrounding reach out global to associations, like [Google Developer Groups](https://developers.google.com/community/gdg/) (GDG), [.NET Foundation](https://dotnetfoundation.org/), Microsoft, Mozilla, Atlassian, [openSUSE](https://www.opensuse.org/), etc. and probably start your own group. You might be surprised how this could evolve into something larger and beyond your best imagination.

**Dream big and go for it.**

And perhaps I might want to join at least one open source software (OSS) project on the internet, if time allows of course.

For sure I wouldn't settle with the ordinary. Whatever it might be, say a course curriculum, studies, a project assignment. Always strive to not only complete but to excel a task.

PS: FYI, I had to learn this kind of attitude. ;-)

## Time spent learning

For Azure it was an organic transition due to my daily software development activities. We started to develop solutions for Azure infrastructure and services. Some of our customers were interested to explore options to reduce cost and to modernize their IT landscape. It was a pragmatic approach to get work done.

Compared to the ALC 4.0 program where I'm solely exploring GCP and experimenting with the labs without having any actual business cases or customer requirements for the moment. As an organiser of GDG Mauritius however I'm looking forward to be able to host meetings on Google Cloud and perhaps run a few Cloud Study Jams in the weeks to come.

<small>Image courtesy: Perry Grone</small>
