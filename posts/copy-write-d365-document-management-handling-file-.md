---
title: Copy Write D365 Document Management Handling File to wherever via Logic Apps
date: 2022-12-20T16:39:00.000Z
lastmod: 2022-12-20T20:58:15.000Z
description: Because why not?

Problem: How do I get this lost raccoon from a D365 attachment to another part
of the cloud?

Spoiler: You&#x27;re going to DB partnerFirst, we need to create a custom web service
that can fetch our friend:

    public FileDataString getStuff()
    {

        DocuRef docuRef;
        FileDataString FileDataString &#x3D; &#x27;&#x27;;

        select firstonly docuRef where docuRef.Name &#x3D;&#x3D; &#x27;RaccoonPardner&#x27;;

        if(docuRef)
        {
            container data &#x3D;
            	DocumentManagement:
tags: D365, Document Handling, Document Management, Integrations, Logic Apps, POST, Stuff, Web services, x++
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

20 December 2022 / [D365](/tag/d365/)

# Copy Write D365 Document Management Handling File to wherever via Logic Apps

Because why not?

Problem: How do I get this lost raccoon from a D365 attachment to another part
of the cloud?

![](https://www.d365stuff.co/content/images/2022/12/image.png)Spoiler: You're
going to DB partner

First, we need to create a custom web service that can fetch our friend:

    
    
        public FileDataString getStuff()
        {
    
            DocuRef docuRef;
            FileDataString FileDataString = '';
    
            select firstonly docuRef where docuRef.Name == 'RaccoonPardner';
    
            if(docuRef)
            {
                container data =
                	DocumentManagement::getAttachmentAsContainer(docuRef);
                if (data && conLen(data) > 0)
                {
                    BinData binData = new BinData();
                    binData.setData(data);
                    FileDataString = binData.base64Encode();
                }
            }
            return FileDataString;
    
        }

Second, we need a logic app to call the service:

![](https://www.d365stuff.co/content/images/2022/12/image-9.png)

Here is the code view to better show the expression in File Content. The key
method I use is base64ToBinary().

![](https://www.d365stuff.co/content/images/2022/12/image-2.png)

And there it is:

![](https://www.d365stuff.co/content/images/2022/12/image-3.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

