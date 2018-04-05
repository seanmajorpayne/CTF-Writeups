# PicoCTF 2017 - Level 1 - Keyz

**Category:** Cryptography **Points:** 20

**Description:**

> While webshells are nice, it'd be nice to be able to login directly. To do so, 
> please add your own public key to ~/.ssh/authorized_keys, using the webshell. 
> Make sure to copy it correctly! The key is in the ssh banner, displayed when you 
> login remotely with ssh, to shell2017.picoctf.com

So we need to set up an SSH connection with a private, public key-pair. There are plenty
of tutorials for this online. We'll start by logging into the PicoCTF shell. We then
need to generate a private public key pair and copy the public key into the
authorized_keys folder.

```
$ ssh-keygen -t rsa 4096
Generating public/private rsa key pair.                              
Enter file in which to save the key (/home/majorpayne/.ssh/id_rsa):  
Created directory '/home/majorpayne/.ssh'.                           
Enter passphrase (empty for no passphrase):                          
Enter same passphrase again:                                         
Your identification has been saved in /home/majorpayne/.ssh/id_rsa.  
Your public key has been saved in /home/majorpayne/.ssh/id_rsa.pub.  
The key fingerprint is:
76:e9:35:d7:a5:93:f9:52:c8:dc:21:d6:6e:c6:55:1a majorpayne@shell-web 
The key's randomart image is:                                        
+---[RSA 4096]----+                                                  
|              E .|                                                  
|              .o.|                                                  
|             o.oo|                                                  
|           ..o+B+|                                                  
|        S o o X=+|                                                  
|       . o . oo+ |                                                  
|          .   . .|                                                  
|               . |                                                  
|                 |                                                  
+-----------------+   
$ cd .ssh
$ ls
id_rsa id_rsa.pub
$ cat id_rsa.pub > ~/.ssh/authorized_keys
```

Once we've done this, we need to cat the id_rsa file which has our private key. We can
copy this into a text editor in our local computer and save it. If we try to connect, the
server will complain that the key cannot be accessible to multiple users, so we need to
remove permissions on the file. After that we can connect to ssh using the -i parameter
to include our private key in the connection.

```
$ chmod 400 rsa_key
$ ssh -i rsa_key majorpayne@shell2017.picoctf.com
Enter passphrase for key 'rsa_key': 
Congratulations on setting up SSH key authentication!
Here is your flag: who_needs_pwords_anyways
```
