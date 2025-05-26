---
title: x++ AADAuthentication to get D365 Tenant Id
date: 2022-07-28T13:58:51.000Z
lastmod: 2022-07-28T13:58:51.000Z
description: x++ to get D365 FO tenant id
tags: D365, x++
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

28 July 2022 / [D365](/tag/d365/)

# x++ AADAuthentication to get D365 Tenant Id

Hi. Someone asked me the other day how they could determine the environment's
tenant using x++, and here it is. There's a few other fields in the mix, but
aadResponse.TenantId in the code below is what you're looking for:

    
    
    using Microsoft.Dynamics.AX.Security.MicrosoftGraphHelper;
    
    class Class1
    {
        static void main (Args args)
        {
            boolean status = false;
            str exMessage, failureMessage, response, tenant, s2sCertThumbprint, stackTrace;       
        
            // Try to authenticate to AAD
            var aadResponse = AADAuthentication::AuthenticateWithAADByCertificate();
            status = aadResponse.Status;
            tenant = aadResponse.TenantId;
            response = aadResponse.Response;
            s2sCertThumbprint = aadResponse.S2SCertThumbprint;
            stackTrace = aadResponse.StackTrace;
    
        }
    
    }

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

