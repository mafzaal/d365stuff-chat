---
title: Trace Batch Jobs and more via CMD Logman
date: 2019-11-21T21:28:57.000Z
lastmod: 2019-11-21T21:28:57.000Z
description: Tracing and debugging interactive user sessions is one thing, but how do you
trace a batch job in a tier two SAT environment?  Here&#x27;s a high level how:

 1.  If the environment has multiple AOSes, assign the batch job to a batch
    group that only contains one server
 2. RDP into the server from [1]
 3. Create a provider file for Logman to run against 
 4. Open CMD as Administrator and start the trace
 5. End the trace

A provider file is a file listing multiple Event Trace providers to enable.
tags: D365, Performance, Trace, sql, Trace parser
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

21 November 2019 / [D365](/tag/d365/)

# Trace Batch Jobs and more via CMD Logman

Tracing and debugging interactive user sessions is one thing, but how do you
trace a batch job in a tier two SAT environment? Here's a high level how:

  1. If the environment has multiple AOSes, assign the batch job to a batch group that only contains one server
  2. RDP into the server from [1]
  3. Create a provider file for Logman to run against 
  4. Open CMD as Administrator and start the trace
  5. End the trace

A provider file is a file listing multiple Event Trace providers to enable.
The file should be a text file containing one provider per line. When we start
the trace, we will pass the txt file location as a parameter. For D365 traces,
it should look like:

![](https://www.d365stuff.co/content/images/2019/11/image-2.png)

Here is an example of the CMD commands to run the actual trace. As soon as the
start command completes, the ETL will be created in the file, where you can
watch it grow in real time. If you're running multiple traces, be sure to name
the output etl file something new each time. The -pf parameter is how we tell
the trace to use the provider file we made earlier. In this case, I also
specify for the trace file to have a 4GB cap and stop the trace. There is a
stop command to explicitly stop the trace as well.

![](https://www.d365stuff.co/content/images/2019/11/CMD-Screenshot.JPG)

Once the ETL is generated, it can be imported into Trace Parser just like any
other.

![](https://www.d365stuff.co/content/images/2019/11/image-3.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

