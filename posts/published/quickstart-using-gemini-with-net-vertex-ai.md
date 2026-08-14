---
uid: quickstart-using-gemini-with-net-vertex-ai
title: 'Quickstart: Use Gemini with .NET (Vertex AI)'
slug: quickstart-using-gemini-with-net-vertex-ai
date: 2024-04-03
status: published
type: post
description: Use Gemini in .NET in shortest time following this quickstart to configure Vertex AI on Google Cloud and add generative AI features to your apps.
tags:
- Development
keywords: Development
metaTitle: 'Quickstart: Use Gemini with .NET (Vertex AI)'
metaDescription: Use Gemini in .NET in shortest time following this quickstart to configure Vertex AI on Google Cloud and add generative AI features to your apps.
image: content/images/2024/04/Gemini_Generated_Image.webp
ogTitle: 'Quickstart: Use Gemini with .NET (Vertex AI)'
ogDescription: Use Gemini in .NET in shortest time following this quickstart to configure Vertex AI on Google Cloud and add generative AI features to your apps.
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
canonicalUrl: https://jochen.kirstaetter.name/quickstart-using-gemini-with-net-vertex-ai/
imageUrl: content/images/2024/04/Gemini_Generated_Image.webp
twitterImageUrl: https://jochen.kirstaetter.name/content/images/2024/04/Gemini_Generated_Image.jpeg
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2024/04/Gemini_Generated_Image.webp
featured: false
publishedAt: 2024-04-03T09:31:20Z
updatedAt: 2024-04-03T09:32:49Z
excerpt: Use Gemini in .NET in shortest time following this quickstart to configure Vertex AI on Google Cloud and add generative AI features to your apps.
twitterTitle: 'Quickstart: Use Gemini with .NET (Vertex AI)'
twitterDescription: Use Gemini in .NET in shortest time following this quickstart to configure Vertex AI on Google Cloud and add generative AI features to your apps.
twitterImage: 
facebookTitle: 'Quickstart: Use Gemini with .NET (Vertex AI)'
facebookDescription: Use Gemini in .NET in shortest time following this quickstart to configure Vertex AI on Google Cloud and add generative AI features to your apps.
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
This quickstart shows you how to get started with the Gemini API in Vertex AI on Google Cloud using an SDK for .NET called [Mscc.GenerativeAI](https://www.nuget.org/packages/Mscc.GenerativeAI/).

## Prerequisites

To complete this quickstart locally, ensure that your .NET development meets the following requirements:

- .NET 6+ or
- .NET Framework 4.7.2+
- Account on Google Cloud

The NuGet package also supports .NET Standard 2.0.

## Get set up on Google Cloud

To get you started using Vertex AI, follow the [instructions in the official guide](https://cloud.google.com/vertex-ai/docs/start/cloud-environment). You need to complete the following steps:

- Set up a project
- Enable billing for the Google Cloud project
- Enable Vertex AI APIs
- Install the Google Cloud CLI
- [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) (ADC)

In conclusion, you need the project ID associated with your project, and choose a [supported region](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations).

In order to keep private, sensitive information and secrets out of your source code repositories, it is recommended to use either Environment Variables, User Secrets, or a Key/Secrets Manager to retrieve data like an API key.

Here, I'm going to create an `.env` file and place it into the project folder with the following content.

```
GOOGLE_PROJECT_ID=<your project ID>
GOOGLE_REGION=us-central1
```

To access the value of a variable that is defined in a `.env` file, use `$dotenv`. More details are described under [Environment Variables](https://learn.microsoft.com/en-us/aspnet/core/test/http-files?view=aspnetcore-8.0#environment-variables) in the official documentation.

Set the file properties with a Build action of `None` and copy instructions of `Copy, if newer`.

```
<None Update=".env" Condition="Exists('.env')">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
</None>
```

## Install the SDK / NuGet package

The SDK for .NET for the Gemini API is contained in the `Mscc.GenerativeAI` package. Install the dependency using dotnet CLI:

```
dotnet add package Mscc.GenerativeAI
```

See [README](https://www.nuget.org/packages/Mscc.GenerativeAI/) for alternative options, like the NuGet Package Manager.

**Note:** *This is a quickstart to Gemini on Vertex AI. If you need additional authentication options see [README](https://www.nuget.org/packages/Mscc.GenerativeAI/) of Mscc.GenerativeAI and consider to add the package reference [Mscc.GenerativeAI.Google](https://www.nuget.org/packages/Mscc.GenerativeAI.Google/) which is based on the [.NET Cloud Client Libraries](https://cloud.google.com/dotnet/docs/reference).*

## Initialize the Generative Model

Before you can make any API calls, you need to add a reference to the namespace `Mscc.GenerativeAI` and initialize the Generative Model.

```
using Mscc.GenerativeAI;

var vertexAI = new VertexAI(
    projectId: Environment.GetEnvironmentVariable("GOOGLE_PROJECT_ID"), 
    region: Environment.GetEnvironmentVariable("GOOGLE_REGION"));
var model = vertexAI.GenerativeModel(model: Model.Gemini10Pro);
```

The necessary access token to authenticate against Google Cloud is retrieved from the Application Default Credentials or the Google Client Library, in case that you are using the Mscc.GenerativeAI.Google package.

## Generate Text

```
var prompt = "Write a poem about Japanese koi.";
var responseStream = model.GenerateContentStream(prompt);

// Use StringBuilder to append the streamed responses
await foreach (var response in responseStream)
{
    var response = await model.GenerateContent();
    // optional, check for response.Candidates[0].FinishReason
    Console.WriteLine(response.Text);
}
```

**Note:** *The package Mscc.GenerativeAI offers a unified developer experience across Google AI and Vertex AI provided by the interface IGenerativeAI. Meaning, the non-streaming method* `GenerateContent` *is available in Vertex AI and works as expected.*

## What's next

Explore the [README](https://www.nuget.org/packages/Mscc.GenerativeAI/) of the NuGet package which has more samples documented. All unit tests are accessible in the [GitHub repository](https://github.com/mscraftsman/generative-ai):

[GitHub - mscraftsman/generative-ai: Gemini AI Client for .NETGemini AI Client for .NET. Contribute to mscraftsman/generative-ai development by creating an account on GitHub.![](https://github.githubassets.com/favicons/favicon.svg)GitHubmscraftsman![](../content/images/2024/04/generative-ai.webp)](../content/images/2024/04/generative-ai.webp)

If you're new to generative AI models, you might want to look at the [concepts guide](https://ai.google.dev/docs/concepts) and the [Gemini API overview](https://ai.google.dev/docs/gemini_api_overview) before trying a quickstart.

## What's the difference from Google AI Gemini API

The Vertex AI Gemini API and Google AI Gemini API both let you incorporate the capabilities of Gemini models into your applications. The platform that's right for you depends on your goals.

The Vertex AI Gemini API is designed for developers and enterprises for use in scaled deployments. It offers features such as enterprise security, data residency, performance, and technical support. If you're an existing Google Cloud customer or deploy medium to large scale applications, you're in the right place.

If you're a hobbyist, student, or developer who is new to Google Cloud, try the [Google AI Gemini API](xref:quickstart-use-gemini-with-net), which is suitable for experimentation, prototyping, and small deployments. If you're looking for a way to use Gemini directly from your mobile and web apps, see the Google AI SDKs for Android, Swift, and web.

<small>Image credit: Gemini using prompt <em>Create an image showing the fast start of a race in motor sport.</em></small>