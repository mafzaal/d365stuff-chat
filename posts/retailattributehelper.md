---
title: RetailAttributeHelper
date: 2018-11-13T05:21:09.000Z
lastmod: 2019-07-12T15:10:57.000Z
description: Retail sales order attributes are a great way to add properties to orders, at
the header or line level, in an omni-channel solution since they are easily
viewable from the POS as well as D365 client.  Unfortunately, the magic behind
these attributes is super fussy.  Fortunately, there&#x27;s the RetailAttributeHelper
class.

Go ahead, read the code behind the
createOrUpdateRetailSalesOrderAttributeValues(); it&#x27;s super fussy inside.
 Calling it to create or update a collection of retail sales attribut
tags: x++, Retail Attributes, Sales orders, D365
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

12 November 2018 / [x++](/tag/x/)

# RetailAttributeHelper

Retail sales order attributes are a great way to add properties to orders, at
the header or line level, in an omni-channel solution since they are easily
viewable from the POS as well as D365 client. Unfortunately, the magic behind
these attributes is super fussy. Fortunately, there's the
RetailAttributeHelper class.

Go ahead, read the code behind the
createOrUpdateRetailSalesOrderAttributeValues(); it's super fussy inside.
Calling it to create or update a collection of retail sales attributes, not so
much.

You "need" your channel RecId, logical store Id, terminal Id, and transaction
Id.

After that you need need your sales order number, company context, a 0
[header] or line number, and then a list object of attributes. It could look
something like this:

![](https://www.d365stuff.co/content/images/2018/11/image-9.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

