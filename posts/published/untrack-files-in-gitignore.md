---
uid: untrack-files-in-gitignore
title: Untrack files in .gitignore
slug: untrack-files-in-gitignore
date: 2024-04-05
status: published
type: post
description: Despite best effort and preparation of your precious source code one day you might be facing the situation that there is one or more files in your development workspace that doesn't belong into your git repository.
tags:
- Development
keywords: Development
metaTitle: Untrack files in .gitignore
metaDescription: Despite best effort and preparation of your precious source code one day you might be facing the situation that there is one or more files in your development workspace that doesn't belong into your git repository.
image: content/images/2024/04/Gemini_Generated_Image_pxek4spxek4spxek.webp
ogImage: content/images/2024/04/Gemini_Generated_Image_pxek4spxek4spxek-og.webp
ogTitle: Untrack files in .gitignore
ogDescription: Despite best effort and preparation of your precious source code one day you might be facing the situation that there is one or more files in your development workspace that doesn't belong into your git repository.
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
canonicalUrl: https://jochen.kirstaetter.name/untrack-files-in-gitignore/
imageUrl: content/images/2024/04/Gemini_Generated_Image_pxek4spxek4spxek.webp
twitterImageUrl: https://jochen.kirstaetter.name/content/images/2024/04/Gemini_Generated_Image_pxek4spxek4spxek.jpeg
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2024/04/Gemini_Generated_Image_pxek4spxek4spxek.webp
featured: false
publishedAt: 2024-04-05T12:22:27Z
updatedAt: 2024-04-05T12:22:27Z
excerpt: Despite best effort and preparation of your precious source code one day you might be facing the situation that there is one or more files in your development workspace that doesn't belong into your git repository.
twitterTitle: Untrack files in .gitignore
twitterDescription: Despite best effort and preparation of your precious source code one day you might be facing the situation that there is one or more files in your development workspace that doesn't belong into your git repository.
twitterImage: 
facebookTitle: Untrack files in .gitignore
facebookDescription: Despite best effort and preparation of your precious source code one day you might be facing the situation that there is one or more files in your development workspace that doesn't belong into your git repository.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Despite best effort and preparation of your precious source code one day you might be facing the situation that there is one or more files in your development workspace that doesn't belong into your git repository.

In general, that's a scenario to use the `.gitignore` file and exclude such file(s) from being considered or tracked for your repository. This works great but requires that you cover all your tracks regarding potential files, file extensions or folders you don't want to set under version control. Predicting the future is hard.

Plus, changes and audits happen. Meaning, a previously added file should be ignored from now on. Excluding such file in `.gitignore` won't work as expected out of the box. Such a file needs to be *untracked* first, and then excluded.

## Behold a single one

To untrack a *single* file that has already been added/initialized to your repository, *i.e.*, stop tracking the file but not delete it from your system use:

```
git rm --cached filename
```

To undo the previous command, add that single file back using `git add filename`.

## Hold my beer!

Occasionally, there is more than a single file to handle. Here's how to untrack *every* file that is now in your `.gitignore` and then add all other files back.

## First commit any outstanding code changes!

Then, run this command to untrack everything.

```
git rm -r --cached .
```

This removes any changed files from the *index* (staging area).

Afterwards, add everything back into the *index*, now respecting `.gitignore` excluding certain files and folders.

```
git add .
```

Note: Make sure to commit all your important changes before running `git add .` Otherwise, you will lose any changes to other files.

Complete the changes by commit.

```
git commit -m ".gitignore is now working"
```

## Note of caution

Please be careful, when you push this to a repository and pull from somewhere else into a state where those files are still tracked, those files will be **deleted**.

<small>Image credit: Gemini using prompt <i>create an image showing a junction of railroad tracks</i></small>