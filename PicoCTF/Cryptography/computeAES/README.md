# PicoCTF 2017 - Level 1 - ComputeAES

**Category:** Cryptography **Points:** 50

**Description:**

> You found this clue laying around. Can you decrypt it?

```
Encrypted with AES in ECB mode. All values base64 encoded
ciphertext = ACw5ftWAMhGPpxkbT1iun8aLQ55rGrYUMjeyZfIlYd8Whz8TwCMg1AgeTA83J7qt
key = zb9v8uGYo/BWzbhouenY2g==
```

We have an AES encrypted message with the key. They are both in base64 encoding. If we
try to base64 decode this message in terminal, we will get non-printable characters, so
we need to do everything with hex codes. Using https://cryptii.com/base64-to-hex we can
put in the message and key and get their hex representations.

Then using http://aes.online-domain-tools.com/ we can decrypt this message by providing
the hex. We will get 

```
00000000: 666c 6167 7b64 6f5f 6e6f 745f 6c65 745f  flag{do_not_let_
00000010: 6d61 6368 696e 6573 5f77 696e 5f36 3866  machines_win_68f
00000020: 6132 3138 637d 5f5f 5f5f 5f5f 5f5f 5f5f  a218c}__________
```

The first column is the address, the middle section are the hex values and the right is
our ASCII text flag!