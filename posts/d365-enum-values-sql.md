---
title: D365 Enum Values SQL
date: 2020-02-21T16:56:17.000Z
lastmod: 2020-02-21T16:56:17.000Z
description: With every AX release it seems the way enumeration values are stored and
referenced changes.  Thanks to my good friend Muhammad
[https://twitter.com/afzaal_qau], we now have a great SQL query to look these up
in D365.  Here is an example for SalesType:

select t1.NAME,t2.ENUMID,t2.ENUMVALUE,t2.NAME EnumValueName from ENUMIDTABLE t1
inner join ENUMVALUETABLE t2 on t1.ID&#x3D;t2.ENUMID
where t1.NAME&#x3D;&#x27;SalesType&#x27;
tags: sql, D365, Enumerations, t-sql
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

21 February 2020 / [sql](/tag/sql/)

# D365 Enum Values SQL

With every AX release it seems the way enumeration values are stored and
referenced changes. Thanks to my good friend
[Muhammad](https://twitter.com/afzaal_qau?ref=d365stuff.co), we now have a
great SQL query to look these up in D365. Here is an example for SalesType:

    
    
    select t1.NAME,t2.ENUMID,t2.ENUMVALUE,t2.NAME EnumValueName from ENUMIDTABLE t1
    inner join ENUMVALUETABLE t2 on t1.ID=t2.ENUMID
    where t1.NAME='SalesType'

![](https://www.d365stuff.co/content/images/2020/02/image.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

