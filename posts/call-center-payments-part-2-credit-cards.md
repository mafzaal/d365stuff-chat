---
title: Call Center Payments Part 2 - Credit Cards
date: 2019-08-15T00:03:39.000Z
lastmod: 2019-08-16T01:01:49.000Z
description: Part 1 was a simple example of how to add a cash payment to a call center order.
 Here, we&#x27;ll explore how to add a credit card payment to the order.  The
functional overview is:

 1. Create a payment (MCRCustPaymTable)
 2. Select a credit card [token] to use (CreditCardCust)
 3. Update payment with the credit card information 

Depending on situational context, there may or may not be a need to generate a
credit card token through code.  If the token already exists, the process is
just like part
tags: x++, Payments, D365, Call center, AX, Dynamics, Retail, Sales orders
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

14 August 2019 / [x++](/tag/x/)

# Call Center Payments Part 2 - Credit Cards

Part 1 was a simple example of how to add a cash payment to a call center
order. Here, we'll explore how to add a credit card payment to the order. The
functional overview is:

  1. Create a payment (MCRCustPaymTable)
  2. Select a credit card [token] to use (CreditCardCust)
  3. Update payment with the credit card information 

Depending on situational context, there may or may not be a need to generate a
credit card token through code. If the token already exists, the process is
just like part 1 of the series with an extra table relation. The steps can
also be streamlined into one or two parts, but [again] it's contextual.

    
    
    using Retail=Microsoft.Dynamics.Retail;
    using RetailConst=Microsoft.Dynamics.Retail.PaymentSDK.Portable.Constants;
    using Microsoft.Dynamics.Commerce.Runtime.Services.CustomerOrder;
    class paymentExample
    {
        static mcrCustPaymTable createCallCenterPaymentRecord()
        {
    
            MCRCustPaymTable mcrCustPaymTable;
            SalesTable					salesTable = SalesTable::find('SalesId'); 
    
            try
            {
                ttsbegin;
                mcrCustPaymTable.clear();
                mcrCustPaymTable.Channel        = salesTable.retailSalesTable().RetailChannel;
                mcrCustPaymTable.CurrencyCode   = 'USD';
                mcrCustPaymTable.TenderTypeId   = 'CreditCard';
                mcrCustPaymTable.RefTableId     = salesTable.TableId;
                mcrCustPaymTable.RefRecId       = salesTable.RecId;
                mcrCustPaymTable.CustAccount    = salesTable.CustAccount;
                mcrCustPaymTable.CardTypeId     = 'Visa';
                mcrCustPaymTable.Status         = MCRCustPaymStatus::NotSubmitted;
                mcrCustPaymTable.CustPaymType   = MCRCustPaymTable::getMCRTypeFromTender( mcrCustPaymTable.TenderTypeId,
                                                                                      mcrCustPaymTable.Channel);
    
                switch (_mcrCustPaymStatus)
                {
                    case MCRCustPaymStatus::NotSubmitted:
                    case MCRCustPaymStatus::Authorized:
    
                        mcrCustPaymTable.Amount = CurrencyExchange::round(10, 'USD');
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
    
        static void AddCreditCardToPayment()
        {
            MCRCustPaymTable    mcrCustPaymTable = paymentexample::createCallCenterPaymentRecord();
            
            CreditCardCust      creditCardCust = CreditCardCust::findByUniqueCardId('MyFavoriteCard');
    
            //update payment with credit card info
            mcrCustPaymTable.selectForUpdate();
            mcrCustPaymTable.PaymInfoTableId = creditCardCust.TableId;
            mcrCustPaymTable.PaymInfoRecId = creditCardCust.RecId;
            mcrCustPaymTable.update();
    
        }
    }

Creating the MCRCustPaymTable record is very similar to creating one for a
cash payment, however now it's important to specify the card type (eg Visa,
AMEX), and the tender type is different (Credit Card vs Cash) as well. These
values can vary from system to system, so as always, don't hardcode them.

The above example is very presumptuous about finding and using an existing
credit card. What if a card doesn't exist, and a token needs to be created on
the fly? If so, the steps change to:

  1. Create a payment (MCRCustPaymTable)
  2. Create a credit card [token] to use (CreditCardCust)
  3. Update payment with the credit card information 

That's a lot harder.

Tokens are stored in giant hard-to-read arrays (especially when using SQL) on
the CreditCardCust table. This format allows for a dynamic collection of token
attributes to be stored, which could change in the future without needing to
change the table schema. As of right now, the following are in there:

  * ServiceAccountId (a unique GUID per instance)
  * ConnectorName
  * Alias
  * CardType (eg Visa)
  * CardToken (the token value representing a credit card)
  * Last4Digits
  * UniqueCardid (a GUID)
  * ExpirationYear (4 digit integer year, eg 2019)
  * ExpirationMonth (2 digit integer month, eg 11)
  * Customerid (shopper reference)
  * Name (eg Bill Gates)
  * BankIdentificationNumberStart (BIN, optional backup in case the credit card processor doesn't understand what [eg] Visa means)
  * CardVerificationValue
  * ShowSameAsShippingAddress
  * House 
  * StreetAddress
  * City
  * State
  * PostalCode
  * Country
  * CardVerificationValue

All of the above fields are crammed into CreditCardCust.CardToken. Once that's
handled, the rest is straight forward.

    
    
    using Retail=Microsoft.Dynamics.Retail;
    using RetailConst=Microsoft.Dynamics.Retail.PaymentSDK.Portable.Constants;
    using Microsoft.Dynamics.Commerce.Runtime.Services.CustomerOrder;
    class paymentExample
    {
        static mcrCustPaymTable createCallCenterPaymentRecord()
        {
    
            MCRCustPaymTable mcrCustPaymTable;
            SalesTable					salesTable = SalesTable::find('SalesId'); 
    
            try
            {
                ttsbegin;
                mcrCustPaymTable.clear();
                mcrCustPaymTable.Channel        = salesTable.retailSalesTable().RetailChannel;
                mcrCustPaymTable.CurrencyCode   = 'USD';
                mcrCustPaymTable.TenderTypeId   = 'CreditCard';
                mcrCustPaymTable.RefTableId     = salesTable.TableId;
                mcrCustPaymTable.RefRecId       = salesTable.RecId;
                mcrCustPaymTable.CustAccount    = salesTable.CustAccount;
                mcrCustPaymTable.CardTypeId     = 'Visa';
                mcrCustPaymTable.Status         = MCRCustPaymStatus::NotSubmitted;
                mcrCustPaymTable.CustPaymType   = MCRCustPaymTable::getMCRTypeFromTender( mcrCustPaymTable.TenderTypeId,
                                                                                      mcrCustPaymTable.Channel);
    
                switch (_mcrCustPaymStatus)
                {
                    case MCRCustPaymStatus::NotSubmitted:
                    case MCRCustPaymStatus::Authorized:
    
                        mcrCustPaymTable.Amount = CurrencyExchange::round(10, 'USD');
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
    
        static void AddCreditCardToPayment()
        {
            MCRCustPaymTable    mcrCustPaymTable = paymentexample::createCallCenterPaymentRecord();
    
    		//instead of finding a token, this call will create a new token
    		CreditCardCust      creditCardCust = paymentexample::createToken();
    
    		//update payment with credit card info
    		ttsbegin;
    		mcrCustPaymTable.selectForUpdate();
    		mcrCustPaymTable.PaymInfoTableId = creditCardCust.TableId;
    		mcrCustPaymTable.PaymInfoRecId = creditCardCust.RecId;
    		mcrCustPaymTable.update();
    		ttscommit;
    
        }
    	
    	static CreditCardCust createToken()
        {
            CustTable         custTable = custTable::find('BillGates');
            CreditCardCust    creditCardCust;
    		
    		str uniqueCardId = guid2Str(newGuid());
    
            CreditCardPaymentCardTokenize   cardTokenize;
            CreditCardProcessors 			activeCreditCardProcessors;
            activeCreditCardProcessors 		= CreditCardProcessors::findActiveProcessor();
    
    		cardTokenize = CreditCardPaymentCardTokenize::construct();
    		cardTokenize.parmCustAccount(custTable.AccountNum);
    		cardTokenize.init(activeCreditCardProcessors.Name);
    
    		var cardPaymentProperties  = CreditCardPaymentProperties::construct();
    		var processorProperties = CreditCardPaymentProperties::fromProperties(cardTokenize.parmprocessorProperties());  
    		cardPaymentProperties.add(processorProperties.find('MerchantAccount', 'ServiceAccountId'));
    		
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('Connector', 'ConnectorName', 'Your favorite connector'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue(RetailConst.GenericNamespace::get_PaymentCard(), 'Alias', 'ccAlias'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue(RetailConst.GenericNamespace::get_PaymentCard(), 'CardType', 'Visa'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue(RetailConst.GenericNamespace::get_PaymentCard(), 'AdyenPaymentMethod', 'Visa'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue(RetailConst.GenericNamespace::get_PaymentCard(), 'CardToken', '0123456789'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue(RetailConst.GenericNamespace::get_PaymentCard(), 'Last4Digits', '1234'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue(RetailConst.GenericNamespace::get_PaymentCard(), 'UniqueCardId', uniqueCardId));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue(RetailConst.GenericNamespace::get_PaymentCard(), 'ExpirationYear', 2020));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue(RetailConst.GenericNamespace::get_PaymentCard(), 'ExpirationMonth', 10));
    
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('CommerceIdentification', 'CustomerId', 'ShopperRef'));
    
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'Name', 'Bill Gates'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'BankIdentificationNumberStart', '123456'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'ShowSameAsShippingAddress', 'False'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'House', 'N/A'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'StreetAddress', '1 Microsoft Way'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'City', 'Redmond'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'State', 'WA'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'PostalCode', '98052'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'Country', 'USA'));
    		cardPaymentProperties.add(CreditCardPaymentProperty::newValue('PaymentCard', 'CardVerificationValue', 'SUCCESS')); 
    
    		cardTokenize.parmpaymentCardProperties(cardPaymentProperties.toArray());
    		
    		creditCardCust.clear();
    		creditCardCust.CardNumber = '1234';//use last 4 digits
    		creditCardCust.CustAccount = custTable.AccountNum;
    		creditCardCust.CreditCardProcessors = activeCreditCardProcessors.RecId;
    		creditCardCust.CreditCardTypeName = 'Visa';
    		creditCardCust.ExpiryDate = '10/2020';//I know... a str field called date
    		creditCardCust.UniqueCardId = uniqueCardId;//
    		creditCardCust.Name = custTable.name();
    		creditCardCust.CardToken = cardTokenize.getXmlString();
    		creditCardCust.Notes = 'This could be your first token!!!';
    
    		creditCardCust.insert();
        }
    }

And the above is very presumptuous about procuring a token. But that's another
problem to solve.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

