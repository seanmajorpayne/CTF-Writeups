# PicoCTF 2017 - Level 1 - Internet Kitties

**Category:** Random **Points:** 10

**Description:**

> A program at /problems/ab718be873f8a7efe966f4ed5af749eb has access to a flag but 
> refuses to share it. Can you convince it otherwise?

This is a very simple problem. It's introducing us to netcat. One command will get us
the flag.

```
$ nc shell2017.picoctf.com 12275
Yay! You made it!
Take a flag!
1e1ccf22b278d35b1977c76bb66c5e30
```