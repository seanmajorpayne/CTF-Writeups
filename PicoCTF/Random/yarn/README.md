# PicoCTF 2017 - Level 2 - Yarn

**Category:** Random **Points:** 55

**Description:**

> I was told to use the linux strings command on yarn, but it doesn't work. Can you help? 
> I lost the flag in the binary somewhere, and would like it back

For this problem, we are given a binary file called Yarn. Running strings on this file
will indeed return various strings, but nothing that resembles a flag. Looking at the
hints we see that Strings has a criteria for what it considers to be a string, looking at
the man page we see:

```
$ man strings
-min-len
-n min-len
--bytes=min-len
Print sequences of characters that are at least min-len characters long, instead of the default 4.
$ strings -n 1 yarn
Sub
mit
_me
_fo
r_I
_am
_th
e_f
lag
```

In the output, we will now find the flag in character sets of 3.

Submit_me_for_I_am_the_flag