# HackCenter Engima2017 readasm

**Category:** Binary **Points:** 5 

**Description:**

> At the end of this sequence of instructions, how many bytes separate esp and the stored return address on the program's stack? Assume that we called this function using standard 32-bit x86 calling conventions.

## Write-Up

Here is the assembly provided:

```
804847c functioname:
804847c: push %ebp
804847d: mov %esp,%ebp
804847f: sub $0x60,%esp
8048482: movl $0x0,0x4(%esp)
804848a: movl $0x8048580,(%esp)
  
```

At the start of a function call, the function arguments will be pushed onto the stack,
followed by the 4-byte return address. In the assembly above, %ebp is pushed onto the stack,
adding 4-bytes of distance between the %esp and the return address. The value of %esp is
then placed into %ebp, effectively pointing %ebp at the top of the stack (but not modifying
the contents of the stack, thus we are still 4-bytes away). We then subtract 0x60 (94) from
%esp, meaning we are now 100 bytes away from the return address (Recall that the stack
grows towards lower addresses). The final instructions move values into the location 0x4
below %esp (towards higher addresses) and into the location of %esp. Neither of these instructions
change our %esp location, so the final distance between %esp and the return address is
100 bytes.





