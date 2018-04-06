# PicoCTF 2017 - Level 1 - What is Web

**Category:** Web Exploitation **Points:** 20

**Description:**

> Someone told me that some guy came up with the "World Wide Web", using "HTML" and 
> "stuff". Can you help me figure out what that is? Website.

This problem is very simple and focused on understanding where files are located and how
to view source code for various components of a website. Right-click on the web page
and click "View Source" (or "Inspect") and take a look at the source code. There is
one part of the flag located in the HTML as a commment

```
<!-- Cool! Look at me! This is an HTML file. It describes what each page contains in a format your browser can understand. -->
<!-- The first part of the flag (there are 3 parts) is 8d96c7d8966 -->
<!-- What other types of files are there in a webpage? -->
```

Looking around, we'll find a couple of other files listed in the source code including
hacker.css and script.js. Adding these to our URL we can find the other parts of the flag.

```
/*
This is the css file. It contains information on how to graphically display
the page. It is in a seperate file so that multiple pages can all use the same 
one. This allows them all to be updated by changing just this one.
The second part of the flag is 8106eabacc0 
*/

/* This is a javascript file. It contains code that runs locally in your
 * browser, although it has spread to a large number of other uses.
 *
 * The final part of the flag is 3b680682297
 */
```

