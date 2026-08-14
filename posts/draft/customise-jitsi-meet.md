---
uid: customise-jitsi-meet
title: Customise your instance of Jitsi Meet (Draft)
slug: customise-jitsi-meet
date: 2020-04-20
status: draft
type: post
description: In this third article on Jitsi Meet we are going to explore a few options to customise your instance. And how to make them persistent while upgrading the installation packages. At the time of writing...
tags:
- Development
keywords: Development
metaTitle: Customise your instance of Jitsi Meet
metaDescription: In this third article on Jitsi Meet we are going to explore a few options to customise your instance. And how to make them persistent while upgrading the installation packages. At the time of writing...
image: ''
ogTitle: Customise your instance of Jitsi Meet
ogDescription: In this third article on Jitsi Meet we are going to explore a few options to customise your instance. And how to make them persistent while upgrading the installation packages. At the time of writing...
layout: post
bodyClass: post-template tag-development
postClass: post tag-development
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
canonicalUrl: https://jochen.kirstaetter.name/customise-jitsi-meet/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: ''
updatedAt: 2020-10-09T21:15:04Z
excerpt: In this third article on Jitsi Meet we are going to explore a few options to customise your instance. And how to make them persistent while upgrading the installation packages. At the time of writing...
twitterTitle: Customise your instance of Jitsi Meet
twitterDescription: In this third article on Jitsi Meet we are going to explore a few options to customise your instance. And how to make them persistent while upgrading the installation packages. At the time of writing...
twitterImage: 
facebookTitle: Customise your instance of Jitsi Meet
facebookDescription: In this third article on Jitsi Meet we are going to explore a few options to customise your instance. And how to make them persistent while upgrading the installation packages. At the time of writing...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
In this third article on Jitsi Meet we are going to explore a few options to customise your instance. And how to make them persistent while upgrading the installation packages. At the time of writing this article any modifications are overwritten when you update the installed packages; at least on Debian/Ubuntu.

Given the architecture and the number of components involved in a Jitsi Meet installation there are multiple locations that allow you to tweak your installation.

The adjustments described below require `root` permissions which you can handle by either launching an interactive, privileged terminal session or by prefixing the commands with `sudo`.

## Feature configuration

The `hostname-config.js` file is your central configuration and it is also loaded by the web client. Here you would define your basic settings in regards to all kinds of aspects in Jitsi, i.e. whether participants are muted on entry and so forth.

Open the configuration file and go really slow through the individual settings.

```
nano /etc/jitsi/meet/$(hostname -f)-config.js
```

**Note**: I inspected the config file of the public instance running at jitsi.org to get a better understanding of recommended default settings and how some integrations should be configured.

### Integrate Google Calendar and Youtube

In the same configuration file you would also place necessary information to integrate with some of the services offered by either Google, Microsoft, or Dropbox.

There is a well-written document on [Integrations](https://github.com/jitsi/jitsi-meet/blob/master/doc/integrations.md) available in the Jitsi Meet repository on GitHub. You might have a look there and read through it as a starting point.

## Change the appearance

Although you are going to come across a few variables / directives in the hostname configuration file be aware that the ones related to visual appearance, i.e. background colour actually do not work (any more). At least, my changes did not have any impact on the visual appearance of Jitsi Meet in my installation.

### Styling your website using CSS directives

### Use your own images

### Tweak a few more features

```
nano /usr/share/jitsi-meet/interface_config.js
```

### Social media and open graph information

```
nano /usr/share/jitsi-meet/title.html
```

### Custom footer area

```
nano /usr/share/jitsi-meet/static/welcomePageAdditionalContent.html
```

## Persistence #1: Use virtual locations

While finishing off the initial installation and getting some rough ideas on customisation options of Jitsi Meet I took this approach as the most obvious one to avoid any kind of loss due to an upgrade.

Maybe it's not the most elegant way to handle things but at least it is possible to keep your modifications alive. ;-)

The idea is based on the list of files that are installed by the Debian or Ubuntu package. You can inspect that list of files using the `dpkg` command.

Next, I took the list of files that I either modified or replaced completely and started to use a pleasant feature of nginx web server: location directive.

## Persistence #2: Use a git repository

Trust me, this idea came weeks or even months later. However given the delay between the individual articles of this series on Jitsi Meet I would say it might be very positive for you at this stage now.

The concept of this approach is to use version control for the Jitsi Meet files. This has two essential advantages over using the location directive described earlier.

First, you can track your own modifications over time and have them safely versioned. Using version control is literally like using a time-capsule for your files. You can restore any previous stage at any time.

Second, prior to an upgrade of the installed package you can stash your changes and pop them back after the upgrade has been completed.

And perhaps most interestingly however completely optional you can work with a remote repository hosted by any cloud service offering git repository. This give you the advantage that you could easily deploy your configuration changes to more than one machine.

As there are so many tutorials on how to get started with `git` I don't want to elaborate too much in this article here. Only the initial steps to get you started are following.

Make sure that `git` is actually installed on your system.

```
sudo apt-get install git
```

Then navigate to the base directory of the Jitsi Meet installation.

```
cd /usr/share/jitsi-meet
```

There you would initialise a local git repository and add all existing files like this.

```
git init
git add .
git commit -m 'initial commit'
```

Now, your time-capsule is active and you can safely apply your configuration changes. Remember to stage and commit your modifications regularly.

As mentioned, optionally you could add one or more remotely located git repositories to your local one and push your modifications. It's a nice backup mechanism in case something unexpected might happen to your machine or VM.

## Use Jitsi Meet Electron

[https://github.com/jitsi/jitsi-meet-electron](https://github.com/jitsi/jitsi-meet-electron)

![Using the Jitsi Meet Desktop (Electron-based) application ](../content/images/2020/04/image-24.webp)

```
X-Frame-Options SAMEORIGIN;
```