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

## Level 5

Username: natas5
Password: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

The prompt is "Access disallowed. You are not logged in." There is no information on
the page to signify a way to login, so we can guess that the session data is saved with
a cookie. Let's check intercepter in Burp again. Sure enough we see:

```
Cookie: loggedin=0
```

Changing 0 to 1 we are successfully logged in.

## Level 6

Username: natas6
Password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

We are presented with a prompt to enter the secret passcode with a login form. Looking at
the source code we find:

```
<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```

Looking at the /includes/secret.inc URL we see a blank page, but viewing the source code
reveals

```
<!--? $secret = "FOEIUWGHFEEUHOFUOIU"; ?-->
```

Putting this secret into the form gives us the password.

## Level 7

Username: natas7
Password: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9 

We are given a page with two links, home and about. Clicking either of these links changes
the URL to include a php variable (ex. ?page=about). There is nothing else of interest
on this page (however the source has a hint about the file structure). We were originally
told in the Natas game overview that all passwords are found in /etc/natas_webpass/natas#

Since the PHP variable is pulling information from the server, let's modify this to
the file path

```
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
```

This gives us the password for level 8

## Level 8

Username: natas8
Password: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

We are given another secret code login with a link to view the page source. Looking at the
source code we see

```
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

So digesting what's going on, we have some PHP code. The code is taking the user supplied
secret, running it through the encodeSecret function and checking to see if this matches
the encodedSecret variable. So we can take the encodedSecret variable, and do all of the 
operations in reverse to determine what our final output should be.

The secret was first base64 encoded, then the string was reversed and finally the ASCII
was converted to Hexadecimal. So starting by reversing the hexadecimal to ASCII in
terminal we have.

```
$ echo '3d3d516343746d4d6d6c315669563362' | xxd -r -p | rev | base64 -D
```

We are piping the String into xxd.
xxd - makes a hexdump
-r reverses (ASCII to hexdump)
-p outputs in plaintext
Then piping this into rev, which reverses the String
Then piping this into base64 -D, which decodes the base64

This gives us oubWYf2kBq. Putting this back into the secret field gets us the natas9 PW.

## Level 9

Username: natas9
Password: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

This page presents us with a search function that looks for words and outputs them to the
page. Looking at the page source, we see the following code:

```
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search>
</form>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```






