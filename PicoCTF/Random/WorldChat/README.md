# PicoCTF 2017 - Level 1 - WorldChat

**Category:** Random **Points:** 30

**Description:**

> We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are 
> so many other people talking that we can't really keep track of what is going on! Go 
> see if you can find the messenger at shell2017.picoctf.com:14747. Remember to use 
> Ctrl-C to cut the connection if it overwhelms you!

If we netcat to this service, we will be flooded with messages. We need a way to only
grab what's important. If we pipe into a grep for a flag, we will still get a lot of
weird traffic from usernames with the word flag. However, we'll also see a message that
contains 1/8 of the flag. Using part of this string, we should be able to grep for each
part of the flag.

```
$ nc shell2017.picoctf.com 14747 | grep "/8 of the flag"
20:20:41 flagperson: this is part 1/8 of the flag - ab4b
20:20:42 flagperson: this is part 2/8 of the flag - 181f
20:20:46 flagperson: this is part 3/8 of the flag - 3bc9
20:20:49 flagperson: this is part 4/8 of the flag - 2758
20:20:50 flagperson: this is part 5/8 of the flag - 9e0d
20:20:50 flagperson: this is part 6/8 of the flag - 79a4
20:20:52 flagperson: this is part 7/8 of the flag - 845a
20:20:55 flagperson: this is part 8/8 of the flag - 3ace
```

Flag: ab4b181f3bc927589e0d79a4845a3ace