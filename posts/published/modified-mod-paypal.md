---
uid: modified-mod-paypal
title: Modified Ultimate Paypal Donations Module
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
<form action="https://www.paypal.com/cgi-bin/webscr" method="post">  
<input type="hidden" name="cmd" value="_donations" **/**>  
<input type="hidden" name="business" value="<?php echo $paypal_emailID; ?>" **/**>  
<input type="hidden" name="item_name" value="<?php echo $item_name; ?>" **/**>  
<?php if ($item_number)  
{  
echo "<input type=\"hidden\" name=\"item_number\" value=\"" . $item_number . "\" **/**>\r\n";  
}  
?>  
<?php **if ($amount)**  
{  
echo "<input type=\"hidden\" name=\"amount\" value=\"" . $amount . "\" **/**>\r\n";  
echo "<input type=\"hidden\" name=\"lc\" value=\"" . $location . "\" **/**>\r\n";  
}  
?>  
<input type="hidden" name="no_shipping" value="0" **/**>  
<input type="hidden" name="no_note" value="1" **/**>  
<input type="hidden" name="currency_code" value="<?php echo $currency_code; ?>" **/**>  
<input type="hidden" name="tax" value="0" **/**>  
<input type="hidden" name="bn" value="PP-DonationsBF" **/**>  
<?php if ($image_choice==1)  
{  
echo "<input type=\"image\" **border=\"0\"** src=\"" . $donate_image . "\" name=\"submit\"  
alt=\"PayPal - The safer, easier way to pay online!\" **/**>\r\n";  
}else{  
echo "<input type=\"image\" **border=\"0\"** src=\"" . $own_donate_image . "\" name=\"submit\"  
alt=\"PayPal - The safer, easier way to pay online!\" **/**>\r\n";  
}  
?>  
</form>
```


*Modified version of mod_paypal-j15/tmpl/default.php*

Despite the tooltip description about choosing your own PayPal button for this module you do not need to specify the full URL including https:// prefix. As you can see in the PHP code any relative path is working too. For reduced number of DNS lookups you should get your preferred PayPal button on your server and change the module to use your 'own' image.

In my changes above you also see a marked if-statement in the code. Well, in the original code there are two identical statements, I just merged them together for better reading.

Add last but not least, I removed the border attribute from input tags that displays the PayPal image on your site. Style information like border attributes belong to CSS files and should not be part of the HTML code.