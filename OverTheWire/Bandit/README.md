# OverTheWire - Bandit Write-Up

## Level 0

For the first level we are given the username, domain and port and asked to login via
SSH. This is very simple. The command line syntax for this uses the ssh command, followed
by the username@domain, the -p (port) flag and the #.

```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

We're then prompted for a password. Once entered, we get a welcome message and we're in!

```
$ ls
readme
$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
exit
```

ls lists all of the files in a directory. cat reads a file.

## Level 1

User: bandit1
Pass: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

The next level is very similar. This time when we list all the files, we see a '-' dash
character. This is a filename, but we can't directly cat it since dash is a special
character. Using the ./ syntax to specify the current directory, we can cat the file.

```
$ ls
-
$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

## Level 2

User: bandit2
Pass: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

Again, we have a similar situation. This time, we have spaces in a filename. In order
to not process these words as different commands, we have to group them together using
quotes.

```
$ ls
spaces in this filename
$ cat "spaces in this filename"
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

## Level 3

User: bandit3
Pass: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

This level focuses on navigating through directories and dealing with hidden files. We
have a directory called "inhere" but when we go into the file, we see nothing. We can do
a couple of things here. One is to find which will return all of the files
in the directory. We can also go in the directory and list hidden files.

```
$ ls
inhere
$ find
.
./.profile
./.bashrc
./inhere
./inhere/.hidden
./.bash_logout

$ cat ./inhere/.hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB

------Alternatively------
$ cd inhere
$ ls -lah
total 12K
drwxr-xr-x 2 root    root    4.0K Dec 28 14:34 .
drwxr-xr-x 3 root    root    4.0K Dec 28 14:34 ..
-rw-r----- 1 bandit4 bandit3   33 Dec 28 14:34 .hidden
$ cat .hidden
```

## Level 4

User: bandit4
Pass: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

This level focuses on finding information when many files are present. One easy way to
do this is to fun the file command on all of the files and see what types of files they
are.

```
$ ls
inhere
$ cd inhere
$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

## Level 5
User: bandit5
Pass: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
