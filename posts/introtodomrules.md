---
title: Intro to DOM rules
date: 2019-12-17T23:00:00.000Z
lastmod: 2019-12-21T16:17:45.000Z
description: There&#x27;s a new sheriff in town making all sorts of rules around order
fulfillment, and it goes by the name DOM [Distributed Order Management]
[https://docs.microsoft.com/en-us/dynamics365/retail/dom].  DOM is a massive new
retail feature in D365 that everyone will be implementing, so it&#x27;s important to
understand DOM rules and its table structure.

Per Microsoft [https://docs.microsoft.com/en-us/dynamics365/retail/dom], the DOM
rule types are:

 * Minimum Inventory rule * This rule type lets organ
tags: DOM, D365, sql, Retail
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

17 December 2019 / [DOM](/tag/dom/)

# Intro to DOM rules

There's a new sheriff in town making all sorts of rules around order
fulfillment, and it goes by the name [DOM [Distributed Order
Management]](https://docs.microsoft.com/en-
us/dynamics365/retail/dom?ref=d365stuff.co). DOM is a massive new retail
feature in D365 that everyone will be implementing, so it's important to
understand DOM rules and its table structure.

Per [Microsoft](https://docs.microsoft.com/en-
us/dynamics365/retail/dom?ref=d365stuff.co), the DOM rule types are:

  * Minimum Inventory rule 
    * This rule type lets organizations "ring fence" a specific quantity of a product for purposes other than order fulfillment. For example, organizations might not want DOM to consider all the inventory that is available in a store for order fulfillment. Instead, they might want to reserve some inventory for walk-in customers. When this rule type is used, you can define the minimum inventory to keep for a category of products, an individual product, or a product variant per location or group of locations.
  * Fulfillment location Priority Rule 
    * This rule type lets organizations define a hierarchy of locations to establish the priority that the DOM engine considers when it tries to identify fulfillment locations for specific products. The valid range of priorities is 1 through 10, where 1 is the highest priority and 10 is the lowest priority. Locations that have higher priority are considered before locations that have lower priority. If the rule is defined as a hard constraint rule, orders are brokered only to locations that priorities are defined for.
  * Maximum rejects rule 
    * This rule lets organizations define a threshold for rejections. When the threshold is reached, the DOM processor will mark an order or order line as an exception, and exclude it from further processing.
  * Maximum orders rule 
    * This rule lets organizations define the maximum number of orders that a location or group of locations can process during a calendar day. If the maximum number of orders is assigned to a location in a single day, DOM won't assign any more orders to that location for the rest of that calendar day.
  * Maximum distance rule 
    * This rule lets organizations define the maximum distance that a location or group of locations can be to fulfill the order. If overlapping maximum distance rules are defined for a location, DOM will apply the lowest maximum distance that is defined for that location.
  * Offline fulfillment location rule 
    * This rule lets organizations specify a location or group of locations as offline or unavailable to DOM, so that orders can't be assigned to those locations for fulfillment.
  * Partial orders rule 
    * This rule lets organizations define whether an order or order lines can be partially fulfilled.

DOM rules have a classic header and line table pattern, with table inheritance
mixed in. DOMRules is the abstract table that represents the rule header, and
DOMRulesLine is the abstract table that represents the rule lines. Since
DOMRules and DOMRulesLine are abstract, records cannot be directly inserted in
them via x++. It's very important to determine the type of rule being made
before starting development, since it impacts the tables to declare.

Here is what the table hierarchy looks like:

![](https://www.d365stuff.co/content/images/2019/12/DOMRules-5.jpg)

The Name field [alone] is the unique index on the table; it is also used to
join to the line level data of the DOM rule; naming DOM rules well is very
important. None of the children tables can be selected in SQL, only [the
abstract] DOMRules can, however only the children tables can be inserted into
via x++ due to table inheritance.

DOMCatalogRules is probably the most technically unique instance, because it
is the only DOMRules child table that is [also] an abstract table. In order to
make a 'catalog' rule, data must be inserted into
DOMCatalogMinimumInventoryRules or DOMCatalogShipPriorityRules. This is also
the only instance that has [RecId] relationships to D365 master product data.

The line level data uses the same pattern and hierarchy. There is an abstract
table, DOMRulesLine, and a child table for each type of rule:

![](https://www.d365stuff.co/content/images/2019/12/DOMRulesLine-1.jpg)

The unique index for DOM rule line data is DOMRulesName and LineNum. The line
level data joins on DOMRulesName to the header's Name field.

Creating DOM rules through code, or creating a data entity can seem daunting,
but with proper planning, organization, and understanding of the table
hierarchies and relations, it can be a little less difficult.

Happy DOMing!

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

