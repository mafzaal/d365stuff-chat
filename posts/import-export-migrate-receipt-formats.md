---
title: Import Export Migrate Retail Receipt Formats
date: 2019-02-08T23:32:18.000Z
lastmod: 2019-02-08T23:32:18.000Z
description: How to migrate D365 Retail Receipts from one environment to another
tags: Retail, Receipt Designer, DMF, Retail receipt, D365, Tips Tricks
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

8 February 2019 / [Retail](/tag/retail/)

# Import Export Migrate Retail Receipt Formats

This is a super fun task. After all the hard work you spent in the archaic AF
designer, moving your work from one environment to another should be easy. It
can be easy, but it can also cause you to throw your laptop out the window if
you aren't precise in your steps.

You've probably gotten the "Value cannot be null" error message, or been
warned your XML is too long and is about to be truncated. It's ok. Just be
sure to do the following:

  1. Use the "XML-Attribute" format on your data entity. You'll be sorry if you don't.
  2. Ignore any warnings you get. 
  3. Get your sequence right: Receipt Format >> Receipt Profile >> Receipt Profile Line
  4. Relax.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

