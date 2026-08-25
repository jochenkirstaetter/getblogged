---
uid: custom-page-sizes-in-paging-dropdown-in-telerik-radgrid
title: Custom page sizes in paging dropdown in Telerik RadGrid
date: 2012-11-08
status: published
type: post
description: This article describes how you can customize the default values (10, 20 and 50) of the drop-down list in the paging element of RadGrid.
tags:
- Development
keywords: Development
metaTitle: Custom page sizes in paging dropdown in Telerik RadGrid
metaDescription: This article describes how you can customize the default values (10, 20 and 50) of the drop-down list in the paging element of RadGrid.
image: content/images/2019/01/telerik_radgrid_custom_pagesize.webp
ogImage: content/images/2019/01/telerik_radgrid_custom_pagesize-og.webp
ogTitle: Custom page sizes in paging dropdown in Telerik RadGrid
ogDescription: Working with Telerik RadControls for ASP.NET AJAX is actually quite easy and the initial effort to get started with the control suite is very low. Meaning that you can easily get good result with...
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
canonicalUrl: https://jochen.kirstaetter.name/custom-page-sizes-in-paging-dropdown-in-telerik-radgrid/
imageUrl: content/images/2019/01/telerik_radgrid_custom_pagesize.webp
twitterImageUrl: https://jochen.kirstaetter.name/content/images/2019/01/telerik_radgrid_custom_pagesize.png
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2019/01/telerik_radgrid_custom_pagesize.webp
featured: false
publishedAt: 2012-11-08T15:07:31Z
updatedAt: 2019-01-28T03:05:30Z
excerpt: Working with Telerik RadControls for ASP.NET AJAX is actually quite easy and the initial effort to get started with the control suite is very low. Meaning that you can easily get good result with...
twitterTitle: Custom page sizes in paging dropdown in Telerik RadGrid
twitterDescription: Working with Telerik RadControls for ASP.NET AJAX is actually quite easy and the initial effort to get started with the control suite is very low. Meaning that you can easily get good result with...
twitterImage: 
facebookTitle: Custom page sizes in paging dropdown in Telerik RadGrid
facebookDescription: Working with Telerik RadControls for ASP.NET AJAX is actually quite easy and the initial effort to get started with the control suite is very low. Meaning that you can easily get good result with...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Working with [Telerik RadControls for ASP.NET AJAX](https://www.telerik.com/products/aspnet-ajax.aspx "Telerik RadControls for ASP.NET AJAX") is actually quite easy and the initial effort to get started with the control suite is very low. Meaning that you can easily get good result with little time. But there are usually cases where you have to go a little further and dig a little bit deeper than the standard scenarios. In this article I am going to describe how you can customize the default values (10, 20 and 50) of the drop-down list in the paging element of RadGrid. Get control over the displayed page sizes while using numeric paging...

![Telerik RadGrid with customized page size values](https://s.kirstaetter.name/images/telerik_radgrid_custom_pagesize.png "Telerik RadGrid with customized page size values")

## The default page sizes are good but not always good enough

The paging feature in RadGrid offers you 3, well actually 4, possible page sizes in the drop-down element out-of-the box, which are 10, 20 or 50 items. You can get a fourth option by specifying a value different than the three standards for the PageSize attribute, ie. 35 or 100. The drawback in that case is that it is the initial page size.

Certainly, the available choices could be more flexible or even a little bit more intelligent. For example, by taking the total count of records into consideration. There are some interesting scenarios that would justify a customized page size element:

- A low number of records, like 14 or similar shouldn't provide a page size of 50,
- A high total count of records (ie: 300+) should offer more choices, ie: 100, 200, 500, or
- display of all records regardless of number of records

I am sure that you might have your own requirements, and I hope that the following source code snippets might be helpful.

## Wiring the ItemCreated event

In order to adjust and manipulate the existing RadComboBox in the paging element we have to handle the OnItemCreated event of RadGrid. Simply specify your code behind method in the attribute of the RadGrid tag, like so:

```
<telerik:RadGrid ID="RadGridLive" runat="server" AllowPaging="true" PageSize="20"  
AllowSorting="true" AutoGenerateColumns="false" OnNeedDataSource="RadGridLive_NeedDataSource"  
OnItemDataBound="RadGrid_ItemDataBound" OnItemCreated="RadGrid_ItemCreated">  
<ClientSettings EnableRowHoverStyle="true">  
<ClientEvents OnRowCreated="RowCreated" OnRowSelected="RowSelected" />  
<Resizing AllowColumnResize="True" AllowRowResize="false" ResizeGridOnColumnResize="false"  
ClipCellContentOnResize="true" EnableRealTimeResize="false" AllowResizeToFit="true" />  
<Scrolling AllowScroll="true" ScrollHeight="360px" UseStaticHeaders="true" SaveScrollPosition="true" />  
<Selecting AllowRowSelect="true" />  
</ClientSettings>  
<MasterTableView DataKeyNames="AdvertID">  
<PagerStyle AlwaysVisible="true" Mode="NextPrevAndNumeric" />  
<Columns>  
<telerik:GridBoundColumn HeaderText="Listing ID" DataField="AdvertID" DataType="System.Int32"  
SortExpression="AdvertID" UniqueName="AdvertID">  
<HeaderStyle Width="66px" />  
</telerik:GridBoundColumn>
```

```
            <!--//  ... and some more columns ... -->
```

```
        </Columns>  
</MasterTableView>  
</telerik:RadGrid>
```

To provide a consistent experience for your visitors it might be helpful to display the page size selection always. This is done by setting the AlwaysVisible attribute of the PagerStyle element to true, like highlighted above.

## Customize the values of page size

Your delegate method for the ItemCreated event should look like this:

```
protected void RadGrid_ItemCreated(object sender, GridItemEventArgs e)  
{  
if (e.Item is GridPagerItem)  
{  
var dropDown = (RadComboBox)e.Item.FindControl("PageSizeComboBox");  
var totalCount = ((GridPagerItem)e.Item).Paging.DataSourceCount;  
var sizes = new Dictionary<string, string>() {  
{"10", "10"},  
{"20", "20"},  
{"50", "50"}  
};  
if (totalCount > 100)  
{  
sizes.Add("100", "100");  
}  
if (totalCount > 200)  
{  
sizes.Add("200", "200");  
}  
sizes.Add("All", totalCount.ToString());  
  
dropDown.Items.Clear();  
foreach (var size in sizes)  
{  
var cboItem = new RadComboBoxItem() { Text = size.Key, Value = size.Value };  
cboItem.Attributes.Add("ownerTableViewId", e.Item.OwnerTableView.ClientID);  
dropDown.Items.Add(cboItem);  
}  
dropDown.FindItemByValue(e.Item.OwnerTableView.PageSize.ToString()).Selected = true;  
}  
}
```

It is important that we explicitly check the event arguments for GridPagerItem as it is the control that contains the PageSizeComboBox control that we want to manipulate. To keep the actual modification and exposure of possible page size values flexible I am filling a Dictionary with the requested 'key/value'-pairs based on the number of total records displayed in the grid. As a final step, ensure that the previously selected value is the active one using the FindItemByValue() method.

Of course, there might be different requirements but I hope that the snippet above provide a first insight into customized page size value in Telerik's Grid. The Grid demos describe a [more advanced approach to customize the Pager](https://demos.telerik.com/aspnet-ajax/grid/examples/programming/customizingpager/defaultcs.aspx "more advanced approach to customize the Pager").