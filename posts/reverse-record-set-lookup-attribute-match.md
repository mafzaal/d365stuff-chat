---
title: Reverse Record Unique Set Lookup Attribute Match
date: 2022-10-04T14:26:09.000Z
lastmod: 2022-10-04T14:50:09.000Z
description: Is there a word or term for this?  The other day someone asked me for help on a
problem, &quot;I&#x27;ve got an integration where I receive somewhere between 0 - 10 tax
codes and need to figure out what [unique] tax group they all belong to.&quot;

To solve, we&#x27;re going to use the Contoso DB.  Here is a look at the TaxGroupData
table:

Let&#x27;s look at the CA group; it has three codes, HR_CAST, RP_CAST, and SP_CAST.
 The problem with doing a search on just these values, is that not only do I get
the CA group back
tags: sql, D365, TaxGroupData
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

4 October 2022 / [sql](/tag/sql/)

# Reverse Record Unique Set Lookup Attribute Match

Is there a word or term for this? The other day someone asked me for help on a
problem, "I've got an integration where I receive somewhere between 0 - 10 tax
codes and need to figure out what [unique] tax group they all belong to."

To solve, we're going to use the Contoso DB. Here is a look at the
TaxGroupData table:

![](https://www.d365stuff.co/content/images/2022/10/image.png)

Let's look at the CA group; it has three codes, HR_CAST, RP_CAST, and SP_CAST.
The problem with doing a search on just these values, is that not only do I
get the CA group back, but also CALA and CALA-USE, which have those codes
within their [larger] sets:

![](https://www.d365stuff.co/content/images/2022/10/image-3.png)

The key to solve the problem is not just to match on the tax codes
[attributes], but the count of them in a set. I say attributes because I
consider that to be what it really is at the most abstract level, and have
done a similar pattern for advanced product configurators.

To get the number of lines in a set at the line level, I join the table to a
SQL expression (which could easily be a view in x++) on [the header] TaxGroup:

![](https://www.d365stuff.co/content/images/2022/10/image-5.png)![](https://www.d365stuff.co/content/images/2022/10/image-4.png)

Now we know how many attributes or lines are in each set. The CA tax group has
3 lines, HR_CAST, RP_CAST, SP_CAST whereas the CALA group has 6: HR_CAST,
HR_LACITY, RP_CAST, RP_LACITY, SP_CAST, SP_LACITY.

Now when I search on the three codes, I can see the three groups that set is
in, but I can also tell that two of those have larger sets with additional
attributes:

![](https://www.d365stuff.co/content/images/2022/10/image-6.png)

We only want the taxgroup that has a perfect circle Venn diagram with the
supplied tax codes, so we need to also filter on count of tax codes:

![](https://www.d365stuff.co/content/images/2022/10/image-7.png)

This essentially gets us there. From here, there are many options on how where
to take this depending on the context of the call or how it will be used. For
demo ease, here is a the final query with a top 1:

![](https://www.d365stuff.co/content/images/2022/10/image-8.png)

That's it! This can all be reproduced in x++ in a number of ways. The best way
will be up to you.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

