---
title: DMF JumpRef
date: 2018-11-16T05:57:16.000Z
lastmod: 2018-12-07T16:07:10.000Z
description: No matter who you are, if you&#x27;re working with D365 you&#x27;re working with DMF.  You
will inevitably have data problems and be trying to review your staging data in
the visualizer, however that form can&#x27;t be called from code just like any other
form.  Here are the three keys behind calling the form properly.

 1. Get the name right.  The form object name is DMFDataVizualization.  With a
    z.
 2.  Don&#x27;t use the DMFDataVizualization display menu item and pass args its way.
     You will get an error
tags: x++, D365, AX, DMF, DMFFormBrowser
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

15 November 2018 / [x++](/tag/x/)

# DMF JumpRef

No matter who you are, if you're working with D365 you're working with DMF.
You will inevitably have data problems and be trying to review your staging
data in the visualizer, however that form can't be called from code just like
any other form. Here are the three keys behind calling the form properly.

  1. Get the name right. The form object name is DMFDataVizualization. With a z.
  2. **Don't** use the DMFDataVizualization display menu item and pass args its way. You will get an error because of the form's init code: 

![](https://www.d365stuff.co/content/images/2018/11/image-2.png)

3\. Use the DMFFormBrowser class:

![](https://www.d365stuff.co/content/images/2018/11/image-5.png)

In short:

![](https://www.d365stuff.co/content/images/2018/11/image-8.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

