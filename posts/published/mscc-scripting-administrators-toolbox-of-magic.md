---
uid: mscc-scripting-administrators-toolbox-of-magic
title: "MSCC: Scripting - Administrator's­ toolbox of magic..."
slug: mscc-scripting-administrators-toolbox-of-magic
date: 2014-05-04
status: published
type: post
description: Ish and Dan had well prepared presentations on shell scripting, mainly focused towards Bourne Again Shell (bash), and the pros and cons of scripting versus actually writing something in a decent programming language. I thought that I could cut myself out of the equation but the demand for information about PowerShell was higher than expected...
tags:
- Community
keywords: Community
metaTitle: "MSCC: Scripting - Administrator's­ toolbox of magic..."
metaDescription: Ish and Dan had well prepared presentations on shell scripting, mainly focused towards Bourne Again Shell (bash), and the pros and cons of scripting versus actually writing something in a decent programming language. I thought that I could cut myself out of the equation but the demand for information about PowerShell was higher than expected...
image: https://images.unsplash.com/photo-1533229613598-751dc97ec35f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
ogTitle: "MSCC: Scripting - Administrator's­ toolbox of magic..."
ogDescription: Finally, we made it to have our April meetup - in May. The most obvious explanation is the increased amount of open source and IT activities that either the MSCC, the Linux User Group of Mauritius...
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/mscc-scripting-administrators-toolbox-of-magic/
imageUrl: https://images.unsplash.com/photo-1533229613598-751dc97ec35f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
twitterImageUrl: https://images.unsplash.com/photo-1533229613598-751dc97ec35f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: https://images.unsplash.com/photo-1533229613598-751dc97ec35f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ
featured: false
publishedAt: 2014-05-04T03:22:40Z
updatedAt: 2019-01-07T22:30:27Z
excerpt: Finally, we made it to have our April meetup - in May. The most obvious explanation is the increased amount of open source and IT activities that either the MSCC, the Linux User Group of Mauritius...
twitterTitle: "MSCC: Scripting - Administrator's­ toolbox of magic..."
twitterDescription: Finally, we made it to have our April meetup - in May. The most obvious explanation is the increased amount of open source and IT activities that either the MSCC, the Linux User Group of Mauritius...
twitterImage: 
facebookTitle: "MSCC: Scripting - Administrator's­ toolbox of magic..."
facebookDescription: Finally, we made it to have our April meetup - in May. The most obvious explanation is the increased amount of open source and IT activities that either the MSCC, the Linux User Group of Mauritius...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

[![Logo of the Mauritius Software Craftsmanship Community](https://s.kirstaetter.name/images/mscc.jpg)](https://www.meetup.com/MauritiusSoftwareCraftsmanshipCommunity "Mauritius Software Craftsmanship Community")Finally, we made it to have our April meetup - in May. The most obvious explanation is the increased amount of open source and IT activities that either the MSCC, the Linux User Group of Mauritius (LUGM), or the University of Mauritius Student's Computer Club is organising. It's absolutely incredible to see the recent hype of events here on the island. And I'm loving it!

Unfortunately, we also had to deal with arranging for a location this time. It was kind of an odyssey as my requests (and phone calls) haven't been answered, even though I tried it several times - well, kind of disappointing and I have to look into that for future gatherings. In my opinion, it is essential that two parameters of a community meeting are fixed as early as possible:

- Location, and
- Date and time

You can't just change one or both on the very last minute. Well, this time we had to do it due to unforeseen reasons, and I apologise to any MSCC member which couldn't make it to our April meetup. Okay, lesson learned but now back to the actual meetup report ...

Shortly after the meeting I placed the following statement as my first impression:

> *"Spontaneous and improvised :)*
>
> *No, seriously, Ish and Dan had well prepared presentations on shell scripting, mainly focused towards Bourne Again Shell (bash), and the pros and cons of scripting versus actually writing something in a decent programming language. I thought that I could cut myself out of the equation but the demand for information about PowerShell was higher than expected..."*

Well, it turned out that the interest in Windows PowerShell was high, as I even got a couple of questions on it via social media networks during the evening.

I also like to mention that the number of attendees went back to what I would call a "standard" number of participation. This time there were 12 craftsmen, but again a good number of First Timers.

## []()Reactions of other attendees

Here are some impressions and feedback from our participants:

> *"Enjoyed the bash and powershell (linux / windows) presentations ..."* -- Nadim on [event comments](https://www.meetup.com/MauritiusSoftwareCraftsmanshipCommunity/events/167485972/)
>
> *"He [Daniel] also showed us some syntax loopholes in Bash that could leave someone with bad code."* -- Ish on [MSCC – Let's talk about Scripting](https://hacklog.in/mscc-lets-talk-about-scripting/)

Glad to see a couple of first time attendees, especially students from the university itself.

## []()Some details on the presentations

![MSCC: First time visit at the University of Mauritius - Phase II Engineering Tower, room 2.9](https://s.kirstaetter.name/images/mscc-20140503-scripting-1.png)  
*MSCC: First time visit at the University of Mauritius - Phase II Engineering Tower, room 2.9*

### Gimme some love ... bash and other shells

Ish gave a great introduction into shell scripting as he spoke about existing shell environments and a little bit about their history. Furthermore, he talked about various built-in commands, the use of coreutils, the ability to daisy-chain multiple commands using pipes, the importance of the standard I/O streams and their file descriptors in advanced scripting techniques. Combined with a couple of sample statements in the Linux terminal on Ubuntu 14.04 machine it was a solid presentation.

Have a closer look at his slides - published on his blog on [MSCC – Let's talk about Scripting](https://hacklog.in/mscc-lets-talk-about-scripting/).

### Oddities of scripting

After the brief introduction into bash it was Daniel's turn to highlight a good number of oddities when working with shell scripts. First of all, it should be clear that scripting is not supposed for any kind of implementations in terms of software but simply to automate administrative procedures and to simplify routine jobs on a system. One of the cool oddities that he mentioned is that everything (!) in a shell is represented by strings; there are no other types like integer, float, date-time, etc. that you'd like to use in a full-fledged programming language. Let's have a look at his sample:

> `more to come...`

What's the output?

As a conclusion, Daniel suggests that shell scripting should be limited but not restricted to automatic repetitive command stacks and batch jobs, startup wrapper for applications in order to set up the execution environment, and other not too sophisticated jobs. But as soon as it might involve a little bit more logic or you might rely on performance it's better to write an application in Ruby, Python, or Perl (among others of course). This is also enables the possibility to test your code properly.

![MSCC: Ish talking about bash and shell scripting](https://s.kirstaetter.name/images/mscc-20140503-scripting-2.jpg)*MSCC: Ish talking about Bourne Again Shell (bash) and shell scripting to automate regular tasks*

![MSCC: Daniel gives an overview about the pros and cons of shell scripting versus programming](https://s.kirstaetter.name/images/mscc-20140503-scripting-3.jpg)*MSCC: Daniel gives an overview about the pros and cons of shell scripting versus programming*

![MSCC: PowerShell as your scripting solution on Windows operating systems](https://s.kirstaetter.name/images/mscc-20140503-scripting-4.jpg)*MSCC: PowerShell as your scripting solution on Windows operating systems*

### The path of the Enlightened is long ...

and tough.

Honestly, even though PowerShell was mentioned without any further details on the meetup's agenda, I didn't expect that there would be demand to give a presentation on Microsoft PowerShell after all. I already took this topic out of the announcement but the audience wanted to have some information. Okay, then let's see what I could do - improvised style. While my machine booted and got hooked up to the projector, I started to talk about the beginnings of [PowerShell from back in 2006](https://jochen.kirstaetter.name/posh-windows-powershell/), and its predecessors MS DOS and Command Prompt. A throwback in history... always good for young people.

As usual, Microsoft didn't get it at that time. Instead of listening to their client's needs and demands they ignored the feasibility to administrate Windows server farms without any UI tools. PowerShell is actually a result of this, and seeing that shell scripting is a common, reliable and fast way in an administrator's toolbox for decades, Microsoft had to adapt from their Microsoft Management Console (MMC) to a broader approach. It's not like shell scripting was something new; it is in daily use by alternative operating systems like AIX, HP UX, Solaris, and last but not least Linux.

Most interestingly, Microsoft is very good at renovating existing architectures, and over the years PowerShell not only replaced their own combination of Command Prompt and Scripting Hosts (VBScript and CScript) but really turned into a challenging competitor on the market. The shell is easy to extend with cmdlets, and open to other Microsoft products like SQL Server, SharePoint, as well as Third-party software applications. Similar to MMC PowerShell also offers the ability to administer other machine remotely - only without a graphical user interface and therefore it's easier to automate and schedule regular tasks.

Following is a sample of a PowerShell script file (extension .ps1):

> `$strComputer = "."`
>
> `$colItems = get-wmiobject -class Win32_BIOS -namespace root\CIMV2 -comp $strComputer`
>
> `foreach ($objItem in $colItems) {`  
`write-host "BIOS Characteristics: " $objItem.BiosCharacteristics`  
`write-host "BIOS Version: " $objItem.BIOSVersion`  
`write-host "Build Number: " $objItem.BuildNumber`  
`write-host "Caption: " $objItem.Caption`  
`write-host "Code Set: " $objItem.CodeSet`  
`write-host "Current Language: " $objItem.CurrentLanguage`  
`write-host "Description: " $objItem.Description`  
`write-host "Identification Code: " $objItem.IdentificationCode`  
`write-host "Installable Languages: " $objItem.InstallableLanguages`  
`write-host "Installation Date: " $objItem.InstallDate`  
`write-host "Language Edition: " $objItem.LanguageEdition`  
`write-host "List Of Languages: " $objItem.ListOfLanguages`  
`write-host "Manufacturer: " $objItem.Manufacturer`  
`write-host "Name: " $objItem.Name`  
`write-host "Other Target Operating System: " $objItem.OtherTargetOS`  
`write-host "Primary BIOS: " $objItem.PrimaryBIOS`  
`write-host "Release Date: " $objItem.ReleaseDate`  
`write-host "Serial Number: " $objItem.SerialNumber`  
`write-host "SMBIOS BIOS Version: " $objItem.SMBIOSBIOSVersion`  
`write-host "SMBIOS Major Version: " $objItem.SMBIOSMajorVersion`  
`write-host "SMBIOS Minor Version: " $objItem.SMBIOSMinorVersion`  
`write-host "SMBIOS Present: " $objItem.SMBIOSPresent`  
`write-host "Software Element ID: " $objItem.SoftwareElementID`  
`write-host "Software Element State: " $objItem.SoftwareElementState`  
`write-host "Status: " $objItem.Status`  
`write-host "Target Operating System: " $objItem.TargetOperatingSystem`  
`write-host "Version: " $objItem.Version`  
`write-host`  
`}`

Which gives you information about your BIOS and Windows OS. Then change the computer name to another one on your network (NetBIOS based) and run the script again.

There lots of samples and tutorials at the [Microsoft Script Center](https://technet.microsoft.com/en-us/scriptcenter/powershell.aspx "Microsoft Script Center"), and I would advise you to pay a visit over there if you are more interested in PowerShell. The Script Center provides the download links, too.

## []()Upcoming Events

What are the upcoming events here in Mauritius? So far, we have the following ones (incomplete list as usual) in chronological order:

- [Hacking Defence](https://www.facebook.com/photo.php?fbid=743000712397610&set=a.550859001611783.1073741827.535899709774379&type=1&relevant_count=1&ref=nf "Hacking Defence") (14. May 2014)
- [WebCup Maurice](https://maurice.webcup.fr "WebCup Maurice") (7. & 8. June 2014)
- Developers Conference (TBA ~ July 2014)
- Linuxfest 2014 (TBA ~ November 2014)

Hopefully, there will be more announcements during the next couple of weeks and months. If you know about any other event, like a bootcamp, a code challenge or hackathon here in Mauritius, please drop me a note in the comment section below this article. Thanks!

## []()My resume of the day

> **Spontaneous and improvised :)**

The new location at the University of Mauritius turned out very well, there is plenty of space, and it could be a good choice for future meetings. Especially, having the ability to get more and more students into our IT community sounds like a great opportunity. Later during the day, I got some promising mails from Nadim regarding future sessions at the local branch of the Middlesex University. Well, we will see in the future... But for now this will be on hold until approximately October when students resume their regular studies.

Anyway, it was a good experience at the university, and thanks again to the UoM Student's Computer Club that made the necessary arrangements for the MSCC!
