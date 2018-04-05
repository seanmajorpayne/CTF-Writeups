# kebab STO - Nuit Du Hack Quals 2018 Write-Up

**Category:** Network **Points:** 350 

**Description:**

> The challenge consists in finding the flag into a network capture.
> Challenge is listening on port 8888

## Write-Up

The "STO" must stand for "Security through Obscurity" because the challenge led us on a 
wild goose chase. We spent a long time trying to get a decrypted password to work with
Wireshark, but it turned out the password wasn't used for this. Here is the solution:

We are provided with a pcap file kebabsto.pcapng. Opening this file in Wireshark we see
a series of TCP streams, where the following is revealed. 

1. Two people are discussing a file via email

```
AUTH PLAIN AHNhbGFkZUBkZWJpYW4ueW8Ac2FsYWRlMTIz
235 2.7.0 Authentication successful
MAIL FROM:<salade@debian.yo> BODY=8BITMIME SIZE=668
250 2.1.0 Ok
RCPT TO:<tomate@debian.yo>
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
Subject: Re: Private
To: tomate <tomate@debian.yo>
References: <6c9268e7-035b-0fa4-0486-c6624af41265@debian.yo>
From: salade <salade@debian.yo>
Message-ID: <5f8e93f0-9b6a-522f-f35a-3225bc919df7@debian.yo>
Date: Thu, 21 Dec 2017 18:59:07 +0100
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101
 Thunderbird/52.4.0
MIME-Version: 1.0
In-Reply-To: <6c9268e7-035b-0fa4-0486-c6624af41265@debian.yo>
Content-Type: text/plain; charset=utf-8; format=flowed
Content-Transfer-Encoding: 7bit
Content-Language: en-US

I can help you if you want.


On 12/21/17 17:07, tomate wrote:
> They provided a file but I don't know what it contains.
```

2. One of the emails reveals the file begins with kd... and a curl request is sent 
for this file

```
GET / HTTP/1.1
Host: 10.0.2.5:8000
User-Agent: curl/7.55.1
Accept: */*

HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/2.7.14+
Date: Thu, 21 Dec 2017 16:10:20 GMT
Content-type: text/html; charset=UTF-8
Content-Length: 220

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><html>
<title>Directory listing for /</title>
<body>
<h2>Directory listing for /</h2>
<hr>
<ul>
<li><a href="kdsqfkpdsdf">kdsqfkpdsdf</a>
</ul>
<hr>
</body>
</html>
  
```

3. The file is received. Looking at the beginning section we see the file header 'PK'
which stands for Phil Katz, the creator of zip. Great we have a zip file.

```
GET /kdsqfkpdsdf HTTP/1.1
User-Agent: Wget/1.19.1 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: 10.0.2.5:8000
Connection: Keep-Alive

HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/2.7.14+
Date: Thu, 21 Dec 2017 16:10:34 GMT
Content-type: application/octet-stream
Content-Length: 56148
Last-Modified: Thu, 21 Dec 2017 09:46:14 GMT

PK.........U.K.P[j............lkdjflknezczUT	....;Z..;Zux................T...7>t. )
..H#..".-.")- % ]R...HK.4R..R. ..........|..[..>.u#..5{..U...g..$......sq.........d...|..
z<.4...h.S.._..x|.....iF.vx...............OP...".
```

4. Running File -> Export -> HTTP stream we can download this zip file & extract it
which leaves us with a zip file containing another pcap. This file's data is encrypted
so let's continue through the first pcap for more clues.

5. Ignoring this for a bit, going back to the emails in the first pcap, we continue
to find more interesting info in the emails.

```
They also retrieved a public key and an interesting cipher text
(attached documents).

Besides, they also found a service at mydomainndh.ndh (port 55555) which
decrypts every text encrypted with the public key, apart from the
interesting one.

--------------821D8D192BDE01EA2B1C5E07
Content-Type: application/zip;
 name="docs.zip"
Content-Transfer-Encoding: base64
Content-Disposition: attachment;
 filename="docs.zip"

UEsDBAoAAAAAAFZ6lUsAAAAAAAAAAAAAAAAFABwAZG9jcy9VVAkAA8PCO1rdwjtadXgLAAEE
AAAAAAQAAAAAUEsDBBQAAAAIALd5lUvQbcUR4wAAABABAAAPABwAZG9jcy9wdWJrZXkucGVt
VVQJAAOawTtamsE7WnV4CwABBAAAAAAEAAAAAGXPvVaDMABA4Z2n6M7hlAoKjEmIIWDTRsQD
bBESaKAHqBZant6f1Tve7bOsnyAmlG2OGXyhaJPg4vdZxp4StQc2QelEUvrhhBxDwDMAXMJA
iOCJJ7DhyI9Zy6iQHS91tfO3c1HK3dO8xEZeTcr/fNflBXHlicfbpSZjdOg7hL8EVolIUG76
7EwCoO/SC1yXVlHkyb7QrT1Kaqy79PU6d+71efRANYAgdtb6EGdi3T6oocl7YS5qPca3KRig
NxdAuW+lduwwS9WY0co4iWaxdat13Y5nqbC50BBwAI0/IWbhP/Q3UEsDBBQAAAAIAFZ6lUus
24QeoQAAADUBAAAPABwAZG9jcy9jaXBoZXJUZXh0VVQJAAPDwjtaw8I7WnV4CwABBAAAAAAE
AAAAABWPyREAQQgC/xuNFwL5J7bOS6pstWWJTYxoe/3qYopgqq6OQruta0ieSC8nAmvPMGJU
dmics9wyyrkHpTRV0wVPZoYboT5GDCYmr+GHtrBhLuuGW4llFBXLTFgBbJPOEurBXQ6c0m1c
xGlI0ZF9wq0L1SeoSkY/n+jtPLcLieaBhiYBAtmsZutOmad7MwzEiXVy4+6Z991gvMPi2ewk
6/sBUEsBAh4DCgAAAAAAVnqVSwAAAAAAAAAAAAAAAAUAGAAAAAAAAAAQAO1BAAAAAGRvY3Mv
VVQFAAPDwjtadXgLAAEEAAAAAAQAAAAAUEsBAh4DFAAAAAgAt3mVS9BtxRHjAAAAEAEAAA8A
GAAAAAAAAQAAAKSBPwAAAGRvY3MvcHVia2V5LnBlbVVUBQADmsE7WnV4CwABBAAAAAAEAAAA
AFBLAQIeAxQAAAAIAFZ6lUus24QeoQAAADUBAAAPABgAAAAAAAEAAACkgWsBAABkb2NzL2Np
cGhlclRleHRVVAUAA8PCO1p1eAsAAQQAAAAABAAAAABQSwUGAAAAAAMAAwD1AAAAVQIAAAAA

--------------821D8D192BDE01EA2B1C5E07--

```

6. Here we see a file "docs.zip" being sent via email and it's base64 encoded. Using
python, we can convert this base64 to binary and write it into a zip file.

```
import base64

base64_text = """UEsDBAoAAAAAAFZ6lUsAAAAAAAAAAAAAAAAFABwAZG9jcy9VVAkAA8PCO1rdwjtadXgLAAEE
AAAAAAQAAAAAUEsDBBQAAAAIALd5lUvQbcUR4wAAABABAAAPABwAZG9jcy9wdWJrZXkucGVt
VVQJAAOawTtamsE7WnV4CwABBAAAAAAEAAAAAGXPvVaDMABA4Z2n6M7hlAoKjEmIIWDTRsQD
bBESaKAHqBZant6f1Tve7bOsnyAmlG2OGXyhaJPg4vdZxp4StQc2QelEUvrhhBxDwDMAXMJA
iOCJJ7DhyI9Zy6iQHS91tfO3c1HK3dO8xEZeTcr/fNflBXHlicfbpSZjdOg7hL8EVolIUG76
7EwCoO/SC1yXVlHkyb7QrT1Kaqy79PU6d+71efRANYAgdtb6EGdi3T6oocl7YS5qPca3KRig
NxdAuW+lduwwS9WY0co4iWaxdat13Y5nqbC50BBwAI0/IWbhP/Q3UEsDBBQAAAAIAFZ6lUus
24QeoQAAADUBAAAPABwAZG9jcy9jaXBoZXJUZXh0VVQJAAPDwjtaw8I7WnV4CwABBAAAAAAE
AAAAABWPyREAQQgC/xuNFwL5J7bOS6pstWWJTYxoe/3qYopgqq6OQruta0ieSC8nAmvPMGJU
dmics9wyyrkHpTRV0wVPZoYboT5GDCYmr+GHtrBhLuuGW4llFBXLTFgBbJPOEurBXQ6c0m1c
xGlI0ZF9wq0L1SeoSkY/n+jtPLcLieaBhiYBAtmsZutOmad7MwzEiXVy4+6Z991gvMPi2ewk
6/sBUEsBAh4DCgAAAAAAVnqVSwAAAAAAAAAAAAAAAAUAGAAAAAAAAAAQAO1BAAAAAGRvY3Mv
VVQFAAPDwjtadXgLAAEEAAAAAAQAAAAAUEsBAh4DFAAAAAgAt3mVS9BtxRHjAAAAEAEAAA8A
GAAAAAAAAQAAAKSBPwAAAGRvY3MvcHVia2V5LnBlbVVUBQADmsE7WnV4CwABBAAAAAAEAAAA
AFBLAQIeAxQAAAAIAFZ6lUus24QeoQAAADUBAAAPABgAAAAAAAEAAACkgWsBAABkb2NzL2Np
cGhlclRleHRVVAUAA8PCO1p1eAsAAQQAAAAABAAAAABQSwUGAAAAAAMAAwD1AAAAVQIAAAAA"""

base64_text = base64_text.replace('\n', '').replace('\t', '').replace(' ', '')
decoded_text = base64.b64decode(base64_text)
with open("new_file.zip","wb+") as zipFile:
	zipFile.write(decoded_text)

```
7. This leaves us with a public key file & a cipher text.

```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8JNhNIaekQZjc18/vYZe16vwJ
Xcqf8sVjZrCQf7a5xrdGpHOlkCEtaEfKaKCX+8NmG9Ajye7944IcHH7elYjh0peI
z1SRuvk4uFp7AcoA9J3zdOJUaz/2fogXla+wfzPJxq9oB7vYAf4TZj30DUSfpUIc
iagw0jhjjdhpmefE+wIDAQAB
-----END PUBLIC KEY-----

---Cipher Text---
72873754879996948796542757182427480866384878894019674005699447004
82990849146762952916196188422432594111093508346787071541259991613
85609767229538156702780671159805563779128521385329058660936506998
80301357138301236748217037629036311469031537013958415575513723738
671978421707050599317605219729945496472798064172

```

8. Connecting to the service hosted on port 8888 (as specified in challenge description)
and copying the cipher text into their decryption service, we get
123360975347216093033775350245751721746535757669936, after converting to hex format and
then to ASCII, we get Th1s1s2P@ss_W0rd%M0f0, however trying to decrypt the second pcap 
with this does not work. Running aircrack-ng on the pcap with a standard dictionary gives 
us the WPA password.

```
$ aircrack-ng -w word_list.txt lkdjflknezcz.pcap

                                Aircrack-ng 1.2 rc4

      [00:00:00] 21/20 keys tested (1276.67 k/s) 

      Time left: 0 seconds                                     105.00%

                           KEY FOUND! [ abcdefgh ]


      Master Key     : 46 DE 68 77 59 26 52 28 68 59 E3 E9 27 C2 75 66 
                       77 A0 C0 C2 59 7C B7 6A 52 06 A3 B8 5D 7F 33 29 

      Transient Key  : C8 2A 89 4B 43 93 57 73 35 B7 9E 21 99 8A 5A F2 
                       B6 89 B8 10 F6 AF 77 68 A8 B4 69 E7 30 E4 A7 9B 
                       88 32 93 FF AA B5 8E CE 9E AC 4A 05 05 0C EC BB 
                       37 C9 12 11 5B DA 0C E9 D8 25 02 5E F3 D2 AA 4F 

      EAPOL HMAC     : 76 32 AE BA 65 FD A2 64 BD FD 8E 76 BA 1F B7 84 

```

9. Using this password, we are able to decrypt the pcap file. This leaves us with a few
TCP streams where we again see a PK header on a file transmission. Copying the raw data
into python, we're again able to convert it to a zip file.

```
import binascii

file_hex = "504b03040a0009000000476a924b7697d2733c0000003000000009001c00736c6b666473666c6a555409000306b2375a19b2375a75780b00010400000000040000000035979c6cb0ac04bd755ab6af55a8b8a8b25397bccb51d5cdf817f5e1b11b55210ef418c56768bfb3aaf3467ab65be3dc1746ed3652f6f68a957ee299504b07087697d2733c00000030000000504b01021e030a0009000000476a924b7697d2733c00000030000000090018000000000001000000a48100000000736c6b666473666c6a555405000306b2375a75780b000104000000000400000000504b050600000000010001004f0000008f0000000000"

binary = binascii.unhexlify(file_hex)

with open("new_file2.zip","wb+") as zipFile:
	zipFile.write(binary)
```

10. Using the password we found in the cryptographic message, we can open the zip file
which leaves us with the text file and the flag.

>The flag is : ndh2k18{M4k3M4tr10cHKa9r34T4g41n}





