---
uid: modified-mod-paypal
title: Modified Ultimate Paypal Donations Module
slug: modified-mod-paypal
date: 2010-02-17
status: published
type: post
description: Modifications for Ultimate Paypal Donations Module by JoomlaSpan to provide any kind of PayPal donation element on your site is really easy and straight forward.
tags:
- Development
keywords: Development
metaTitle: Modified Ultimate Paypal Donations Module
metaDescription: Modifications for Ultimate Paypal Donations Module by JoomlaSpan to provide any kind of PayPal donation element on your site is really easy and straight forward.
image: ''
ogTitle: Modified Ultimate Paypal Donations Module
ogDescription: The article describes some opinions and modifications for a Joomla! extension called Ultimate Paypal Donations Module by JoomlaSpan.
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
canonicalUrl: https://jochen.kirstaetter.name/modified-mod-paypal/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2010-02-17T15:00:06Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: The article describes some opinions and modifications for a Joomla! extension called Ultimate Paypal Donations Module by JoomlaSpan.
twitterTitle: Modified Ultimate Paypal Donations Module
twitterDescription: The article describes some opinions and modifications for a Joomla! extension called Ultimate Paypal Donations Module by JoomlaSpan.
twitterImage: 
facebookTitle: Modified Ultimate Paypal Donations Module
facebookDescription: The article describes some opinions and modifications for a Joomla! extension called Ultimate Paypal Donations Module by JoomlaSpan.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
The article describes some opinions and modifications for a Joomla! extension called [Ultimate Paypal Donations Module](https://extensions.joomla.org/extensions/e-commerce/donations/5318) by JoomlaSpan.

First of all I have to say that using this extension to provide any kind of PayPal donation element on your site is really easy and straight forward. You just install it, setup your parameters and mdoule location and you are done. It could not be better...

Well, it could.

Actually, my main problem with this module is about XHTML 1.0 compliance. Sadly to see that the current version (as of writing this article) does not follow the W3C rules about XHTML 1.0. Luckily, the necessary changes are very simple to realize by modfying one PHP file. Following is the modified version:


```
&lt;form action="https://www.paypal.com/cgi-bin/webscr" method="post"&gt;  
&lt;input type="hidden" name="cmd" value="\_donations" **/**&gt;  
&lt;input type="hidden" name="business" value="&lt;?php echo $paypal\_emailID; ?&gt;" **/**&gt;  
&lt;input type="hidden" name="item\_name" value="&lt;?php echo $item\_name; ?&gt;" **/**&gt;  
&lt;?php if ($item\_number)  
{  
echo "&lt;input type=\"hidden\" name=\"item\_number\" value=\"" . $item\_number . "\" **/**&gt;\r\n";  
}  
?&gt;  
&lt;?php **if ($amount)**  
{  
echo "&lt;input type=\"hidden\" name=\"amount\" value=\"" . $amount . "\" **/**&gt;\r\n";  
echo "&lt;input type=\"hidden\" name=\"lc\" value=\"" . $location . "\" **/**&gt;\r\n";  
}  
?&gt;  
&lt;input type="hidden" name="no\_shipping" value="0" **/**&gt;  
&lt;input type="hidden" name="no\_note" value="1" **/**&gt;  
&lt;input type="hidden" name="currency\_code" value="&lt;?php echo $currency\_code; ?&gt;" **/**&gt;  
&lt;input type="hidden" name="tax" value="0" **/**&gt;  
&lt;input type="hidden" name="bn" value="PP-DonationsBF" **/**&gt;  
&lt;?php if ($image\_choice==1)  
{  
echo "&lt;input type=\"image\" **border=\"0\"** src=\"" . $donate\_image . "\" name=\"submit\"  
alt=\"PayPal - The safer, easier way to pay online!\" **/**&gt;\r\n";  
}else{  
echo "&lt;input type=\"image\" **border=\"0\"** src=\"" . $own\_donate\_image . "\" name=\"submit\"  
alt=\"PayPal - The safer, easier way to pay online!\" **/**&gt;\r\n";  
}  
?&gt;  
&lt;/form&gt;
```


*Modified version of mod\_paypal-j15/tmpl/default.php*

Despite the tooltip description about choosing your own PayPal button for this module you do not need to specify the full URL including https:// prefix. As you can see in the PHP code any relative path is working too. For reduced number of DNS lookups you should get your preferred PayPal button on your server and change the module to use your 'own' image.

In my changes above you also see a marked if-statement in the code. Well, in the original code there are two identical statements, I just merged them together for better reading.

Add last but not least, I removed the border attribute from input tags that displays the PayPal image on your site. Style information like border attributes belong to CSS files and should not be part of the HTML code.