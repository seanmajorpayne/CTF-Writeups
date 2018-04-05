# PicoCTF 2017 - Level 1 - Digital Camouflage

**Category:** Forensics **Points:** 50 

**Description:**

> We need to gain access to some routers. 
> Let's try and see if we can find the password in the captured network data

## Write-Up

We are provided a data.pcap file, which can be opened with Wireshark. Looking through
the packets, we see that there are HTTP packets being sent over the network. Since we are
looking for a login password and this is an HTTP connection, we should be looking for POST
requests. We can do this with the filter:

```
http.request.method == "POST"
```

Now we'll find one POST request. Right-click this file and click Follow -> TCP Stream.
We now see the following information

```
POST /pages/main.html HTTP/1.1
Referer: 10.0.0.1:8080/index.html
User-Agent: User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9*/*;q=0.8
Host: 10.0.0.1:8080
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 43
Accept-Language: en-US,en;q=0.5

userid=sullivanm&pswrd=UldPRVRNOWZhWQ%3D%3DHTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.9
Date: Sat, 19 Mar 2016 01:58:00 GMT
Content-type: text/html
```

Looking at the parameters we see a username and password. We can see that the password
contains %3D, which is an HTML character representing "=" so two equals at the end. That's
base64 padding. On Unix systems we can run the following in terminal:

```
$ echo UldPRVRNOWZhWQ== | base64 -D
RWOETM9faY
```

This is our flag!

