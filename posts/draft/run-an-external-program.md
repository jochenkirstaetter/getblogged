---
uid: run-an-external-program
title: Run an external program (Draft)
date: 2024-02-29
status: draft
type: post
description: // usage const string ToolFileName = "example.exe"; string output = RunExternalExe(ToolFileName);
tags: []
keywords: ''
metaTitle: Run an external program
metaDescription: // usage const string ToolFileName = "example.exe"; string output = RunExternalExe(ToolFileName);
image: ''
ogTitle: Run an external program
ogDescription: // usage const string ToolFileName = "example.exe"; string output = RunExternalExe(ToolFileName);
layout: post
bodyClass: post-template
postClass: post
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
canonicalUrl: https://jochen.kirstaetter.name/run-an-external-program/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: ''
updatedAt: 2024-02-29T08:38:05Z
excerpt: // usage const string ToolFileName = "example.exe"; string output = RunExternalExe(ToolFileName);
twitterTitle: Run an external program
twitterDescription: // usage const string ToolFileName = "example.exe"; string output = RunExternalExe(ToolFileName);
twitterImage: 
facebookTitle: Run an external program
facebookDescription: // usage const string ToolFileName = "example.exe"; string output = RunExternalExe(ToolFileName);
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
```cs
// usage
const string ToolFileName = "example.exe";
string output = RunExternalExe(ToolFileName);

public string RunExternalExe(string filename, string arguments = null)
{
    var process = new Process();

    process.StartInfo.FileName = filename;
    if (!string.IsNullOrEmpty(arguments))
    {
        process.StartInfo.Arguments = arguments;
    }

    process.StartInfo.CreateNoWindow = true;
    process.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
    process.StartInfo.UseShellExecute = false;

    process.StartInfo.RedirectStandardError = true;
    process.StartInfo.RedirectStandardOutput = true;
    var stdOutput = new StringBuilder();
    process.OutputDataReceived += (sender, args) => stdOutput.AppendLine(args.Data); // Use AppendLine rather than Append since args.Data is one line of output, not including the newline character.

    string stdError = null;
    try
    {
        process.Start();
        process.BeginOutputReadLine();
        stdError = process.StandardError.ReadToEnd();
        process.WaitForExit();
    }
    catch (Exception e)
    {
        throw new Exception("OS error while executing " + Format(filename, arguments)+ ": " + e.Message, e);
    }

    if (process.ExitCode == 0)
    {
        return stdOutput.ToString();
    }
    else
    {
        var message = new StringBuilder();

        if (!string.IsNullOrEmpty(stdError))
        {
            message.AppendLine(stdError);
        }

        if (stdOutput.Length != 0)
        {
            message.AppendLine("Std output:");
            message.AppendLine(stdOutput.ToString());
        }

        throw new Exception(Format(filename, arguments) + " finished with exit code = " + process.ExitCode + ": " + message);
    }
}

private string Format(string filename, string arguments)
{
    return "'" + filename + 
        ((string.IsNullOrEmpty(arguments)) ? string.Empty : " " + arguments) +
        "'";
}
```

Source: [https://stackoverflow.com/a/10072082](https://stackoverflow.com/a/10072082)