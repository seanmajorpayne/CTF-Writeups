# PicoCTF 2017 - Level 1 - ComputeRSA

**Category:** Cryptography **Points:** 50

**Description:**

> RSA encryption/decryption is based on a formula that anyone can find and use, 
> as long as they know the values to plug in. Given the encrypted number 150815, 
> d = 1941, and N = 435979, what is the decrypted number?

The RSA formula is (m^e)^d = m (mod n)