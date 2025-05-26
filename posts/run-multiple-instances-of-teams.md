---
title: Run Multiple Instances of Teams
date: 2020-05-07T17:41:44.000Z
lastmod: 2020-05-07T17:41:44.000Z
description: I never thought I&#x27;d get this (in their words) &quot;hack&quot; from a supply chain
consultant, but apparently anything is possible in 2020.  Here is a great way to
run multiple desktop Teams clients at the same time.

Copy and paste the following into a text editor:

@ECHO OFF

REM Uses the file name as the profile name
SET MSTEAMS_PROFILE&#x3D;%~n0
ECHO - Using profile &quot;%MSTEAMS_PROFILE%&quot;

SET &quot;OLD_USERPROFILE&#x3D;%USERPROFILE%&quot;
SET &quot;USERPROFILE&#x3D;%LOCALAPPDATA%\Microsoft\Teams\CustomProfiles\%MSTEAMS_PROFILE%&quot;

EC
tags: Tips Tricks
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

7 May 2020 / [Tips Tricks](/tag/tips-tricks/)

# Run Multiple Instances of Teams

I never thought I'd get this (in their words) "hack" from a supply chain
consultant, but apparently anything is possible in 2020. Here is a great way
to run multiple desktop Teams clients at the same time.

Copy and paste the following into a text editor:

    
    
    @ECHO OFF
    
    REM Uses the file name as the profile name
    SET MSTEAMS_PROFILE=%~n0
    ECHO - Using profile "%MSTEAMS_PROFILE%"
    
    SET "OLD_USERPROFILE=%USERPROFILE%"
    SET "USERPROFILE=%LOCALAPPDATA%\Microsoft\Teams\CustomProfiles\%MSTEAMS_PROFILE%"
    
    ECHO - Launching MS Teams with profile %MSTEAMS_PROFILE%
    cd "%OLD_USERPROFILE%\AppData\Local\Microsoft\Teams"
    "%OLD_USERPROFILE%\AppData\Local\Microsoft\Teams\Update.exe" --processStart "Teams.exe"
    

Name the file whatever you want, and give it a .cmd extension.

![](https://www.d365stuff.co/content/images/2020/05/image.png)

Now with a mere double click, I can have two desktop Teams clients open, at
the same time. In this example, I have my work account open and a guest
account open for a customer:

![](https://www.d365stuff.co/content/images/2020/05/image-1.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

