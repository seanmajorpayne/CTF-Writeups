# PicoCTF 2017 - Level 1 - Hash101

**Category:** Cryptography **Points:** 50

**Description:**

> Prove your knowledge of hashes and claim a flag as your prize! 
> Connect to the service at shell2017.picoctf.com:46122

This problem focuses on hash cracking. There are four levels in total, each of which
gets slightly harder (although still easy). Most of these answers can be obtained using
converters online (and since this is timed, you probably need to do this to be efficient).

The third level wants you to take a string who's decimal equivalent leaves the specified
remainder after a modulus operation. This is easiest to do by inputting one random ASCII
character. When the server tells you what the remainder is for that character, just adjust
it the appropriate # of characters away.

The last problem will have you visiting a few md5 hash cracking websites until you can
find the cracked hash.

```
$ nc shell2017.picoctf.com 46122

Welcome to Hashes 101!

There are 4 Levels. Complete all and receive a prize!


-------- LEVEL 1: Text = just 1's and 0's --------
All text can be represented by numbers. To see how different letters translate to numbers, go to http://www.asciitable.com/

TO UNLOCK NEXT LEVEL, give me the ASCII representation of 0110100001100101011011000110110001101111

> hello

------ LEVEL 2: Numbers can be base ANYTHING -----
Numbers can be represented many ways. A popular way to represent computer data is in base 16 or 'hex' since it lines up with bytes very well (2 hex characters = 8 binary bits). Other formats include base64, binary, and just regular base10 (decimal)! In a way, that ascii chart represents a system where all text can be seen as "base128" (not including the Extended ASCII codes)

TO UNLOCK NEXT LEVEL, give me the text you just decoded, hello, as its hex equivalent, and then the decimal equivalent of that hex number ("foo" -> 666f6f -> 6713199)

hex>68656c6c6f0a
68656c6c6f0a to ASCII -> hello
 is not hello
hex>68656c6c6f
Good job! 68656c6c6f to ASCII -> hello is hello
Now decimal
dec>10410110810811
10410110810811 to Hex -> 0977caf4fabb to ASCII -> 	w???? does not equal hello
dec>448378203247
Good job! 448378203247 to Hex -> 68656c6c6f to ASCII -> hello is hello
Correct! Completed level 2

----------- LEVEL 3: Hashing Function ------------
A Hashing Function intakes any data of any size and irreversibly transforms it to a fixed length number. For example, a simple Hashing Function could be to add up the sum of all the values of all the bytes in the data and get the remainder after dividing by 16 (modulus 16)

TO UNLOCK NEXT LEVEL, give me a string that will result in a 6 after being transformed with the mentioned example hashing function

>F
Correct! Completed level 3

--------------- LEVEL 4: Real Hash ---------------
A real Hashing Function is used for many things. This can include checking to ensure a file has not been changed (its hash value would change if any part of it is changed). An important use of hashes is for storing passwords because a Hashing Function cannot be reversed to find the initial data. Therefore if someone steals the hashes, they must try many different inputs to see if they can "crack" it to find what password yields the same hash. Normally, this is too much work (if the password is long enough). But many times, people's passwords are easy to guess... Brute forcing this hash yourself is not a good idea, but there is a strong possibility that, if the password is weak, this hash has been cracked by someone before. Try looking for websites that have stored already cracked hashes.

TO CLAIM YOUR PRIZE, give me the string password that will result in this MD5 hash (MD5, like most hashes, are represented as hex digits):
08a81fafe787c93d02eb338b75f61819

>d3r7h
Correct! Completed level 4
You completed all 4 levels! Here is your prize: a24c028f0a572b9101afd00c86734472

```