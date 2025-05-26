---
title: DMFUtil DMFDownloadDataPackage Stuff
date: 2018-12-12T18:24:00.000Z
lastmod: 2018-12-12T18:24:00.000Z
description: The DMFUtil class is a great code collection to be aware of in case you ever
find yourself trying to kick off DMF import/exports via x++, or are just curious
about how some of that entity stuff works.

The setupNewExecution method is the most convenient and succinct way you can
create a new execution to kick off.  First, all you need is the string name of
your definition group, which could have been created manually or through code.
 Next, the ExecutionId is generated (and ultimately returned) v
tags: x++, DMF, DMFUtil, DMFDownloadDataPackage, D365
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

12 December 2018 / [x++](/tag/x/)

# DMFUtil DMFDownloadDataPackage Stuff

The DMFUtil class is a great code collection to be aware of in case you ever
find yourself trying to kick off DMF import/exports via x++, or are just
curious about how some of that entity stuff works.

The setupNewExecution method is the most convenient and succinct way you can
create a new execution to kick off. First, all you need is the string name of
your definition group, which could have been created manually or through code.
Next, the ExecutionId is generated (and ultimately returned) via the mother of
all ExecutionIds (you should check out the generateExecutionId method as
well).

![](https://www.d365stuff.co/content/images/2018/12/image-2.png)

The DMFDefinitionGroupExecution::InsertOrDisplay method is the super helpful
finale. If you peek in there, you'll see a lot of fussy work being done for
you. Once you get your own DMFDefinitionGroupExecution record, you can do
pretty much any DMF-related thing you want. My favorite use-case is calling
the DMFDownloadDataPackage class to create a downloadable package:

![](https://www.d365stuff.co/content/images/2018/12/image-3.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

