---
uid: taking-web-sites-offline-for-demonstration
title: Taking web sites offline for demonstration
slug: taking-web-sites-offline-for-demonstration
date: 2012-10-29
status: published
type: post
description: How to prepare an offline version of your web site for the purpose of demonstration or for exhibitions.
tags:
- Development
keywords: Development
metaTitle: Taking web sites offline for demonstration
metaDescription: How to prepare an offline version of your web site for the purpose of demonstration or for exhibitions.
image: https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=76a0db878c33cf839e0c482a332ddad0
ogTitle: Taking web sites offline for demonstration
ogDescription: While working in software development in general, and in web development for a couple of customers it is quite common that it is necessary to provide a test bed where the client is able to get an...
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
canonicalUrl: https://jochen.kirstaetter.name/taking-web-sites-offline-for-demonstration/
imageUrl: https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=76a0db878c33cf839e0c482a332ddad0
twitterImageUrl: https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=76a0db878c33cf839e0c482a332ddad0
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ&s=76a0db878c33cf839e0c482a332ddad0
featured: false
publishedAt: 2012-10-29T12:13:20Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: While working in software development in general, and in web development for a couple of customers it is quite common that it is necessary to provide a test bed where the client is able to get an...
twitterTitle: Taking web sites offline for demonstration
twitterDescription: While working in software development in general, and in web development for a couple of customers it is quite common that it is necessary to provide a test bed where the client is able to get an...
twitterImage: 
facebookTitle: Taking web sites offline for demonstration
facebookDescription: While working in software development in general, and in web development for a couple of customers it is quite common that it is necessary to provide a test bed where the client is able to get an...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

While working in software development in general, and in web development for a couple of customers it is quite common that it is necessary to provide a test bed where the client is able to get an image, or better said, a feeling for the visions and ideas you are talking about. Usually here at [IOS Indian Ocean Software Ltd.](https://www.ios.mu/ "IOS Indian Ocean Software Ltd.") we set up a demo web site on one of our staging servers, and provide credentials to the customer to access and review our progress and work ad hoc. This gives us the highest flexibility on both sides, as the test bed is simply online and available 24/7. We can update the structure, the UI and data at any time, and the client is able to view it as it suits best for her/him.

## Limited or lack of online connectivity

But what is going to happen when your client is not capable to be online - no matter for what reasons; here are some more obvious ones:

- No internet connection (permanently or temporarily)
- Expensive connection, ie. mobile data package, stay at a hotel, etc.  
- Presentation devices at an exhibition, ie. using tablets or iPads
- Being abroad for a certain time, and only occasionally online  
- No network coverage, especially on mobile
- Bad infrastructure, like ie. in Third World countries
- Providing a catalogue on CD or USB pen drive

Anyway, it doesn't matter really. We should be able to provide a solution for the circumstances of our customers.

## Presentation during an exhibition

Recently, we had the following request from a customer:

> Is it possible to let us have a desktop version of [ResortWork.co.uk](https://www.resortwork.co.uk/ "ResortWork.co.uk") that we can use for demo purposes at the forthcoming Ski Shows? It would allow us to let stand visitors browse the sites on an iPad to view jobs and training directory course listings.

Yes, sure we can do that. Eventually, you might think why don't they simply use 3G enabled iPads for that purpose? As stated above, there might be several reasons for that - low coverage, expensive data packages, etc. Anyway, it is not a question on how to circumvent the request but to deliver a solution to that.

## Possible solutions... or not?

We already did offline websites earlier, and even established complete mirrors of one or two web sites on our systems. There are actually several possibilities to handle this kind of request, and it mainly depends on the system or device where the offline site should be available on. Here, it is clearly expressed that we have to address this on an Apple iPad, well actually, I think that they'd like to use multiple devices during their exhibitions.

Following is an overview of possible solutions depending on the technology or device in use, and how it can be done:

- Replication of source files and database
  - The above mentioned web site is running on ASP.NET, IIS and SQL Server. In case that a laptop or slate runs a Windows OS, the easiest way would be to take a snapshot of the source files and database, and transfer them as local installation to those Windows machines. This approach would be fully operational on the local machine.
- Saving pages for offline usage
  - This is actually a quite tedious job but still practicable for small web sites
- Tool based approach to 'harvest' the web site  
- There quite some tools in the wild that could handle this job, namely wget, httrack, web copier, etc.
- Screenshots bundled as PDF document
  - Not really... ;-)
- Creating screencast or video
  - Simply navigate through your website and record your desktop session. Actually, we are using this kind of approach to track down difficult problems in order to see and understand exactly what the user was doing to cause an error.

Of course, this list isn't complete and I'd love to get more of your ideas in the comments section below the article.

## Preparations for offline browsing

The original website is dynamically and data-driven by ASP.NET, and looks like this:

![Original web site - October 2012](https://s.kirstaetter.name/images/resortwork_linux_firefox.jpg "Original web site - October 2012")

As we have to put the result onto iPads we are going to choose the tool-based approach to 'download' the whole web site for offline usage. Again, depending on the complexity of your web site you might have to check which of the applications produces the best results for you. My usual choice is to use wget but in this case, we run into problems related to the rewriting of hyperlinks. As a consequence of that we opted for using [HTTrack](https://www.httrack.com "HTTrack"). HTTrack comes in different flavours, like console application but also as either GUI (WinHTTrack on Windows) or Web client (WebHTTrack on Linux/Unix/BSD). Here's a brief description taken from the original website about HTTrack:

> HTTrack is a [free](https://www.gnu.org/philosophy/free-sw.html) ([GPL](https://www.gnu.org/licenses/gpl.txt), libre/free software) and easy-to-use offline browser utility.
>
> It allows you to download a World Wide Web site from the Internet to a local directory, building recursively all directories, getting HTML, images, and other files from the server to your computer. HTTrack arranges the original site's relative link-structure. Simply open a page of the "mirrored" website in your browser, and you can browse the site from link to link, as if you were viewing it online.

And there is an extensive documentation for all options and switches online. General recommendation is to go through the [HTTrack Users Guide By Fred Cohen](https://www.httrack.com/html/fcguide.html). It covers all the initial steps you need to get up and running. Be aware that it will take quite some time to get all the necessary resources down to your machine. Actually, for our customer we run the tool directly on their web server to avoid unnecessary traffic and bandwidth. After a couple of runs and some additional fine-tuning - explicit inclusion or exclusion of various external linked web sites - we finally had a more or less complete offline version available.

A very handsome feature of HTTrack is the error/warning log after completing the download. It contains some detailed information about errors that appeared on the pages and the links within the pages that have been processed.

```
Error:  "Bad Request" (400) at link www.resortwork.co.uk/job-details_Ski_hire:tech_or_mgr_or_driver_37854.aspx  
(from www.resortwork.co.uk/Jobs_A_to_Z.aspx)  
Error:  "Not Found" (404) at link www.247recruit.net/images/applynow.png  
(from www.247recruit.net/css/global.css)  
Error:  "Not Found" (404) at link www.247recruit.net/activate.html  
(from www.247recruit.net/247recruit_tefl_jobs_network.html)
```

In our situation, we took the records of HTTP 400/404 errors and passed them to the web development department. Improvements are to be expected soon. ;-)

## Quality assurance on the full-featured desktop

Unfortunately, the generated output of HTTrack was still incomplete but luckily there were only images missing. Being directly on the web server we simply copied the missing images from the original source folder into our offline version. After that, we created an archive and transferred the file securely to our local workspace for further review and checks.

From that point on, it wasn't necessary to get any more files from the original web server, and we could focus ourselves completely on the process of browsing and navigating through the offline version to isolate visual differences and functional problems. As said, the original web site runs on ASP.NET Web Forms and uses Postback calls for interaction like search, pagination and partly for navigation. This is the main field of improving the offline experience.

Of course, same as for standard web development it is advised to test with various browsers, and strangely we discovered that the offline version looked pretty good on Firefox, Chrome and Safari, but not in Internet Explorer. A quick look at the HTML source shed some light on this, and there are conditional CSS inclusions based on the user agent. HTTrack is not acting as Internet Explorer and so we didn't have the necessary overrides for this browser. Not problematic after all in our case, but you might have to pay attention to this and get the IE-specific files explicitly.

And while having a view at the source code, we also found out that HTTrack actually modifies the generated HTML output. In several occasions we discovered that &lt;div&gt; elements were converted into &lt;table&gt; constructs for no obvious reason; even nested structures.

## Search 'e'nd destroy - sed (or Notepad++) to the rescue

During our intensive root cause analysis for a couple of HTML/CSS problems that needed some extra attention it is very helpful to be familiar with any editor that allows search and replace over multiple files like, ie. sed - stream editor for filtering and transforming text on Linux or my personal favourite Notepad++ on Windows. This allowed us to quickly fix a lot of anchors with onclick attributes and Javascript code that was addressed to ASP.NET files instead of their generated HTML counterparts, like so:

```
grep -lr -e '.aspx' * | xargs sed -e 's/.aspx/.html?/g'
```

The additional question mark after the HTML extension helps to separate the query string from the actual target and solved all our missing hyperlinks very fast. The same can be done in Notepad++ on Windows, too. Just use the 'Replace in files' feature and you are settled. Especially, in combination with Regular Expressions (regex).

## Landscape of browsers  
Okay, after several runs of HTML/CSS code analysis, searching and replacing some strings in a pool of more than 4.000 files, we finally had a very good match of an offline browsing experience in Firefox and Chrome on Linux. Next, we transferred that modified set of files to a Windows 8 machine for review on Firefox, Chrome and Internet Explorer 7 to 10, and a Mac mini running Mac OS X 10.7 to check the output on Safari and again on Chrome. Besides IE, for reasons already mentioned above, the results were identical.

And last but not least it was about to check web site on tablets.  
Please continue to read on the following articles:

[Taking web sites offline for demonstration on Galaxy Tablet](xref:taking-web-sites-offline-for-demonstration-on-galaxy-tablet "Taking web sites offline for demonstration on Galaxy Tablet")

[Taking web sites offline for demonstration on iPad](xref:taking-web-sites-offline-for-demonstration-on-ipad "Taking web sites offline for demonstration on iPad")
