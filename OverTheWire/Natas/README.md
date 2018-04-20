# OverTheWire - Natas Write-up

**Category:** Web **Points:** N/A

**Description:**

> Natas is a wargame hosted by OverTheWire. These challenges are focused on web
> application hacking. There are 33 levels which get progressively more difficult.

## Level 0

Username: natas0
Password: natas0

We are given a simple webpage with the text "The password for the next level is on this
page. Opening the source code we see...

```
<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
```

## Level 1

Username: natas1
Password: gtVrDuiDfck831PqWsLEZy5gyDz1clto

The prompt is "You can find the password for the next level on this page, but 
rightclicking has been blocked!"

On Firefox you can shift-click, you can use burpsuite to intercept the response or
on Mac you can use Option+Command+U to view the source code.

```
<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
```

## Level 2

Username: natas2
Password: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

The prompt is "There is nothing on this page."

Looking at the source code we see the following:

```
<img src="files/pixel.png">
```

Opening the files directory, we find a users.txt file with the password for natas3

## Level 3

Username: natas3
Password: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14

The prompt is "There is nothing on this page." Looking in the source code we see...

```
<!-- No more information leaks!! Not even Google will find it this time... -->
```

Doing a Google Search for Natas3 shows a directory result we shouldn't have access to.
The users.txt file contains the password for level 4.

## Level 4

Username: natas4
Password: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

The prompt says "Access disallowed. You are visiting from "" while authorized users 
should come only from "http://natas5.natas.labs.overthewire.org/"

Obviously we don't have access to level 5 yet. The site is pulling the empty string
from the referer data sent in the HTML header. Opening up BurpSuite, we can use
intercepter to modify our request to the site. (some info omitted). If you haven't
set up Burp, there are plenty of tutorials online. This wouldn't work for me in Chrome,
so I'd recommend using Firefox. 

```
GET /index.php HTTP/1.1
Host: natas4.natas.labs.overthewire.org
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://natas5.natas.labs.overthewire.org/
Connection: close
Upgrade-Insecure-Requests: 1
```




