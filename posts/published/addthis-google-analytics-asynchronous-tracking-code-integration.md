---
uid: addthis-google-analytics-asynchronous-tracking-code-integration
title: 'AddThis and Google Analytics : Asynchronous Tracking Code Integration'
slug: addthis-google-analytics-asynchronous-tracking-code-integration
date: 2010-03-03
status: published
type: post
description: Step by step guide to establish interop between AddThis sharing and Google Analytics asynchronous tracking.
tags:
- Community
keywords: Community
metaTitle: 'AddThis and Google Analytics : Asynchronous Tracking Code Integration'
metaDescription: Step by step guide to establish interop between AddThis sharing and Google Analytics asynchronous tracking.
image: ''
ogTitle: 'AddThis and Google Analytics : Asynchronous Tracking Code Integration'
ogDescription: During the weekend I did some modifications, read improvements, here on the website according to Search Engine Optimization (SEO), keywords and page load times. Reducing the page load times made it...
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
canonicalUrl: https://jochen.kirstaetter.name/addthis-google-analytics-asynchronous-tracking-code-integration/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2010-03-03T07:41:40Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: During the weekend I did some modifications, read improvements, here on the website according to Search Engine Optimization (SEO), keywords and page load times. Reducing the page load times made it...
twitterTitle: 'AddThis and Google Analytics : Asynchronous Tracking Code Integration'
twitterDescription: During the weekend I did some modifications, read improvements, here on the website according to Search Engine Optimization (SEO), keywords and page load times. Reducing the page load times made it...
twitterImage: 
facebookTitle: 'AddThis and Google Analytics : Asynchronous Tracking Code Integration'
facebookDescription: During the weekend I did some modifications, read improvements, here on the website according to Search Engine Optimization (SEO), keywords and page load times. Reducing the page load times made it...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
During the weekend I did some modifications, read improvements, here on the website according to Search Engine Optimization (SEO), keywords and page load times. Reducing the page load times made it necessarily to arrange my Javascript snippets in the template. So far, everything went well, until I figured out that my Google Analytics dropped down to 0...

So, while checking those issues I stumbled upon the 'new' [Google Analytics Asynchronous Tracking](https://code.google.com/apis/analytics/docs/tracking/asyncTracking.html "Google Analytics Asynchronous Tracking") code. This will also reduce page load time as "asynchronous tracking optimizes how browsers load `ga.js` so its impact on user experience is minimized." - Great!

The steps to use the asynchronous tracking is straight forward:

- Memorize or copy your web property ID from the existing snippet
- Remove the synchronous tracking code
- Insert the asynchronous tracking code  

```
&lt;script type="text/javascript"&gt;&lt;!--  
var _gaq = _gaq || [];  
_gaq.push(['_setAccount', 'UA-XXXXX-X']);  
_gaq.push(['_trackPageview']);  
  
(function() {  
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;  
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'https://www') + '.google-analytics.com/ga.js';  
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);  
})();  
// --&gt;&lt;/script&gt;
```

- Replacing UA-XXXXX-X with your web property ID.

That's the easy part...

[Integrating AddThis](https://www.addthis.com/help/google-analytics-integration "Google Analytics Integration") into the 'standard' Google Analytics is extensively described on the help pages of AddThis. But sadly, there is no information about the asynchronous tracking code. Additionally, I checked the AddThis support forum and the topic ['](https://www.addthis.com/forum/viewtopic.php?f=6&t=22352 "Google Analytics : Asynchronous Tracking Code Integration")[Google Analytics : Asynchronous Tracking Code Integration'](https://www.addthis.com/forum/viewtopic.php?f=6&t=22352 "Google Analytics : Asynchronous Tracking Code Integration") is discussed since a while. Not even answered by AddThis supporters yet. Even the [Google Forum](https://www.google.com/support/forum/p/Google+Analytics/thread?tid=0d2e9675bdecb6dd&hl=en "Switched to Asynchronous and now we have no data at all. ") does not provide an answer. I was astonished to see this! Frankly speaking, this is not an unusual situation for a website, or?

Anyways, back to this article. You can send AddThis shares to your Google Analytics reports as custom events in the category “addthis” by adding the following configuration code to your existing AddThis sharing code:


```
addthis_config = {  
data_ga_tracker: pageTracker  
}
```


The main problem about the interoperability between AddThis and Google Analytics is that the asynchronous tracking code does not provide a pageTracker object anymore. As said, this only works with the synchronous tracking code of Google Analytics. The forum threads actually provides some directions towards the solution of this problem. The link between those two services is to reference the GA pageTracker object in the AddThis configuration.

The Asynchronous Tracking Usage Guide provides the necessary information in the paragraphs about Multiple Tracker Objects and Pushing Functions. It is not clearly described on the spot but with a little bit of logic you can figure it out: Create your own Javascript variable that queries the Google API.


```
_gaq.push(function() {  
var pageTracker = _gaq._getAsyncTracker('myTracker');  
var link = document.getElementById('my-link-id');  
link.href = pageTracker._getLinkerUrl('https://example.com/');  
});
```
&lt;

The solution lies in the parameter of _getAsyncTracker(). The samples in the User Guide refer to a named tracker. But what about the initial one? Right, just specify an empty string and you are done!



To summarize this article just use the following code snippet at the very end of your website to integrate Google Analytics : Asynchronous Tracking with your AddThis analytics:


```
&lt;!-- Google Analytics and AddThis button --&gt;  
&lt;script type="text/javascript"&gt;  
(function() {  
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;  
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'https://www') + '.google-analytics.com/ga.js';  
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);  
})();  
&lt;/script&gt;  
  
&lt;script type="text/javascript"&gt;  
**var pageTracker = [];  
if (_gaq._getAsyncTracker) {  
pageTracker = _gaq._getAsyncTracker('');  
}**  
var addthis_config = {  
data_ga_tracker: pageTracker  
};&lt;/script&gt;  
&lt;/body&gt;
```


The GA user guide recommends to split your asynchronous code over your HTML content. The setup of the tracker should be directly after the &lt;body&gt; tag whereas the rest should be placed at the very end of your document (as described above).

Hopefully, my description is clear enough to enjoy a smooth and seamless code integration between Google Analytics Asynchronous Tracking and AddThis Sharing.