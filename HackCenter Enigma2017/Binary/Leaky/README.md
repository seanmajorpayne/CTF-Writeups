# HackCenter Engima2017 Leaky.c

**Category:** Binary **Points:** 60 

**Description:**

> Leak the key from memory. Source is available at leaky.c, and the binary's running on enigma2017.hackcenter.com:49769.

## Write-Up

The provided code shows us the following:

```
  unsigned int key = ???;
  unsigned int filler4 = 0x70571007;
  unsigned int filler5 = 0x51107055;
  unsigned int filler6 = 0x50755011;

  unsigned int red = read(STDIN_FILENO,buf,80);
  buf[red] = '\x00';
  printf(buf);
  
```

Okay so we can see the flag (key) is loaded directly into a variable within main, meaning 
that it will be on our stack frame. An argument is read from the user with `STDIN_FILENO`
and stored in the buffer 'buf.' The buffer is then used without formatting within printf.

This is a format string vulnerability. Let's print some format strings into the program.

`$ perl -e 'print "%x "x11;' | nc enigma2017.hackcenter.com 5175`

Within the output, we'll get a series of hex values on the stack. The last one is our
flag! (I figured out where it was in the stack by using more format strings until the
variables started showing up, since the stack is FILO, the key will be located after
filler 4.








