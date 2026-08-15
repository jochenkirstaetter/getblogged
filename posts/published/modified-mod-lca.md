---
uid: modified-mod-lca
title: Modified Mod LCA
slug: modified-mod-lca
date: 2010-01-23
status: published
type: post
description: 'Joomla!s own archive functionality works in a similar way but sadly I experienced own mayor drawback: Archived articles are not part of the internal search engine anymore and therefore results are not displayed.'
tags:
- Development
keywords: Development
metaTitle: Modified Mod LCA
metaDescription: 'Joomla!s own archive functionality works in a similar way but sadly I experienced own mayor drawback: Archived articles are not part of the internal search engine anymore and therefore results are not displayed.'
image: ''
ogTitle: Modified Mod LCA
ogDescription: Joomla! content management system (CMS) is great for websites of any type in general. Even using the system as a blog software is quite easy to configure. Instead of the classical Frontpage Layout as...
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
canonicalUrl: https://jochen.kirstaetter.name/modified-mod-lca/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2010-01-23T11:06:39Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Joomla! content management system (CMS) is great for websites of any type in general. Even using the system as a blog software is quite easy to configure. Instead of the classical Frontpage Layout as...
twitterTitle: Modified Mod LCA
twitterDescription: Joomla! content management system (CMS) is great for websites of any type in general. Even using the system as a blog software is quite easy to configure. Instead of the classical Frontpage Layout as...
twitterImage: 
facebookTitle: Modified Mod LCA
facebookDescription: Joomla! content management system (CMS) is great for websites of any type in general. Even using the system as a blog software is quite easy to configure. Instead of the classical Frontpage Layout as...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Joomla! content management system (CMS) is great for websites of any type in general. Even using the system as a blog software is quite easy to configure. Instead of the classical Frontpage Layout as default you configure the system to use one of the available Blog Layouts as default page. Then some tweaks according to leading articles, columns, etc. and you are almost done. Almost...

One of the great features that I like with blog application is the ability to display an Archive list of existing articles based on their creation date. Well, Joomla!s own archive functionality works in a similar way but sadly I experienced own mayor drawback: Archived articles are not part of the internal search engine anymore and therefore results are not displayed.

After my usual online research I found a recently added Joomla! extension called [Mod LCA](https://extensions.joomla.org/extensions/news-display/articles-listing/10731) of JoniJnm. The description gives the direct motivation / link to other blog applications:

> Mod LCA shows articles sorted by year and month, such as wordpress or blogspot

The module itself is really easy to install and works as expected. Almost...

In case that your content is created the usual way, Mod LCA is just fine. But in my special case I did some direct data migrations via SQL statements from my previous blog software and therefore my sequence of itemids differs from the original creation date of an article. It was quite funny to see that an article of June 2006 was listed in December 2009 by Mod LCA. But hey, when does it happen that the ID and the creation date are controversal? Not quite often but it can happen like in case.

Alright, having a look at the source code files of Mod LCA gives a direct glue about how we can improve the situation. At least, it's nothing complicated but the correct order clause of a SQL statement, or? And there we go...

Before any modifications be aware to have a backup at hand. Open the file mod_lca/helper.php with your favourite text editor and change the query statement like so:


```
$query = 'SELECT a.id, a.title, a.alias, a.catid, a.sectionid, c.alias as calias, '.  
$created.  
' FROM #__content AS a'.  
' LEFT JOIN #__categories AS c ON c.id=a.catid'.  
' LEFT JOIN #__sections AS s ON s.id=a.sectionid'.  
' WHERE ( a.state = 1 AND s.id > 0 )' .  
' AND ( a.publish_up = '.$db->Quote($nullDate).' OR a.publish_up <= '.$db->Quote($now).' )'.  
' AND ( a.publish_down = '.$db->Quote($nullDate).' OR a.publish_down >= '.$db->Quote($now).' )'.  
' AND s.published = 1'.  
' AND c.published = 1'.  
' ORDER BY **a.created DESC**';  
$db->setQuery($query);  
  
... some lines down ...  
  
$out[$d[0]][$month][] = '<a href="'.$link.'">'.**htmlspecialchars(**$row->title**)**.'</a>';
```


*Modified code of mod_lca/helper.php*

The original code orders the result set by a.id and this might cause problems. With this minor code change articles are queried in the expected order and as a consequence in my case my 'Article Time Line' in the sidebar is properly rendered and displayed.

After running some validation tests according to XHTML 1.0 compliance I did some more modifications to mod_lca. By adding the PHP function htmlspecialchars() to encode the output of the article title you will get properly encoded special characters in your hyperlinks. This modification has to be done in the helper.php file as you can see above.

To create the tree hierarchy of the article list based on year and month, mod_lca needs some CSS and JavaScript instructions. Well, for the JavaScript it is not a problem itself but the CSS styles should not be placed with the &lt;body&gt; tag of the rendered page. To improve this situation it is necessary to tidy some code of mod_lca.


```
if (!DEFINED("LCA_HEADER")) {  
// If cache is enabled, we can't add css neither js files  
  
define("LCA_HEADER", 1);  
echo '  
**(<style> section deleted)**  
<script type="text/javascript">
```


*Modified code of mod_lca/tmpl/default.php*

The key of this solution is to move the style information away from the module and into the template CSS file or if you prefer in its own CSS file. To reduce the number of HTTP requests the styles should be in the template.css file.


```
/********  
mod_LCA  
********/  
li.lca {  
display: block  
}  
ul.lca {  
padding: 0px  
}  
span.lca {  
cursor: pointer  
}
```


*Modified CSS code of template.css*

The consequence of those slight modifications is that XHTML validation of my site produces roughly 30 errors less than before. Depending on your content this may vary, of course... ;-)