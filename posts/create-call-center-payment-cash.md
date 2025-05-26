---
title: Call Center Payments Part 1 - Cash
date: 2019-07-23T15:00:42.000Z
lastmod: 2019-08-06T16:32:25.000Z
description: Creating call center payments via x++ is a challenging and increasingly common
task that every architect needs to know.  It&#x27;s a reasonable client request to
integrate or create payments, and it&#x27;s something that needs to work perfectly,
and often at a high velocity and scale.  There&#x27;s a lot to cover and I don&#x27;t want
anyone to read more than they have to, so the series will first cover the whole
process as simply as possible, with a cash payment, and then get into more
complicated methods of payme
tags: x++, Sales orders, Dynamics, D365, Payments
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

23 July 2019 / [x++](/tag/x/)

# Call Center Payments Part 1 - Cash

Creating call center payments via x++ is a challenging and increasingly common
task that every architect needs to know. It's a reasonable client request to
integrate or create payments, and it's something that needs to work perfectly,
and often at a high velocity and scale. There's a lot to cover and I don't
want anyone to read more than they have to, so the series will first cover the
whole process as simply as possible, with a cash payment, and then get into
more complicated methods of payment like credit cards, and implications around
order completion and invoicing.

The functional overview is:

  1. Create a sales order, header and lines - Assuming this is already accomplished
  2. Create a payment record (MCRCustPaymTable) per payment. This is the final step for cash payments 
  3. Associate each payment record with ancillary payment information (eg gift card, credit card)

After payments are created, the order will need to be completed (MCREndOrder
class) and ultimately invoiced.

The MCRCustPaymTable is the linchpin to the entire process. It's many to one
relationship with the sales order means enables customers to pay with multiple
methods of payment on one order. It could be cash and a credit card; two
different credit cards; a gift card, credit card, and cash – there are
unlimited possibilities.

![](https://www.d365stuff.co/content/images/2019/07/image.png)

Cash payments are the simplest because an entire cash payment entry is
contained on the MCRCustPaymTable record, whereas credit and gift cards have
to be fleshed out in other tables, and then referenced back using table and
rec ids.

Here is an example of how to add a single cash payment to a sales order,
inspired by the RetailTransactionPaymentsHelper class:

    
    
    static mcrCustPaymTable createCallCenterPaymentRecord()
    {
    
        MCRCustPaymTable mcrCustPaymTable;
    
        SalesTable					salesTable = SalesTable::find('SalesId');
        CurrencyCode				currency = 'USD';
        str							paymentType = 'Cash';
        real						amount = 10;
        MCRCustPaymStatus			mcrCustPaymStatus = MCRCustPaymStatus::NotSubmitted;
    
        try
        {
            ttsbegin;
            mcrCustPaymTable.clear();
            mcrCustPaymTable.Channel        = salesTable.retailSalesTable().RetailChannel;
            mcrCustPaymTable.CurrencyCode   = currency;
            mcrCustPaymTable.TenderTypeId   = paymentType;
            mcrCustPaymTable.RefTableId     = salesTable.TableId;
            mcrCustPaymTable.RefRecId       = salesTable.RecId;
            mcrCustPaymTable.CustAccount    = salesTable.CustAccount;
            mcrCustPaymTable.Status         = mcrCustPaymStatus;
            mcrCustPaymTable.CustPaymType   = MCRCustPaymTable::getMCRTypeFromTender( mcrCustPaymTable.TenderTypeId,
                                                                                      mcrCustPaymTable.Channel);
    
            switch (_mcrCustPaymStatus)
            {
                case MCRCustPaymStatus::NotSubmitted:
                case MCRCustPaymStatus::Authorized:
    
                    mcrCustPaymTable.Amount = CurrencyExchange::round(amount, _currency);
                    break;                              
            }
    
            mcrCustPaymTable.insert();
    
            ttscommit;
        }
        catch
        {
            RetailTracer::Error('RetailTransactionPaymentsHelper', funcName(), strFmt('Error during Call Center payment (MCRCustPaymTable) creation:\nSalesId [$%1]\n', _salesTable.RecId));
        }
    
    	return mcrCustPaymTable;
    }
    

That's it! Cash is one of the few payments that doesn't require an extra table
and relation. Although fleshing out credit cards, gift cards, and installments
require additional tables and information, the design pattern for them will be
the same.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

