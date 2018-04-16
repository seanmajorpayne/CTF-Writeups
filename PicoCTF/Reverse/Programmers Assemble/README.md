# PicoCTF 2017 - Level 2 - Programmers Assemble

**Category:** Reverse Engineering **Points:** 75

**Description:**

> You found a text file with some really low level code. Some value at the beginning has 
> been X'ed out. Can you figure out what should be there, to make main return the value 
> 0x1? Submit the answer as a hexidecimal number, with no extraneous 0s. For example, 
> the decimal number 2015 would be submitted as 0x7df, not 0x000007df

We are given the following assembly code:

```
.global main

main:
    mov $XXXXXXX, %eax
    mov $0, %ebx
    mov $0x5, %ecx
loop:
    test %eax, %eax
    jz fin
    add %ecx, %ebx
    dec %eax
    jmp loop
fin:
    cmp $0x7ee0, %ebx
    je good
    mov $0, %eax
    jmp end
good:
    mov $1, %eax
end:
    ret
```

Summarizing what's going on here: We set a value for eax, set ebx to zero, and set ecx
to 5. We then jump into loop and do a bitwise AND comparison of eax to itself. The JZ
stands for jump if zero and the only way we can get 0 from the bitwise comparison is if
eax is 0. Within the loop, we add the value of ecx to ebx and decrement eax by 1. Okay,
so we a have a while loop that says "while eax is not 0, add ecx to ebx and decrement
eax." Once this is done, we compare the value 0x7ee0 to ebx, if they are equal (je = jump
if equal) then we jump to good and set eax to 1 before returning. Otherwise, we move 0
into eax and return.

We want to return 0x1, so we need good to execute. In order for this to happen, we need
ebx to equal 0x7ee0 (which is 32480 in decimal). The question then, is how many times
do we need to run through the loop to get 32480 for ebx? We can solve this by dividing
by 5 (since we are adding ecx to ebx) and we get 6496.

If we run through the loop 6496 times, ebx will equal 32480. This means eax needs to
equal 6496 in order to return 1. Converting this to hex, we have 0x1960 which is our flag.