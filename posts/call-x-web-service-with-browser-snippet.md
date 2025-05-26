---
title: Call x++ web service with web browser snippet
date: 2019-05-23T01:37:05.000Z
lastmod: 2019-05-23T05:58:04.000Z
description: There are a lot of ways to call D365 web services – Postman, Fiddler, Logic Apps
– but they&#x27;re all a bit fussy.  Getting authentication right the first time can
be stressful, and they all require additional downloads, accounts, or
subscriptions.

You can run snippets of JavaScript on any page
[https://developers.google.com/web/tools/chrome-devtools/javascript/snippets] 
with Chrome.  Javascript can make JSON POST requests, and fortunately for us,
&quot;any page&quot; includes the D365 default dashboard ho
tags: Integrations, x++, JSON, Snippet, D365, Data contracts, Web services, Javascript
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

22 May 2019 / [Integrations](/tag/integrations/)

# Call x++ web service with web browser snippet

There are a lot of ways to call D365 web services – Postman, Fiddler, Logic
Apps – but they're all a bit fussy. Getting authentication right the first
time can be stressful, and they all require additional downloads, accounts, or
subscriptions.

You can [run snippets of JavaScript on any
page](https://developers.google.com/web/tools/chrome-
devtools/javascript/snippets?ref=d365stuff.co) with Chrome. Javascript can
make JSON POST requests, and fortunately for us, "any page" includes the D365
default dashboard homepage.

Here is a quick example project I made. It's a simple x++ class with a few
test methods. One is a simple Hello World, and the other, HelloParameter, will
take 2 parameters, integers, and return the sum of them with a friendly
message.

![](https://www.d365stuff.co/content/images/2019/05/HelloWorld-Project-
Screenshot-1.JPG)

You can already call a service without parameters simply through URL
navigation, so the real value is being able to pass parameters. To call the
service's HelloParameter method, we can write a quick snippet in Chrome (F12
shortcut).

![](https://www.d365stuff.co/content/images/2019/05/Snippet-Screenshot.JPG)

The snippet sets two parameters, integers with values 1 and 4 respectively. A
POST request is made, and it returns a sum of 5.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

