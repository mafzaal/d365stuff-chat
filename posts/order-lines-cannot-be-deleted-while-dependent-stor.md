---
title: Order lines cannot be deleted while dependent Stores ... exist
date: 2019-12-04T17:37:44.000Z
lastmod: 2019-12-04T17:37:44.000Z
description: This is a frustrating bug that can happen in between DOM runs.  The reason is
there is a [bad] join between the SalesLine and DOMSalesLineToProcess tables,
based solely on DlvMode.  Until resolved, the work around is to delete
DOMSalesLineToProcess records with the same DlvMode as the SalesLine record that
needs to be deleted.
tags: Bugs
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

4 December 2019 / [Bugs](/tag/bugs/)

# Order lines cannot be deleted while dependent Stores ... exist

This is a frustrating bug that can happen in between DOM runs. The reason is
there is a [bad] join between the SalesLine and DOMSalesLineToProcess tables,
based solely on DlvMode. Until resolved, the work around is to delete
DOMSalesLineToProcess records with the same DlvMode as the SalesLine record
that needs to be deleted.

![](https://www.d365stuff.co/content/images/2019/12/image.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

