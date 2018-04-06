# PicoCTF 2017 - Level 1 - Raw2Hex

**Category:** Reverse Engineering **Points:** 20

**Description:**

> This program just prints a flag in raw form. All we need to do is convert the output 
> to hex and we have it! CLI yourself to /problems/963285fb64e4c5f7a31b5a601c704f99 
> and turn that Raw2Hex!

We need to get the hexadecimal representation of the flag. Running the program shows us
a message with the flag and some characters are unreadable. Using xxd we can get a hexdump
of the output.

```
$ ./raw2hex | xxd                                                                               
0000000: 5468 6520 666c 6167 2069 733a e519 e7aa  The flag is:....                       
0000010: 7e59 3fde 891b d24a aa42 3ea4            ~Y?....J.B>.
```     

We can see that the last 4 bytes of the first line are the beginning of the flag. Taking
this along with the next line produces our flag.

Flag: e519e7aa7e593fde891bd24aaa423ea4
