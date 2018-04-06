# PicoCTF 2017 - Level 1 - Leaf of the Forest

**Category:** Random **Points:** 30

**Description:**

> We found an even bigger directory tree hiding a flag starting at 
> /problems/3a36b3b0858a593882b7d6a0dc5bd2f9. It would be impossible to find the file 
> named flag manually...

This is very similar to Leaf of the Tree, except we now have way to many files to go
through. Even running find will flood the console, so we need to pipe the output into
grep. This gives us our flag.

```
$ find . -type f | grep flag
./forest/tree275809/trunkd439/trunk6e5b/trunk9e17/trunk5e55/trunk4ef
f/trunk1b9b/trunk4c82/branch73cf/flag
$ cat ./forest/tree275809/trunkd439/trunk6e5b/trunk9e17/trunk5e55/trunk4ef
f/trunk1b9b/trunk4c82/branch73cf/flag
6c0d4a69fdff4ea12609fd1989749dd5
```