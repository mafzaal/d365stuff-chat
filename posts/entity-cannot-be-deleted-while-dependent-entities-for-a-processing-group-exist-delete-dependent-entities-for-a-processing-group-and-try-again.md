---
title: Entity cannot be deleted while dependent Entities for a processing group exist. Delete dependent Entities for a processing group and try again.
date: 2019-02-27T22:22:29.000Z
lastmod: 2019-02-27T22:22:29.000Z
description: Entity cannot be deleted while dependent Entities for a processing group exist. Delete dependent Entities for a processing group and try again.
tags: Tips Tricks, D365, DMF, Errors
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

27 February 2019 / [Tips Tricks](/tag/tips-tricks/)

# Entity cannot be deleted while dependent Entities for a processing group
exist. Delete dependent Entities for a processing group and try again.

Sometimes, you need to delete a data entity from the data entity master.
Sometimes, that's a pain to do because it's referenced in a data project, and
you have to delete that reference before you can delete the master data.
Sometimes, you have hundreds of data projects to go through, and it sucks a
lot.

You can always use table browser, lookup the DMFDefinitionGroupEntity table,
and filter on the entity you're trying to delete to find the data projects to
resolve.

![](https://www.d365stuff.co/content/images/2019/02/image-1.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

