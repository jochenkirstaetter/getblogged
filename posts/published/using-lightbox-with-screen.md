---
uid: using-lightbox-with-screen
title: Using Lightbox with _Screen
slug: using-lightbox-with-screen
date: 2010-10-31
status: published
type: post
description: This article describes the steps about how to integrate and make use of Bernard's lightbox class in combination with _Screen in Visual FoxPro.
tags:
- Development
keywords: Development
metaTitle: Using Lightbox with _Screen
metaDescription: This article describes the steps about how to integrate and make use of Bernard's lightbox class in combination with _Screen in Visual FoxPro.
image: ''
ogTitle: Using Lightbox with _Screen
ogDescription: Although, I have to admit that I discovered Bernard Bout's ideas and concepts about implementing a lightbox in Visual FoxPro quite a while ago, there was no "spare" time in active projects that...
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
canonicalUrl: https://jochen.kirstaetter.name/using-lightbox-with-screen/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2010-10-31T07:06:08Z
updatedAt: 2018-04-02T08:38:55Z
excerpt: Although, I have to admit that I discovered Bernard Bout's ideas and concepts about implementing a lightbox in Visual FoxPro quite a while ago, there was no "spare" time in active projects that...
twitterTitle: Using Lightbox with _Screen
twitterDescription: Although, I have to admit that I discovered Bernard Bout's ideas and concepts about implementing a lightbox in Visual FoxPro quite a while ago, there was no "spare" time in active projects that...
twitterImage: 
facebookTitle: Using Lightbox with _Screen
facebookDescription: Although, I have to admit that I discovered Bernard Bout's ideas and concepts about implementing a lightbox in Visual FoxPro quite a while ago, there was no "spare" time in active projects that...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Although, I have to admit that I discovered Bernard Bout's ideas and concepts about implementing a lightbox in Visual FoxPro quite a while ago, there was no "spare" time in active projects that allowed me to have a closer look into his solution(s). Luckily, these days I received a demand to focus a little bit more on this. This article describes the steps about how to integrate and make use of Bernard's lightbox class in combination with _Screen in Visual FoxPro.

The requirement in this project was to be able to visually lock the whole application (_Screen area) and guide the user to an information that should not be ignored easily. Depending on the importance any current user activity should be interrupted and focus put onto the notification.

### Getting the "meat", eh, source code  
Please check out [Bernard's blog](https://weblogs.foxite.com/bernardbout/ "Bernard's blog") on [Foxite](https://www.foxite.com/ "Foxite") directly in order to get the latest and greatest version. As time of writing this article I use version 6.0 as described in this blog entry: [The Fastest Lightbox Ever](https://weblogs.foxite.com/bernardbout/archive/2009/09/21/8974.aspx "The Fastest Lightbox Ever")

The Lightbox class is sub-classed from the imgCanvas class from the GdiPlusX project on [VFPx](https://vfpx.codeplex.com/ "VFPx") and therefore you need to have the source code of GdiPlusX as well, and integrate it into your development environment. The version I use is available here: [Release GDIPlusX 1.20](https://vfpx.codeplex.com/releases/view/15083 "Release GDIPlusX 1.20")

As soon as you open the bbGdiLightbox class the first it, VFP might ask you to update the reference to the gdiplusx.vcx. As we have the sources, no problem and you have access to Bernard's code. The class itself is pretty easy to understand, some properties that you do not need to change and three methods: Setup(), ShowLightbox() and BeforeDraw()

### The challenge - _Screen or not?  
Reading Bernard's article about the fastest lightbox ever, he states the following:

*"The class will only work on a form. It will not support any other containers"*

Really? And what about _Screen? Isn't that a form class, too? [Yes, of course it is](https://weblogs.foxite.com/bernardbout/archive/2008/09/13/6768.aspx#6811 "Yes, of course it is") but nonetheless trying to use _Screen directly will fail. Well, let's have look at the code to see why:

```foxpro
WITH This
  .Left = 0
  .Top = 0
  .Height = ThisForm.Height
  .Width = ThisForm.Width
  .ZOrder(0)
  .Visible = .F.
ENDWITH
```

During the setup of the lightbox as well as while capturing the image as replacement for your forms and controls, the object reference *Thisform* is used. Which is a little bit restrictive to my opinion but let's continue.

The second issue lies in the method ShowLightbox() and introduced by the call of .Bitmap.FromScreen():

```foxpro
Lparameters tlVisiblilty
* tlVisiblilty - show or hide (T/F)
* grab a screen dump with controls
IF tlVisiblilty
  Local loCaptureBmp As xfcBitmap
  Local lnTitleHeight, lnLeftBorder, lnTopBorder, lcImage, loImage
  lnTitleHeight = IIF(ThisForm.TitleBar = 1,Sysmetric(9),0)
  lnLeftBorder = IIF(ThisForm.BorderStyle < 2,0,Sysmetric(3))
  lnTopBorder = IIF(ThisForm.BorderStyle < 2,0,Sysmetric(4))
  With _Screen.System.Drawing
    loCaptureBmp = .Bitmap.FromScreen(ThisForm.HWnd,;
      lnLeftBorder,;
      lnTopBorder+lnTitleHeight,;
      ThisForm.Width ,;
      ThisForm.Height)
  ENDWITH
  * save it to a property
  This.capturebmp = loCaptureBmp
  ThisForm.SetAll("Visible",.F.)
  This.DraW()
  This.Visible = .T.
ELSE
  ThisForm.SetAll("Visible",.T.)
  This.Visible = .F.
ENDIF
```

My first trials in using the class ended in an exception - GdiPlusError:OutOfMemory - thrown by the Bitmap object. Frankly speaking, this happened mainly because of my lack of knowledge about GdiPlusX. After reading some documentation, especially about the [FromScreen() method](https://weblogs.foxite.com/vfpimaging/archive/2007/01/17/3145.aspx "FromScreen() method") I experimented a little bit. Capturing the visible area of _Screen actually was not the real problem but the dimensions I specified for the bitmap.

### The modifications - step by step  
First of all, it is to get rid of restrictive object references on *Thisform* and to change them into either *This.Parent* or more generic into *This.oForm* (even better: *This.oControl*). The Lightbox.Setup() method now sets the necessary object reference like so:

```foxpro
*====================================================================
* Initial setup
* Default value: This.oControl = "This.Parent"
* Alternative:   This.oControl = "_Screen"
*====================================================================

With This
  .oControl = Evaluate(.oControl)

  If Vartype(.oControl) == T_OBJECT
    .Anchor = 0
    .Left = 0
    .Top = 0
    .Width = .oControl.Width
    .Height = .oControl.Height
    .Anchor = 15
    .ZOrder(0)
    .Visible = .F.
  EndIf
Endwith
```

Also, based on other developers' comments in Bernard articles on his lightbox concept and evolution I found the source code to handle the differences between a form and _Screen and goes into Lightbox.ShowLightbox() like this:

```foxpro
*====================================================================
* tlVisibility - show or hide (T/F)
* grab a screen dump with controls
*====================================================================
Lparameters tlVisibility

Local loControl
m.loControl = This.oControl

If m.tlVisibility
  Local loCaptureBmp As xfcBitmap
  Local lnTitleHeight, lnLeftBorder, lnTopBorder, lcImage, loImage

  lnTitleHeight = Iif(m.loControl.TitleBar = 1,Sysmetric(9),0)
  lnLeftBorder = Iif(m.loControl.BorderStyle < 2,0,Sysmetric(3))
  lnTopBorder = Iif(m.loControl.BorderStyle < 2,0,Sysmetric(4))

  With _Screen.System.Drawing
    If Upper(m.loControl.Name) == Upper("Screen")
      loCaptureBmp = .Bitmap.FromScreen(m.loControl.HWnd)
    Else
      loCaptureBmp = .Bitmap.FromScreen(m.loControl.HWnd,;
        lnLeftBorder,;
        lnTopBorder+lnTitleHeight,;
        m.loControl.Width ,;
        m.loControl.Height)
    EndIf
  Endwith

  * save it to a property
  This.CaptureBmp = loCaptureBmp
  m.loControl.SetAll("Visible",.F.)
  This.Draw()
  This.Visible = .T.
Else
  This.CaptureBmp = .Null.
  m.loControl.SetAll("Visible",.T.)
  This.Visible = .F.
Endif
```



Are we done? Almost... Although, Bernard says it clearly in his article:

*"Just drop the class on a form and call it as shown."*

It did not come clear to my mind in the first place with _Screen, but, yeah, he is right. Dropping the class on a form provides a permanent link between those two classes, it creates a valid *This.Parent* object reference. Bearing in mind that the lightbox class can not be "dropped" on the _Screen, we have to create the same type of binding during runtime execution like so:

```foxpro
*====================================================================
* Create global lightbox component
*====================================================================

Local llOk, loException As Exception
m.llOk = .F.
m.loException = .Null.

If Not Vartype(_Screen.Lightbox) == "O"
  Try
    _Screen.AddObject("Lightbox", "bbGdiLightbox")
  Catch To m.loException
    Assert .F. Message m.loException.Message
  EndTry
EndIf
m.llOk = (Vartype(_Screen.Lightbox) == "O")

Return m.llOk
```

Through runtime instantiation we create a valid binding to *This.Parent* in the lightbox object and the code works as expected with _Screen.

### Ease your life: Use properties instead of constants  
Having a closer look at the BeforeDraw() method might wet your appetite to simplify the code a little bit. Looking at the sample screenshots in Bernard's article you see several forms in different colors. This got me to modify the code like so:

```foxpro
*====================================================================
* Apply the actual lightbox effect on the captured bitmap.
*====================================================================

If Vartype(This.CaptureBmp) == T_OBJECT
  Local loGfx As xfcGraphics
  loGfx = This.oGfx

  With _Screen.System.Drawing
    loGfx.DrawImage(This.CaptureBmp,This.Rectangle,This.Rectangle,.GraphicsUnit.Pixel)
    * change the colours as needed here
    * possible colours are (220,128,0,0),(220,0,0,128) etc.
    loBrush = .SolidBrush.New(.Color.FromArgb( ;
      This.Opacity, .Color.FromRGB(This.BorderColor)))
    loGfx.FillRectangle(loBrush,This.Rectangle)
  Endwith
Endif
```

Create an additional property *Opacity* to specify the grade of translucency you would like to have without the need to change the code in each instance of the class. This way you only need to change the values of *Opacity* and *BorderColor* to tweak the appearance of your lightbox. This could be quite helpful to signalize different levels of importance (ie. green, yellow, orange, red, etc...) of notifications to the users of the application.

### Final thoughts

Using the lightbox concept in combination with _Screen instead of forms is possible. Already Jim Wiggins comments in Bernard's article to [loop through the _Screen.Forms collection](https://weblogs.foxite.com/bernardbout/archive/2009/09/21/8974.aspx#10068 "loop through the _Screen.Forms collection") in order to cascade the lightbox visibility to all active forms. Good idea. But honestly, I believe that instead of looping all forms one could use _Screen.SetAll("ShowLightbox", .T./.F., "Form") with Form.ShowLightbox_Access method to gain more speed. The modifications described above might provide even more features to your applications while consuming less resources and performance. Additionally, the restrictions to capture only forms does not exist anymore. Using _Screen you are able to capture and cover anything.

The captured area of _Screen does not include any toolbars, docked windows, or menus. Therefore, it is advised to take this concept on a higher level and to combine it with additional classes that handle the state of toolbars, docked windows and menus. Which I did for the customer's project.