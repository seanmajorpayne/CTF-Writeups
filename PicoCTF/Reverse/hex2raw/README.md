# PicoCTF 2017 - Level 1 - Hex2Raw

**Category:** Reverse Engineering **Points:** 20

**Description:**

> This program requires some unprintable characters as input... But how do you print 
> unprintable characters? CLI yourself to /problems/c69bcda4ca5a28fd9d18790fc763db73 
> and turn that Hex2Raw!

Running the program with ./hex2raw, it asks us to give it a long string of hexadecimal
characters, some of which are not printable. Looking at the man page for echo, we can
see that using the -e option will allow us to feed it hex values which it will then
interpret. We can pipe this into the program to get our flag.

```
$ echo -ne "\x41\x6f\x1c\x79\x18\xf8\x3a\x4f\x19\x22\
xd8\x6d\xf5\xe7\x83\x48" | ./hex2raw                      
Give me this in raw form (0x41 -> 'A'):                   
416f1c7918f83a4f1922d86df5e78348                          
                                                          
You gave me:                                              
416f1c7918f83a4f1922d86df5e78348                          
Yay! That's what I wanted! Here be the flag:              
1d2411efe307f5ac07bd28bbabb5769e 
```

