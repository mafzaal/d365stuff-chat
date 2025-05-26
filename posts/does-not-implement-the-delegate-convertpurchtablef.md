---
title: ... does not implement the delegate &#x27;convertPurchTableFieldToVendInvoiceDelegate&#x27;
date: 2020-12-22T18:54:43.000Z
lastmod: 2020-12-23T00:43:46.000Z
description: This is a fun surprise that can take a bit of digging.  When adding fields to
the PurchTable table&#x27;s HeaderToLineUpdate field group, this error can pop up if
they aren&#x27;t accounted for in the convertPurchTableFieldToVendInvoice delegate,
which is part of the VendInvoiceTableToLineUpdate class which copies PO fields
to the invoice.

The first step in subscribing is to find the class&#x27; delegate in the Designer and
copy the event handler method:

Next, paste that method into a new class:

d365StuffCl
tags: D365, Errors, x++, Delegates
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

22 December 2020 / [D365](/tag/d365/)

# ... does not implement the delegate
'convertPurchTableFieldToVendInvoiceDelegate'

This is a fun surprise that can take a bit of digging. When adding fields to
the PurchTable table's HeaderToLineUpdate field group, this error can pop up
if they aren't accounted for in the convertPurchTableFieldToVendInvoice
delegate, which is part of the VendInvoiceTableToLineUpdate class which copies
PO fields to the invoice.

The first step in subscribing is to find the class' delegate in the Designer
and copy the event handler method:

![](https://www.d365stuff.co/content/images/2020/12/image.png)

Next, paste that method into a new class:

    
    
    d365StuffClass
    {
    	[SubscribesTo(classStr(VendInvoiceTableToLineUpdate), staticDelegateStr(VendInvoiceTableToLineUpdate, convertPurchTableFieldToVendInvoiceDelegate))]
    	public static void VendInvoiceTableToLineUpdate_convertPurchTableFieldToVendInvoiceDelegate(FieldId _purchTableFieldId, EventHandlerResult _result)
    	{
    		switch(_purchTableFieldId)
    		{
    			case fieldNum(PurchTable, DlvMode):
    				_result.result(0);
    							break;
    		}
    	}
    }

In this example, I'm adding a condition for the DlvMode field. I don't want it
to copy to the invoice, so I'm setting the result to 0.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

