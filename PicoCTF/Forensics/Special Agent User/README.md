# PicoCTF 2017 - Level 1 - Special Agent User

**Category:** Forensics **Points:** 50 

**Description:**

> We can get into the Administrator's computer with a browser exploit. 
> But first, we need to figure out what browser they're using. Perhaps 
> this information is located in a network packet capture we took: data.pcap. 
> Enter the browser and version as "BrowserName BrowserVersion". NOTE: We're just 
> looking for up to 3 levels of subversions for the browser version (ie. Version 1.2.3 
> for Version 1.2.3.4) and ignore any 0th subversions (ie. 1.2 for 1.2.0)

This challenge is focused on locating HTTP Request headers, which specify the user's
information. Only two fields are required in these headers, the method specification and
the host. We need to focus on requests being sent by the user, so looking at the GET
requests is a good bet. We can filter with the command:

```
http.request.method == "GET"
```

Right-click on some of them and Follow -> TCP Stream, on many, the method request is shown
as a wget, which is executed from the linux terminal. One of these however, shows the
following:

```
GET / HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F
Accept: */*
Host: 10.0.0.1
Connection: Keep-Alive
```

The Mozilla header is legacy information that's usually in headers, but looking towards
the end we see Chrome. That's our flag.

Flag: Chrome 34.0.1847