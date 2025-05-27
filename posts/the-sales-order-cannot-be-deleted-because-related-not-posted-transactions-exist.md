---
title: The sales order cannot be deleted because related not posted transactions exist
date: 2019-05-14T05:23:37.000Z
lastmod: 2019-05-19T19:53:20.000Z
description: Breaking up with sales orders can be hard to do.  You try your best to make
invoicing work, but eventually you cut your losses and to part ways.  Or at
least try to.  &quot;The sales order cannot be deleted because related not posted
transactions exist&quot; error can appear for a variety of reasons; sometimes those
reasons make sense, and sometimes they&#x27;re confusing.

The least common, and rarely thought of reason for this error is because there
are existing invoice history records (ie invoicing demons) 
tags: Tips Tricks, D365, Errors
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

14 May 2019 / [Tips Tricks](/tag/tips-tricks/)

# The sales order cannot be deleted because related not posted transactions
exist

Breaking up with sales orders can be hard to do. You try your best to make
invoicing work, but eventually you cut your losses and to part ways. Or at
least try to. "The sales order cannot be deleted because related not posted
transactions exist" error can appear for a variety of reasons; sometimes those
reasons make sense, and sometimes they're confusing.

The least common, and rarely thought of reason for this error is because there
are existing invoice history records (ie invoicing demons) related to the
order. This is why even if you delete every order line (SalesLine), the error
still comes up when you try to delete the empty header (SalesTable). In lower
tier environments, it's easy to delete the SalesParmTable and SalesParmLine
table records with a job or script, however in a production environment you
have to brush up on your navigation skills.

Accounts receivable > Inquiries and reports > Invoices > Invoice history is
your path to healing. Here you can filter on your order, delete the invoicing
history, and move on with your life.

![](https://www.d365stuff.co/content/images/2019/05/image.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

