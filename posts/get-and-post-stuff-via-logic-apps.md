---
title: GET and POST Stuff via Logic Apps
date: 2020-07-01T23:00:00.000Z
lastmod: 2020-07-15T22:51:57.000Z
description: Sometimes you need to get stuff in and out of D365; Logic Apps help with this a
lot.  Here are some simple examples of GETs and POSTs that call D365 exposed web
services, data entities, and metadata services.

GET REST Metadata Service 
The basic Logic App pattern is to:

 1. Execute on a schedule
 2. Perform an HTTP GET on a D365 Metadata service
 3. Put the results in a file in a Dropbox folder

The most important thing to get right is the HTTP Method.  Metadata services are
read only, and GET
tags: Logic Apps, D365, Data Entity, JSON, Integrations, ODATA, POST, Web services
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

1 July 2020 / [Logic Apps](/tag/logic-apps/)

# GET and POST Stuff via Logic Apps

Sometimes you need to get stuff in and out of D365; Logic Apps help with this
a lot. Here are some simple examples of GETs and POSTs that call D365 exposed
web services, data entities, and metadata services.

### GET REST Metadata Service

The basic Logic App pattern is to:

  1. Execute on a schedule
  2. Perform an HTTP GET on a D365 Metadata service
  3. Put the results in a file in a Dropbox folder

![](https://www.d365stuff.co/content/images/2020/07/GetMetaDataServiceCreateFile.JPG)

The most important thing to get right is the HTTP Method. Metadata services
are read only, and GET must be used.

![](https://www.d365stuff.co/content/images/2020/07/GetMetaDataService.JPG)

Once the Logic App is executed, an enormous file of Data Entities is made in
Dropbox. Here is what part of it looks like:

![](https://www.d365stuff.co/content/images/2020/07/MetadataEntitiesJSON.JPG)

### POST Exposed Web Services

Any x++ class can be exposed as a web service with service and service group
objects. For this example, I found an OOB class, AvailabilityService, that can
retrieve the availability for various services with a ping test. If you
explore the class, you can check out possible values to pass in the
MonitoringAndDiagnostics macro.

![](https://www.d365stuff.co/content/images/2020/07/getAvailabilityClass.JPG)

We'll use a pattern similar to what we used for the metadata service, however
we'll POST instead of GET:

  1. Execute on a schedule
  2. Perform an HTTP POST on a D365 service endpoint
  3. Put the results in a file in a Dropbox folder

For the POST, all of the parameters for the method are passed in the body in a
JSON format. I figured out the test values by looking at the aforementioned
Macro.

![](https://www.d365stuff.co/content/images/2020/07/POSTAvailabilityServiceParameters1Redacted.JPG)

Once it's run, test results appear in Dropbox. Not the best result this time,
but the Logic App worked!

![](https://www.d365stuff.co/content/images/2020/07/AvailabilityServiceOutput.JPG)

### POST Data Entity Endpoint

This example has a bonus step that the others don't, getting contents from a
file.

![](https://www.d365stuff.co/content/images/2020/07/image-1.png)

The Logic App pattern is:

  1. Execute on a schedule
  2. Get the content of a file on Dropbox
  3. Use file content to perform an HTTP POST on a D365 data entity endpoint
  4. Put the [success] results in a file in a Dropbox folder

![](https://www.d365stuff.co/content/images/2020/07/image-6.png)

The trickiest part is creating the URI to POST to, and it's very sensitive.
Here is the breakdown of the import (enqueue) API:

https://<base URL>/api/connector/enqueue/<activity ID>?entity=<entity name>

Here is an example from [Microsoft ](https://docs.microsoft.com/en-
us/dynamics365/fin-ops-core/dev-itpro/data-entities/recurring-
integrations?ref=d365stuff.co#integration-rest-apis)using the Customer Groups
data entity:

[https://usncax1aos.cloud.onebox.dynamics.com/en/api/connector/enqueue/%7B6D31E09F-0249-459F-94F0-AAD9C2C47B64%7D?entity=Customer%20Groups](https://usncax1aos.cloud.onebox.dynamics.com/en/api/connector/enqueue/%7B6D31E09F-0249-459F-94F0-AAD9C2C47B64%7D?entity=Customer+Groups&ref=d365stuff.co)

Company [dataAreaId] can be added at the end via &. Spaces in entity names
must be handled with %20. If this is wrong, the data entity message status
will be stuck "in process" forever.

Having problems? A great place to debug the import method of the
DMFIntegrationBridge class. There you'll be able to see the file imported, and
also see how the entity name is matched (or not) based on the URI.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

