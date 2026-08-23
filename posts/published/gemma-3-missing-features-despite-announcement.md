---
uid: gemma-3-missing-features-despite-announcement
title: Gemma 3 - missing features despite announcement
slug: gemma-3-missing-features-despite-announcement
date: 2025-03-12
status: published
type: post
description: Congrats to the team to provide the new Gemma 3 models and the new endpoint on the Google AI API. The announcement blog - https://blog.google/technology/developers/gemma-3/ - reads wonderfully. Until...
tags:
- Development
keywords: Development
metaTitle: Gemma 3 - missing features despite announcement
metaDescription: Congrats to the team to provide the new Gemma 3 models and the new endpoint on the Google AI API. The announcement blog - https://blog.google/technology/developers/gemma-3/ - reads wonderfully. Until...
image: content/images/2025/03/Gemma3.webp
ogImage: content/images/2025/03/Gemma3-og.webp
ogTitle: Gemma 3 - missing features despite announcement
ogDescription: Congrats to the team to provide the new Gemma 3 models and the new endpoint on the Google AI API. The announcement blog - https://blog.google/technology/developers/gemma-3/ - reads wonderfully. Until...
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
canonicalUrl: https://jochen.kirstaetter.name/gemma-3-missing-features-despite-announcement/
imageUrl: content/images/2025/03/Gemma3.webp
twitterImageUrl: https://jochen.kirstaetter.name/content/images/2025/03/Gemma3.png
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2025/03/Gemma3.webp
featured: false
publishedAt: 2025-03-12T04:45:00Z
updatedAt: 2025-03-25T04:45:55Z
excerpt: Congrats to the team to provide the new Gemma 3 models and the new endpoint on the Google AI API. The announcement blog - https://blog.google/technology/developers/gemma-3/ - reads wonderfully. Until...
twitterTitle: Gemma 3 - missing features despite announcement
twitterDescription: Congrats to the team to provide the new Gemma 3 models and the new endpoint on the Google AI API. The announcement blog - https://blog.google/technology/developers/gemma-3/ - reads wonderfully. Until...
twitterImage: 
facebookTitle: Gemma 3 - missing features despite announcement
facebookDescription: Congrats to the team to provide the new Gemma 3 models and the new endpoint on the Google AI API. The announcement blog - https://blog.google/technology/developers/gemma-3/ - reads wonderfully. Until...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Congrats to the team to provide the new Gemma 3 models and the new endpoint on the Google AI API. The announcement blog - [https://blog.google/technology/developers/gemma-3/](https://blog.google/technology/developers/gemma-3/) - reads wonderfully. Until someone puts it to the test...

## Create AI with advanced text and visual reasoning capabilities

Easily build applications that analyze images, text, and short videos, opening up new possibilities for interactive and intelligent applications

HTTP 400: "Image input modality is not enabled for models/gemma-3-27b-it"  
HTTP 400: "Audio input modality is not enabled for models/gemma-3-27b-it"

Tried different images (png, jpg, bmp), video (mp4) and PDF documents - both via `inlineData` and per File API using `fileData` attributes.

## Create AI-driven workflows using function calling

Gemma 3 supports function calling and structured output to help you automate tasks and build agentic experiences.

HTTP 400: "Function calling is not enabled for models/gemma-3-27b-it"  
HTTP 400: "Json mode is not enabled for models/gemma-3-27b-it"  
HTTP 400: "Enum mode is not enabled for models/gemma-3-27b-it"

## System Instruction

HTTP 400: "Developer instruction is not enabled for models/gemma-3-27b-it"

## Code execution?

It's not explicitly mentioned in the blog. What's the situation here? Right now...

HTTP 400: "Code execution is not enabled for models/gemma-3-27b-it"

## Candidate count &gt; 1?

It's not explicitly mentioned in the blog. What's the situation here? Right now...

HTTP: "Multiple candidates is not enabled for models/gemma-3-27b-it"

Not sure what's the issue is...

However, with the announcement blog I would kind of expect that the mentioned features are available and operational from day 0 on. And not hoping for the best and then those are being added at a later stage.

I'm not sure whether those features have been disabled for the gemma3 model in the Gemini API and the model itself might be capable to deal with everything, like when used locally or deployed in Vertex AI or Cloud Run with GPU...

What are your observations?