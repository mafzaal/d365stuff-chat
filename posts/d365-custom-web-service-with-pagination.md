---
title: D365 Custom JSON Web Service with Pagination
date: 2023-02-10T23:00:30.000Z
lastmod: 2023-02-10T23:00:24.000Z
description: I got a request for a RESTful API with Pagination; here is my proof of concept:

There are a few keys to this:

 * A queryRun object must be used (vs SELECT statement) in order to use enablePositionPaging
 * The query MUST have a sort on it

Without using queryRun, you would have to do some hacky stuff with x++ SQL that would not be performant.  And that still may not work.

Without a sort, you will get the error &quot;An exception occured when invoking the operation - Paging is not supported for que
tags: D365, Data contracts, Integrations, Logic Apps, Serialization, Snippet, Web services, x++
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

10 February 2023 / [D365](/tag/d365/)

# D365 Custom JSON Web Service with Pagination

I got a request for a RESTful API with Pagination; here is my proof of
concept:

![](https://www.d365stuff.co/content/images/2023/02/image.png)

There are a few keys to this:

  * A queryRun object must be used (vs SELECT statement) in order to use enablePositionPaging
  * The query MUST have a sort on it

Without using queryRun, you would have to do some hacky stuff with x++ SQL
that would not be performant. And that still may not work.

Without a sort, you will get the error "An exception occured when invoking the
operation - Paging is not supported for queries that do not have an ordering
property."

    
    
    class testPagingCustomers
    {
        public str getCustomers(int64 _startPosition, int64 _pageSize, boolean _includeTotalCount)
        {
            str json;
            Query query;
            QueryRun queryRun;
    
            query = new Query();
            QueryBuildDataSource qbd = query.addDataSource(tableNum(CustTable));
            qbd.addSortField(fieldNum(CustTable, AccountNum), SortOrder::Ascending);
    
            // Set up paging
            queryRun = new QueryRun(query);
            queryRun.enablePositionPaging(true);
            queryRun.addPageRange(_startPosition, _pageSize);
            
            List customers = new List(Types::Class);
    
            while (queryRun.next())
            {
                CustTable custTable = queryRun.get(tableNum(CustTable));
                testCustomersLinesContract testCustomersLinesContract = new testCustomersLinesContract();
    
                testCustomersLinesContract.parmAccountNum(CustTable.AccountNum);
                testCustomersLinesContract.parmCustGroup(custTable.CustGroup);
                testCustomersLinesContract.parmCustName(custTable.name());
    
                customers.addEnd(testCustomersLinesContract);
            }
    
            testCustomersContract testCustomersContract = new testCustomersContract();
            testCustomersContract.parmCustomers(customers);
    
            if (_includeTotalCount)
            {
                testCustomersContract.parmTotalCount(SysQuery::countLoops(queryRun));
            }
    
            json =  FormJsonSerializer::serializeClass(testCustomersContract);
    
            return json;
    
        }
    
    }

To test or implement the class, assign it to a service and service group in
D365. Once deployed, you should be able to navigate in a browser to verify:

![](https://www.d365stuff.co/content/images/2023/02/image-1.png)

Then use the verified URI to make a POST request:

![](https://www.d365stuff.co/content/images/2023/02/image-2.png)

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

