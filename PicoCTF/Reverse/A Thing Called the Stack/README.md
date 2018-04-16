# PicoCTF 2017 - Level 2 - A Thing Called the Stack

**Category:** Reverse Engineering **Points:** 60

**Description:**

> A friend was stacking dinner plates, and handed you this, saying something about a 
> "stack". Can you find the difference between the value of esp at the end of the code, 
> and the location of the saved return address? Assume a 32 bit system. Submit the answer 
> as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 
> would be submitted as 0x7df, not 0x000007df

We are given the following Assembly file:

```
foo:
    pushl %ebp
    mov %esp, %ebp
    pushl %edi
    pushl %esi
    pushl %ebx
    sub $0x48, %esp
    movl $0x1, (%esp)
    movl $0x2, 0x4(%esp)
    movl $0x3, 0x8(%esp)
    movl $0x4, 0xc(%esp)
```

The important thing to understand here is which commands affect the value of ESP. ESP is
the stack pointer. In the code above, push and subtract affect ESP, while the mov
commands do not. So doing some quick math.

We first push EBP onto the stack, which takes up 4 bytes. We then run a mov command, which
does not affect our stack pointer. We then push three pointer values onto the stack and
since this is a 32 bit system, each of the pointers has a size of 4 bytes. Lastly we
subtract 0x48 bytes from stack pointer (moving it 72 bytes further away from its
original position.

Adding this all up, we have (0x48 + (0x4 * 4)) = 0x58. This is our flag.