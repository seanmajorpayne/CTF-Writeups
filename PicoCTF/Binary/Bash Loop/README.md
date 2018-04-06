# PicoCTF 2017 - Level 1 - Bash Loop

**Category:** Binary Exploitation **Points:** 40

**Description:**

> We found a program that is hiding a flag but requires you to guess the number it is 
> thinking of. Chances are Linux has an easy way to try all the numbers... 
> Go to /problems/995871fcb203d3e223e9e4aaa65e4053 and try it out!

If we run this program, we'll get a prompt saying the program accepts a number between
0 and 4096. Testing all of these manually would be a pain, so we need to use a bash loop.
If we run the program once with an incorrect number, we'll get a prompt saying "Nope..."
alerting us that the number is wrong. So we can pipe the output into a reverse grep search
for this word. This gives us our flag.

```
$ for val in {0..4096}                             
> do                                                     
> ./bashloop $val | grep -v "Nope"                       
> done                                                   
Yay! That's the number! Here be the flag: 5cabdea71dd5f42
8c8e080db5010a7d6 
```