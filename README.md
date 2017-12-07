# XenScrape
This is a module I developed to scrape Xenforo boards.

There are 4 different methods one can invoke on this module.

The first thing one would want to do is create a new instance of a Xenforo scraper. 
The way to do that would be as follows:

Example = Xen(url)

Next, once an instance of Xen scraper is created you can invoke the following methods.

Example.retrieve();

This method must always be invoked first after you create the Xenforo scraper class. This method is the one that accesses the website and grabs all the relevant data.

The next three methods all take in 2 arguments. The first argument is an empty object, the second argument is a string.

These methods are as follows:

Example.messageCount(obj, name);
Example.discussionCount(obj, name);
Example.memberCount(obj, name);
