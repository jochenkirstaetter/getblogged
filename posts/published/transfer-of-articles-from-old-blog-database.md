---
uid: transfer-of-articles-from-old-blog-database
title: Transfer of articles from old blog database
date: 2008-02-18
status: published
type: post
description: 'Transfer of articles from old blog database After the successful transfer of my articles from Foxite, I finally converted another bunch of articles from my old blog software. The process itself was quite easy: query database, convert records to XML and write out files.The interesting part is that the original'
tags:
- Development
keywords: Development
metaTitle: Transfer of articles from old blog database
metaDescription: 'Transfer of articles from old blog database After the successful transfer of my articles from Foxite, I finally converted another bunch of articles from my old blog software. The process itself was quite easy: query database, convert records to XML and write out files.The interesting part is that the original'
image: ''
ogTitle: Transfer of articles from old blog database
ogDescription: 'After the successful transfer of my articles from Foxite, I finally converted another bunch of articles from my old blog software. The process itself was quite easy: query database, convert records to...'
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
canonicalUrl: https://jochen.kirstaetter.name/transfer-of-articles-from-old-blog-database/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2008-02-18T05:33:27Z
updatedAt: 2018-04-02T08:39:11Z
excerpt: 'After the successful transfer of my articles from Foxite, I finally converted another bunch of articles from my old blog software. The process itself was quite easy: query database, convert records to...'
twitterTitle: Transfer of articles from old blog database
twitterDescription: 'After the successful transfer of my articles from Foxite, I finally converted another bunch of articles from my old blog software. The process itself was quite easy: query database, convert records to...'
twitterImage: 
facebookTitle: Transfer of articles from old blog database
facebookDescription: 'After the successful transfer of my articles from Foxite, I finally converted another bunch of articles from my old blog software. The process itself was quite easy: query database, convert records to...'
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
After the successful transfer of my articles from Foxite, I finally converted another bunch of articles from my old blog software. The process itself was quite easy: query database, convert records to XML and write out files.  
  
The interesting part is that the original data was stored in a MySQL database. So, I had to install the MyODBC driver to gain access to it and the rest is pure FoxPro. Have a look at the code:  
```
*  
Migration: blogMachine to DasBlog  
  
  
Set Safety Off    Local lnHandle, lnResult, lcAlias, lcSqlStatement, ;          laSql[1], ltDate, lcXml, lcFile, lcContent    m.lnHandle = 0  
m.lnResult = 0  
m.lcAlias = "blogmachine"    m.lcSqlStatement = ""    m.lcXml = ""    m.lcFile = ""    m.lcContent = ""        m.lnHandle = SQLStringConnect("DRIVER={MySQL ODBC 3.51 Driver};" + ;  
"SERVER=jochen.kirstaetter.name;PORT=3306;" + ;  
"DATABASE=blog;OPTION=19035;UID=joki;PWD=topsecret", .T.)  
  
If m.lnHandle > 0  
DECLARE INTEGER CoCreateGuid IN Ole32.dll STRING @lcGUIDStruc  
DECLARE INTEGER StringFromGUID2 IN Ole32.dll STRING cGUIDStruc, STRING @cGUID, LONG nSize  
  
Text To m.lcSqlStatement NoShow Flags 1 Pretext 1+2+4+8  
Select post.title As p_title, post.summary As p_summary,  
post.date As p_date, cat.cat_name As c_name  
From bmc_posts post  
Left Outer Join bmc_cats cat On post.cat = cat.id  
Order By post.date        EndText        m.lnResult = SQLExec(m.lnHandle, m.lcSqlStatement, m.lcAlias, laSql)  
If m.lnResult > 0 .And. Used(m.lcAlias)  
Select(m.lcAlias)  
Scan  
m.ltDate = Datetime(1970,1,1,0,0,0) + Nvl(Cast(p_date As Integer), 0)  
m.lcFile = GetWordNum(Ttoc(Ttod(m.ltDate),3),1,"T") + ".dayentry.xml"                Text To m.lcXml TextMerge NoShow Flags 1 Pretext 4  
<?xml version="1.0" encoding="utf-8"?>  
<DayEntry xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance"  
xmlns:xsd="https://www.w3.org/2001/XMLSchema"  
xmlns="urn:newtelligence-com:dasblog:runtime:data">  
<Date><<Ttoc(Ttod(m.ltDate)+0.04167,3)>>+01:00</Date>  
<Entries>  
<Entry>  
<Content><<Strtran(Alltrim(p_summary), Chr(13)+Chr(10), "&"+"lt;br"+"&"+"gt;"+Chr(13)+Chr(10))>></Content>  
<Created><<Ttoc(Ttod(m.ltDate),3)>>.000+01:00</Created>  
<Modified><<Ttoc(Ttod(m.ltDate),3)>>.0000000+01:00</Modified>  
<EntryId><<Lower(Chrtran(GetGuid(), "{}", ""))>></EntryId>  
<Description />  
<Title><<Alltrim(p_title)>></Title>  
<Categories><<Alltrim(c_name)>></Categories>  
<Author>JoKi</Author>  
<IsPublic>true</IsPublic>  
<Syndicated>true</Syndicated>  
<ShowOnFrontPage>true</ShowOnFrontPage>  
<AllowComments>true</AllowComments>  
<Attachments />  
<Crossposts />  
</Entry>  
</Entries>  
</DayEntry>  
EndText  
  
If File(m.lcFile)  
m.lcXml = StrExtract(m.lcXml, "<Entry>", "</Entry>", 1, 4)  
m.lcContent = FileToStr(m.lcFile)  
m.lcXml = Strtran(m.lcContent, "</Entries>", m.lcXml + Chr(13) + Chr(10) + "</Entries>", 1, 1, 1)  
EndIf  
? Alltrim(p_Title) + " " + Transform(m.ltDate)  
StrToFile(m.lcXml, m.lcFile)  
EndScan  
Else            Assert .F.            ? AError(m.laSql)        EndIf        SQLDisconnect(m.lnHandle)    EndIfPROCEDURE GetGuid() As String    cStrucGUID=SPACE(16)  
cGUID=SPACE(80)  
nSize=40  
IF CoCreateGuid(@cStrucGUID) # 0  
RETURN ""    ENDIF    IF StringFromGUID2(cStrucGUID,@cGuid,nSize) = 0  
RETURN ""    ENDIFRETURN STRCONV(LEFT(cGUID,76),6)  
```

There are some interesting parts in this conversion of data:  
- First, the MySQL field names are resevered key words in VFP, so that they have to be renamed before usage.

* Second, datetime conversion from Unix datetime to 'normal' datetime. This is quite simple:

```
m.ltDate = Datetime(1970,1,1,0,0,0) + Nvl(Cast(p_date As Integer), 0)
```

- Third, datetime string conversion between VFP and .NET. Herefore, we simply use VFP Ttoc() function with '3' as second parameter:

```
Ttoc(Ttod(m.ltDate),3)
```

This provides a proper character string with XML DateTime format. See VFP's help file for details.  
- And fourth, generation of a Global Unique IDentifier (GUID) in VFP. This is done with two Win32 API calls. Also nothing extraordinary.

At the moment, this conversion gives me some more categories and increases the number of article to 85. But as you might see on the 'Archive' box on the right side, there is still a huge gap between October 2006 and January 2008. There are more articles to come, but this requires another conversion. The missing entries are part of my AfpWiki database which runs on Microsoft SQL Server. So, stay tuned, you'll get a full package within these days.

Sincerely, JoKi