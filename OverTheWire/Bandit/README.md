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

This level focuses on finding information when many files are present within many
directories. We're given a specific size of the file and told it needs to be human
readable.

```
$ find . -type f -size 1033c -exec ls -l -sh {} \;
4.0K -rw-r----- 1 root bandit5 1.1K Dec 28 14:34 ./inhere/maybehere07/.file2
$ cat ./inhere/maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

This command finds all files in the current directory of type f (file as opposed to d for 
directory) with the size of 1033 bytes. Then it executes ls using the output from find, 
showing the file information with files that are in human readable format.

The {} gets a list of each file found from the find command. Note that it calls ls once 
for each file found. The \; is an escape command followed by the end of the command 
execution from find. The escape is needed to avoid passing the character to find.

## Level 6
User: bandit6
Pass: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

This level is similar to the previous one, but the file could be anywhere on the server.

```
$ find / -type f -size 33c -group bandit6 -user bandit7 -exec ls -la -sh {} \;
4.0K -rw-r----- 1 bandit7 bandit6 33 Dec 28 14:34 /var/lib/dpkg/info/bandit7.password
```

This time, we are searching for all the files with group bandit6 and user bandit7. We've
changed the . after find to a / to search the whole server.

## Level 7
User: bandit7
Pass: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

We are told the password for bandit8 is next to the word millionth in the file data.txt.
The grep command is useful here, because it will return the whole line of text next to
a searched word of our choice.

```
$ grep 'millionth' data.txt
cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

## Level 8
User: bandit8
Pass: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

The password for the next level is stored in the file data.txt and is the only line of 
text that occurs only once. So we need to find the unique line of text. There is a
command for this, but it only works if the lines are sorted, luckily there is a
command for that as well.

```
$ sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

## Level 9
User: bandit9
Pass: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

The password for the next level is stored in the file data.txt in one of the few human-
readable strings, beginning with several ‘=’ characters. If we try to cat this file, we'll
find that it returns a message about being a binary file. However, we can use the
command strings to get human readable text out of the file.

```
$ strings data.txt | grep "="
nfZ=
U=R*q
=-VW+
========== theP`
=uN
\<P5J7=^
========== password
L='.
L========== isA
G&eB_=
9T=8?
9=!/"
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

## Level 10
User: bandit10
Pass: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk


