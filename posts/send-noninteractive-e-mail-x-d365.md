---
title: Send NonInteractive E-mail x++ D365
date: 2019-04-02T23:47:51.000Z
lastmod: 2019-04-02T23:47:51.000Z
description: There are a lot of posts out there about how to send e-mails in Dynamics.  It&#x27;s
something we&#x27;ve all been doing for years, but a lot of us could be doing it
better.  Most of the material I see out there uses the SysMailerSMTP class,
which means committing to a protocol that was first devised in 1982.  It also
implies committing to a protocol that may not be the same as what was configured
in your D365 system. 

There&#x27;s a system parameter that dictates the E-mail provider used by batch
classes.  I
tags: x++, D365, E-mail, Integrations
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

2 April 2019 / [x++](/tag/x/)

# Send NonInteractive E-mail x++ D365

There are a lot of posts out there about how to send e-mails in Dynamics. It's
something we've all been doing for years, but a lot of us could be doing it
better. Most of the material I see out there uses the SysMailerSMTP class,
which means committing to a protocol that was first devised in 1982. It also
implies committing to a protocol that may not be the same as what was
configured in your D365 system.

There's a system parameter that dictates the E-mail provider used by batch
classes. I think it's a good practice to use that. Since it's 2019 (or later
because I don't know when you're reading this), you probably shouldn't be
using SMTP at all in a production environment, but I don't know your life. The
overall key is using the SysMailerFactory::getNonInteractiveMailer() method;
this will always keep your code synced with your system configuration.

![](https://www.d365stuff.co/content/images/2019/04/image.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

