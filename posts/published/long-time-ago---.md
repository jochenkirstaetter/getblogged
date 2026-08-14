---
uid: long-time-ago---
title: Long time ago...
slug: long-time-ago---
date: 2005-12-28
status: published
type: post
description: Long time ago... ...in a country far far far away.I guess this may be the words for a fairy tale. But this blog article isn&#39;t to be one of those. Well, long time ago since I blogged my last article on this site. Meanwhile I did a lot of project
tags:
- Community
keywords: Community
metaTitle: Long time ago...
metaDescription: Long time ago... ...in a country far far far away.I guess this may be the words for a fairy tale. But this blog article isn&#39;t to be one of those. Well, long time ago since I blogged my last article on this site. Meanwhile I did a lot of project
image: ''
ogTitle: Long time ago...
ogDescription: "...in a country far far far away.I guess this may be the words for a fairy tale. But this blog article isn't to be one of those. Well, long time ago since I blogged my last article on this site..."
layout: post
bodyClass: post-template tag-community
postClass: post tag-community
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
canonicalUrl: https://jochen.kirstaetter.name/long-time-ago---/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2005-12-28T09:59:46Z
updatedAt: 2018-04-02T08:38:32Z
excerpt: "...in a country far far far away.I guess this may be the words for a fairy tale. But this blog article isn't to be one of those. Well, long time ago since I blogged my last article on this site..."
twitterTitle: Long time ago...
twitterDescription: "...in a country far far far away.I guess this may be the words for a fairy tale. But this blog article isn't to be one of those. Well, long time ago since I blogged my last article on this site..."
twitterImage: 
facebookTitle: Long time ago...
facebookDescription: "...in a country far far far away.I guess this may be the words for a fairy tale. But this blog article isn't to be one of those. Well, long time ago since I blogged my last article on this site..."
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
...in a country far far far away.

I guess this may be the words for a fairy tale. But this blog article isn't to be one of those. Well, long time ago since I blogged my last article on this site. Meanwhile I did a lot of project stuff for some customers and now again, it's vacation time. Probably the best time to write a new blog entry.

Alright, let's what's changed since last time. Actually I wrote some nice entries to my German blog at [https://jochen.kirstaetter.name/](https://jochen.kirstaetter.name) and like to summarize the last three months a little bit.

Starting with the German VFP developer's conference - [https://devcon.dfpug.de](https://devcon.dfpug.de) - should be a smooth way to sum up all this stuff. Yup, again I had the chance to speak at the conference and I held four sessions. Those were about useful and free tools to enhance daily work with Visual FoxPro (D-GEIZ), Regular Expressions - my favorite one (D-REGX), using Subversion as source code version control system (D-SVN) and last but not least about interoperability between Visual FoxPro and Linux related technologies (D-LINU). Just check out the session descriptions for details or even better the UT Coverage at [https://www.utcoverage.com/German/2005](https://www.utcoverage.com/German/2005) and [https://www.utcoverage.com/German/20052](https://www.utcoverage.com/German/20052) - especially the picture gallery. ;-)

It was a lot of fun during these days and I appreciate next year's event. Additionally I'll head to Praha again. Maybe we'll meet each other.

Fine, talking about German FoxPro User Group (dFPUG) I'd like to mention that we just had our last meeting of the regional user group at Speyer - the city here in Germany with the famous dome. Yeah, it was a quite funny event because we had some nice goodies from O'Reilly, Microsoft and others as give-aways. Plans for 2006 are already made and I bet that this will be one of the best opportunities to get in touch with die-hard FoxPro coders in our region. ;-) One of the monthly attendees uses Fox since FoxBase 1.02b (IIRC) - that's way impressive.

And here we are at the present moment. Currently I did a lot of enhancements in Html Plugin for Active FoxPro Pages and AfpWiki itself. I hope to release both products during next week. Html Plugin is primarily a plug-in for [Active FoxPro Pages](https://www.afpages.com). But that's only half the truth. The plug-in itself is build as a component and offers stand-alone functionality for VFP developers and through COM as well for other programming languages. In VFP you just create an object like so:


```foxpro
Set Procedure To "html.plugin.dll" Additive

Html = CreateObject("CHTML")
```


If you have to use COM instead, then this works just fine:

`Html = CreateObject("AFPPlugin.Html")`

It was quite funny to get this component working in .NET Framework and I'm still working on this topic, but at the moment I got it to create my own namespace (tree) based on this single DLL. After you added a reference to the COM server, you'll have an new namespace tree instead of just one plain entry: ProLib.AFP3.Plugin.Html and due to COM interoperability in .NET the instance name of the class is simple HtmlClass.

I wrote a sample solution that's able to convert an RSS Feed to a .NET DataSet through the Html Plugin. Well, not too hard to implement in pure .NET but the fact is, that the plug-in provides the same functionality to VFP developers.

And... Html Plugin is a core part of AfpWiki - a Wiki engine on top of [Active FoxPro Pages](https://www.afpages.com). Actually the Html Plugin does all the stuff related to Regular Expressions. It's really nice to see that just one line of code parses all hyperlinks of the entire document and converts them into clickable links with 'title' attribute and protocol indicator. There is still a lot of work to do inside of AfpWiki, like backup and restore of the database, online upgrade mechanism as well as an abstraction layer to user authentication and management, but this will be implemented during a couple of weeks. You might check out [https://faq.dfpug.de](https://faq.dfpug.de) to see the system in action.

Ah, before I forget to mention... Html Plugin and AfpWiki are both available for free (as in beer *g*). So, if anyone of you is interested in a Wiki solution... just drop me a note.

That's all for 2005... I wish you A Happy New Year and hope to see you all in 2006 again.

Sincerely, JoKi