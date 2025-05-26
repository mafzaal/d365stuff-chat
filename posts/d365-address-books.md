---
title: D365 Address Books
date: 2018-11-08T06:08:13.000Z
lastmod: 2018-11-08T06:08:13.000Z
description: Address books are pretty much everywhere there&#x27;s a party in D365.  Customers
have address books, stores have address books, workers have address books –
they&#x27;re all over the place.  Even though it&#x27;s a seemingly simple drop down in
the UI, they can be a pain to update or migrate if you&#x27;re not familiar with what
is going on behind the scenes, DirAddressBookParty.  The table is a collection
of party RecIds and address book RecIds, which allows each party to host
multiple address books in this M:M t
tags: D365, x++, Address Book, DirAddressBookParty
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

8 November 2018 / [D365](/tag/d365/)

# D365 Address Books

Address books are pretty much everywhere there's a party in D365. Customers
have address books, stores have address books, workers have address books –
they're all over the place. Even though it's a seemingly simple drop down in
the UI, they can be a pain to update or migrate if you're not familiar with
what is going on behind the scenes, DirAddressBookParty. The table is a
collection of party RecIds and address book RecIds, which allows each party to
host multiple address books in this M:M table.

The solution to populating and managing the table lies within itself, its
static methods createPartyRelations() and createPartyRelationsByName()
(however the latter works by calling the former).

To see it in action, let's investigate Microsoft's own code in the
RetailTransactionServiceCustomer class:

1)Build a container object with the address book RecIds that you want

2)Call the createPartyRelations method with that container and the RecId of
the party you are adding them to.

![](https://www.d365stuff.co/content/images/2018/11/image-1.png)

The best part about using this method is that it will check if the address
book is already associated with the party to help you avoid unique index
violations. And is there really anything better than avoiding unique index
violations? They suck.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

