---
uid: gdg-cloud-munich
title: "Speaking at GDG Cloud Munich: State of GCP (.NET Edition)"
date: 2023-11-18
status: draft
type: post
description: Ahead of the Google I/O Connect event in Amsterdam there had been exchange with the organisers of GDG Cloud Munich. Thankfully, they accepted a proposal to speak. Why Munich, you ask. It's quite far...
metaDescription: "Exploring C# and .NET on Google Cloud Platform: live demos, Minimal APIs, NuGet integration, and Cloud Functions at GDG Cloud Munich."
tags:
  - Community
keywords: Community
image: content/images/2023/11/gdg-cloud-munich.webp
ogImage: content/images/2023/11/gdg-cloud-munich-og.webp
layout: post
bodyClass: post-template tag-community
postClass: post tag-community
isPost: true
isPage: false
isDraft: true
isScheduled: false
isTagPage: false
isTagsIndexPage: false
isAuthorPage: false
isHome: false
author: Jochen Kirstätter
authorTwitter: "@jkirstaetter"
authorFacebook: https://facebook.com/jochen.kirstaetter
authorImage: content/images/2018/10/JoKi_StAubin_100px.webp
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/gdg-cloud-munich/
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
featured: false
publishedAt: ""
updatedAt: 2024-02-11T08:44:29Z
---
Ahead of the Google I/O Connect event in Amsterdam there had been exchange with the organisers of [GDG Cloud Munich](https://gdg.community.dev/gdg-cloud-munich/). Thankfully, they accepted a proposal to speak. Why Munich, you ask. It's quite far from Amsterdam.

## Connecting with GDG Cloud Munich

Given the circumstances that I had to do some of my annual health check-ups and examinations in Germany I crammed a couple of activities into a single trip to Europe. One of them required to stop for a couple of days in Munich. As I was looking for community events around the same time I noticed that the GDG Cloud chapter might have something coming up.

Hence I reached out to Yevgen to see whether there would be a possibility of a meetup around that time, and in case there could be interest in a certain topic. Turns out that both requests aligned nicely and in consequence I was invited to speak at their hybrid event in June.

The topic was "State of GCP: .NET Edition" which covers a range of products and services offered by [Google Cloud Platform (GCP)](https://cloud.google.com/) that can be used in combination with Microsoft .NET technology stack, in particular with C#.

## Why C# and Google Cloud?

Hang on, C# and Google?  

![Source: https://www.tiobe.com/tiobe-index/ ](../content/images/2023/11/uNqLq0ZJtzAvxzpqH2zkZQejEp3Ce8dDcCaupj74g1sJr6j17aEVQf5j-9iX7BZLFIc8rwKb9DM3q_TgnILL3FJ1NInZzmL9YMFOEsYnWP69iKs0HBvkAM9lvf_yNbqoA5-hpvwHzle4LgCPisnVhLlN=s2048.webp)

Personally, it allows me to leverage my existing knowledge and doesn't require me to dig deeper into other programming languages like JavaScript, Go, Python, and so forth, in order to benefit from [Google Cloud](https://cloud.google.com/), and it also shows that one isn't locked in to cloud computing provided by Microsoft Azure while using C# applications. Bearing this in mind, it's actually a solid way to build so-called cross-cloud or multi-cloud solutions.

## Addressing Misconceptions & Starting with .NET

I was given approximately one hour to present about .NET. After setting up the system and being introduced by Yevgen to the in-person and online audience I started to address a couple of potential misconceptions regarding Microsoft .NET and C#. The majority of the audience had never used C# before and I was curious about some of the reasons. This then allowed me to go with the flow and clarify some statements. I added up a few practical examples from my experience and then bridged the discussion to Google Cloud services that can be used as part of the solution. Again sharing some of the obstacles and pitfalls observed and handled in the process.

Some of the questions asked indicated that there is quite some work to do removing a slightly negative reputation of the Microsoft .NET eco-system, simply because it's Microsoft (maybe its past?), whereas other questions looked behind that facade and brought up comparison to other existing approaches like backend development with Node.js and Express, and how C# could be useful for such backend services.

To begin with .NET development I explained the [*dotnet* CLI tool](https://learn.microsoft.com/en-us/dotnet/core/tools/) and how project templates get you started.

![Getting started with .NET CLI and project templates](../content/images/2023/11/GE7cNRtch-j07CuvqrRQuMIOp5oKtR8MHt573fsv_MNhTg-CT2RLZWkpt50u4RaG9yiTczeQCfshFVkvv6mAulhHPfzf_873z6wt0_EyI6uSOxZshwZqP9-bv2Yhrdf1n4tBNThODEq5LebCkJlEK-N2=s2048.webp)

The important part is the installation of the [`Google.Cloud.Functions.Templates`](https://www.nuget.org/packages/Google.Cloud.Functions.Templates) into your `dotnet` environment.
## Minimal APIs & NuGet in VS Code

When I launched the terminal in [Visual Studio Code](https://code.visualstudio.com/) and started to show how a sample API application is developed in C#, using [Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis), the interest level in the audience rose instantly. I showed the generated source code and how easy it is to get going right away. Some remarks were like "hey, that really looks like Express", "Oh, are those arrow functions?" (meaning anonymous delegates), and "that looks neat and clean".

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello from .NET on Google Cloud!");

app.Run();
```

Next, I ventured into the NuGet package management and how developers can integrate any package into their project seamlessly. Especially showing the over 700 NuGet packages available to use [Google APIs for .NET](https://cloud.google.com/dotnet/docs/reference) for all kinds of services and functionalities.

![Browsing Google API NuGet packages for .NET](../content/images/2023/11/evV8iZxybA-TELu0795QGJn2HPcxDvbXswOu-TRmiOJIaDXdTcOnyM7dVhRSyWI5uAx8jP3vHbQ-nT7lIPshrWrUV75QAie0Gf6DC83ecHLIT8FD33k4ABqpSw9xWNfSGJDslHlFIj8_VaH-pQ6QpeTk=s2048.webp)

Also mentioning that the package management is less space-consuming and easier to maintain compared to Node modules.

Lastly, it was time to deploy to Google Cloud. All this time I stayed in VS Code and never had to switch focus to another application. The [Cloud Code extension for VS Code](https://cloud.google.com/code/docs/vscode) provides you access to your resources in the cloud, and using the `gcloud` CLI tool does the rest of the job. Deploying the newly created API service to [App Engine Flexible](https://cloud.google.com/appengine/docs/flexible) was done quickly.

## Serverless with Google Cloud Functions

What about serverless? Let's do it. I explained that the `dotnet` CLI tool can be extended with project templates and showed that there are project templates targeting [Google Cloud Functions](https://cloud.google.com/functions/docs/concepts/dotnet-development).

```bash
# Install Google Cloud Function templates
dotnet new install Google.Cloud.Functions.Templates
```

First, I created a new Google Cloud function using the HTTP endpoint trigger.

```bash
# Create an HTTP Function
dotnet new gcf-http -n DevFest
```

Showed the source code and the necessary implementation of the interface, renamed the entry function to `Greeting`.

```csharp
using Google.Cloud.Functions.Framework;
using Microsoft.AspNetCore.Http;
using System.Threading.Tasks;

namespace DevFest;

public class Greeting : IHttpFunction
{
    /// <summary>
    /// Logic for your function goes here.
    /// </summary>
    /// <param name="context">The HTTP context, containing the request and the response.</param>
    /// <returns>A task representing the asynchronous operation.</returns>
    public async Task HandleAsync(HttpContext context)
    {
        await context.Response.WriteAsync("Hello, Functions Framework.", context.RequestAborted);
    }
}
```

And how to deploy it using the `gcloud` CLI tool.

```bash
# Deploy via gcloud CLI

gcloud functions deploy my-http-function \
    --region=us-central1 \
    --gen2 \
    --runtime=dotnet10 \
    --source=. \
    --entry-point=DevFest.Greeting \
    --trigger-http \
    --memory=128M \
    --max-instances=5 \
    --allow-unauthenticated
```

With an active Cloud billing account, enabled APIs - Cloud Functions and Artifact Registry -, as well as local `gcloud` authentication, it's roughly a matter of five minutes from start to finish.

If not sure, you can retrieve a list of available runtimes in a region like this:

```bash
gcloud functions runtimes list --region=us-central1
```

Then, I did the same using the project template for an event-triggered Google Cloud function.

```bash
dotnet new gcf-event -n DevFest
```

And explained the flexibility of the type-induced interface to create functions handling different types of data loads. The default type is `StorageObjectData` which I changed to `MessagePublishedData` to explain how a function can be used to handle a Pub/Sub message.

![Event-triggered Google Cloud Function implementation in .NET](../content/images/2023/11/yAl9VB2ZTh5lc5W1JoEceHhODXO_rp0wcd5uXD6jGeRozjDD0i_KiFayOPMunBrQEenf5hoduIXeMrPXCwtiI0kY-Pn1AypawInSvPJgX_BBgqP85a1P82uNkIrzoIq6PFJinEWdfiYb_GIFv0Ypawes=s2048.webp)

And thanks to the [Google Cloud Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-dotnet) and local hosting, you can launch, test, and debug your code before deploying it to Google Cloud.

```bash
dotnet run
```

## Conclusion & Wrap-Up

Gratefully, with every piece of source code shown and sharing my experience of combining C# implementation using NuGet packages and how to deploy it to GCP there were more and more questions in the audience. Finally, the team at GDG Cloud Munich signalled that we were running out of time, and I wrapped it up quickly with my opinionated conclusion of using C# together with the rich .NET eco-system in order to develop scalable, enterprise-ready, and cloud-native solutions using Google Cloud Platform.

I was humbled by the audience's interest to know more and the numerous follow-up questions regarding the talk and the live demos shown. Thanks!

My heart-felt thanks and best wishes to the organising team of GDG Cloud Munich, namely Yevgen Batovskyi and Spyros Kyriazatis, for this opportunity to talk and share my passion. It was an amazing evening at the Google office in Munich.

PS: Apart from the announcement screen the whole talk was a *no slide deck presentation* purely based on me talking about the history, the evolution, the current state of C# and .NET, and how it fares together with GCP based on my experience.

---

## References & Links

- [GDG Cloud Munich Community](https://gdg.community.dev/gdg-cloud-munich/)
- [Google Cloud for .NET Developers](https://cloud.google.com/dotnet)
- [Google Cloud Functions .NET Framework on GitHub](https://github.com/GoogleCloudPlatform/functions-framework-dotnet)
- [Google Cloud Client Libraries for .NET on NuGet](https://www.nuget.org/packages?q=Google.Cloud)
- [Cloud Code for Visual Studio Code](https://cloud.google.com/code/docs/vscode)
- [TIOBE Index](https://www.tiobe.com/tiobe-index/)

---

## Join the Conversation

Have you experimented with deploying C# and .NET workloads to Google Cloud Platform or building serverless event handlers with Google Cloud Functions? What was your experience integrating NuGet packages with Google Cloud services outside of Azure?

Feel free to connect and share your thoughts with me on X ([@JKirstaetter](https://x.com/jkirstaetter)), BlueSky ([@jochen.kirstaetter.name](https://bsky.app/profile/jochen.kirstaetter.name)), or Mastodon ([@JKirstaetter](https://mastodon.social/@jkirstaetter)). You can also subscribe to [my blog's RSS feed](https://jochen.kirstaetter.name/rss/) for upcoming articles and technical write-ups.

---

<small>Picture credits: Mary Jane Kirstätter and Inna Zaytseva</small>