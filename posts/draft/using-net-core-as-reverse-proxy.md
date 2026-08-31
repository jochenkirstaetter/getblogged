---
uid: using-net-core-as-reverse-proxy
title: Using .NET Core as reverse proxy
date: 2019-01-22
status: draft
type: post
description: class Program{ static void Main(string[] args) { WebHost.CreateDefaultBuilder(args).ConfigureServices(s => s.AddProxy()).Configure(a => a.RunProxy(c =>...
tags: []
keywords: ''
metaTitle: Using .NET Core as reverse proxy
metaDescription: class Program{ static void Main(string[] args) { WebHost.CreateDefaultBuilder(args).ConfigureServices(s => s.AddProxy()).Configure(a => a.RunProxy(c =>...
image: ''
ogTitle: Using .NET Core as reverse proxy
ogDescription: class Program{ static void Main(string[] args) { WebHost.CreateDefaultBuilder(args).ConfigureServices(s => s.AddProxy()).Configure(a => a.RunProxy(c =>...
layout: post
bodyClass: post-template
postClass: post
isPost: true
isPage: false
isDraft: true
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
canonicalUrl: https://jochen.kirstaetter.name/using-net-core-as-reverse-proxy/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: ''
updatedAt: 2019-01-22T10:47:33Z
excerpt: class Program{ static void Main(string[] args) { WebHost.CreateDefaultBuilder(args).ConfigureServices(s => s.AddProxy()).Configure(a => a.RunProxy(c =>...
twitterTitle: Using .NET Core as reverse proxy
twitterDescription: class Program{ static void Main(string[] args) { WebHost.CreateDefaultBuilder(args).ConfigureServices(s => s.AddProxy()).Configure(a => a.RunProxy(c =>...
twitterImage: 
facebookTitle: Using .NET Core as reverse proxy
facebookDescription: class Program{ static void Main(string[] args) { WebHost.CreateDefaultBuilder(args).ConfigureServices(s => s.AddProxy()).Configure(a => a.RunProxy(c =>...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
> class Program  
{  
static void Main(string[] args)  
{  
WebHost.CreateDefaultBuilder(args).ConfigureServices(s =&gt; s.AddProxy()).Configure(a =&gt; a.RunProxy(c =&gt; c.ForwardTo("https://upstream").Send())).Build().Run();  
}  
}  
  
^ A reverse proxy in a tweet ^
>
> — Damian Hickey ❄️ (@randompunter) [January 22, 2019](https://x.com/randompunter/status/1087650125906878464?ref_src=twsrc%5Etfw)

```
using Microsoft.AspNetCore.Hosting; 
using ProxyKit;

class Program 
{ 
	static void Main(string[] args) 
	{
		WebHost.CreateDefaultBuilder(args).ConfigureServices(
			s => s.AddProxy()).Configure(
			a => a.RunProxy(
			c => c.ForwardTo("https://upstream").Send())).Build().Run(); 
	} 
}
```