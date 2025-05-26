---
title: How to DROP a table in D365
date: 2019-02-19T23:58:13.000Z
lastmod: 2019-02-19T23:58:13.000Z
description: TL;DR: In D365, use SP_RemoveTable instead of DROP
tags: D365, sql, t-sql, DROP, SQLDictionary, Database Synchronization
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

19 February 2019 / [D365](/tag/d365/)

# D365 DROP Table SP_RemoveTable

TL;DR: In D365, use SP_RemoveTable instead of DROP.

Every now and then, whether it's your fault or not, a table is going to get
FUBAR in your DEV environment. The rest of the world will keep spinning, and
no one will care about the catastrophic problem that only you have.

One of the cool things about AX has always been if you delete files, or drop a
table, a simple AOS restart will bring them back. You need to be a little
extra careful in D365. Recently I got an ISV update that caused my DB sych to
break, ultimately because it was trying to add new the same fields to the
SQLDictionary twice, causing a unique index violation. A great problem for one
person to have.

If you don't care about the data in the table, a nice old fashioned SQL DROP
can get you halfway to "fixing" a DB synch – however it's very possible that
your table won't be recreated on your next DB synch. A DB synch will never
complete if the environment has missing [deleted] objects while references to
those objects still exist in the SQLDictionary. Herein lies the golden nugget
of the story, SP_RemoveTable. SP_RemoveTable is a great, safe way to remove
all of a table's references from the SQLDictionary table. Next time you're
ready to crush some tables, use SP_RemoveTable.

![](https://www.d365stuff.co/content/images/2019/02/image.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

