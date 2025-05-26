---
title: LedgerDimensionFacade is the new DimensionDefaultingService
date: 2019-02-04T20:26:52.000Z
lastmod: 2019-02-04T20:26:52.000Z
description: This is more of a reminder for me than you that the DimensionDefaultingService
class doesn&#x27;t exist in D365.  The DimensionDefaultingService was a short-lived
class; brought into existence for only one version of AX.  Its legacy lives on
now in the LedgerDimensionFacade, where we can [most importantly] call the
serviceCreateLedgerDimension() method to combine the RecId values of a
LedgerDimension and up to four DefaultDimensions.  Of course it has a lot more
to offer, but you&#x27;ll have to look at t
tags: x++, D365, defaultDimension, LedgerDimension
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

4 February 2019 / [x++](/tag/x/)

# LedgerDimensionFacade is the new DimensionDefaultingService

This is more of a reminder for me than you that the DimensionDefaultingService
class doesn't exist in D365. The DimensionDefaultingService was a short-lived
class; brought into existence for only one version of AX. Its legacy lives on
now in the LedgerDimensionFacade, where we can [most importantly] call the
serviceCreateLedgerDimension() method to combine the RecId values of a
LedgerDimension and up to four DefaultDimensions. Of course it has a lot more
to offer, but you'll have to look at the class code for that.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

