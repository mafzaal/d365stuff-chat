---
title: JSON ODATA for people that miss AIF
date: 2019-04-16T20:51:46.000Z
lastmod: 2019-04-17T17:43:26.000Z
description: One of the seemingly scariest changes moving to D365 a few years ago [when it
was still AX7] was the loss of the constant in our lives that was AIF.  AIF was
the crux of EDI – it handled inbound and outbound messages, had innate
transactional scope at the message level regardless of complexity, and at the
end of the day you just felt good and secure seeing a tangible [XML] file in a
folder that you could, run, rerun, and archive.

The other nice thing about AIF and XML documents is that you don&#x27;
tags: Tips Tricks, ODATA, D365, AX, DMF, Data Entity, AIF
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

16 April 2019 / [Tips Tricks](/tag/tips-tricks/)

# JSON ODATA for people that miss AIF

One of the seemingly scariest changes moving to D365 a few years ago [when it
was still AX7] was the loss of the constant in our lives that was AIF. AIF was
the crux of EDI – it handled inbound and outbound messages, had innate
transactional scope at the message level regardless of complexity, and at the
end of the day you just felt good and secure seeing a tangible [XML] file in a
folder that you could, run, rerun, and archive.

The other nice thing about AIF and XML documents is that you don't have to
have a technical background to manage and understand them. A formatted XML
document is very easy to read and the message history and error log was
readily accessible in AX. Since catapulting to the cloud, every project I go
on yields the same questions from AIF gurus of old, "What's a JSON?" "What
does ODATA even mean?"

First, JSON means JavaScript Object Notation; the only thing you really need
to get from that is that it's a format for writing stuff (in this case
objects, such as sales order numbers, SKUs, amounts, etc). At the end of the
day, JSON is your new XML. What used to read like this:

![](https://www.d365stuff.co/content/images/2019/04/image-1.png)

Now potentially reads like this:

![](https://www.d365stuff.co/content/images/2019/04/image-2.png)

Second, ODATA is short for Open Data Protocol. If that doesn't mean anything
to you, you might go down the Google rabbit hole of "What's REST?" "What's
SOAP?" What's important to understand is that ODATA is used by a ton of humans
(ie people you want to integrate with) and it supports JSON. In an AIF-less
world, ODATA is a mechanism for your EDI partner to [eg] get your customers'
orders [$$$] in your system.

Even though ODATA and JSON aren't new to the world at large, the way they are
implemented in D365 is still special. Users [you] can use ODATA to query D365
data and get results in a JSON format from the convenience a web browser. In
my opinion, learning to master, or even fumble through this, is essential in
an environment where you don't have SQL access. You can visualize data at
large, get record counts, and get empathy for your integration partners by
seeing what they see.

Step one: Change the your environment URL to end with the word data instead of
company id and menu object. This will reveal a list of all the data entities
available to you.

![](https://www.d365stuff.co/content/images/2019/04/image-3.png)

Step Two. If you know what you're looking for, append the entity name to your
URL, otherwise hit CTRL + F and search stuff. Let's say you loaded a giant
movement journal and are asking yourself, "Is DMF doing anything? Is anything
happening or is the system just spinning?" Search for movement, and look for
something meaningful. You can always tie this back to a data project you made
as well.

![](https://www.d365stuff.co/content/images/2019/04/image-4.png)

Step three. Copy and paste the name into your url after data. This is case
sensitive! In this example,
[https://D365Stuff.sandbox.operations.dynamics.com/data](https://d365stuff.dynamics.com/data/InventoryMovementJournalEntries?ref=d365stuff.co)
becomes
[https://D365Stuff.sandbox.operations.dynamics.com/data/InventoryMovementJournalEntries](https://d365stuff.dynamics.com/data/InventoryMovementJournalEntries?ref=d365stuff.co)

Step four. Add filters. To get the record count, you can add count to the end
of the URL. If you aren't sure whether that data project spinning or not,
refreshing this will tell you if the record count is increasing (aka actually
doing something).

![](https://www.d365stuff.co/content/images/2019/04/image-7.png)

Bonus step. Add a filter to your count. You can have multiple filters and
operators at the same time! Here is an example to check a record count
(growing or not) for a specific journal:

[https://D365Stuff.sandbox.operations.dynamics.com/data/InventoryMovementJournalEntries/$count?$filter=JournalNumber
eq
'000001'](https://d365stuff.sandbox.operations.dynamics.com/data/InventoryMovementJournalEntries/$count?%24filter=JournalNumber+eq+%27000001%27&ref=d365stuff.co)

![](https://www.d365stuff.co/content/images/2019/04/image-6.png)

The possibilities are endless. You can do cross company queries, sorts, and
various operators. The best resource for more details is
[here](https://docs.microsoft.com/en-us/dynamics365/unified-operations/dev-
itpro/data-entities/odata?ref=d365stuff.co), but you can apply almost anything
you read about ODATA outside of Microsoft Docs to your D365 instance.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

