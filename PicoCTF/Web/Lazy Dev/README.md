# PicoCTF 2017 - Level 1 - LazyDev

**Category:** Web **Points:** 50

**Description:**

> I really need to login to this website, but the developer hasn't implemented login yet. 
> Can you help?

This is the final challenge for level 1. We can see on the site there is a login form.
Looking at the source code, we see the following:

```
<h1>Enter the password</h1>
<input id="password">
<button type="button" onclick="process_password()">Submit</button>
```

The onclick is showing that we have a javascript function being run. Looking further
down in the source we see
```
<script type="text/javascript" src="/static/client.js"></script>
```

This javascript file contains the following code:

```
//Validate the password. TBD!
function validate(pword){
  //TODO: Implement me
  return false;
}

//Make an ajax request to the server
function make_ajax_req(input){
  var text_response;
  var http_req = new XMLHttpRequest();
  var params = "pword_valid=" + input.toString();
  http_req.open("POST", "login", true);
  http_req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  http_req.onreadystatechange = function() {//Call a function when the state changes.
  	if(http_req.readyState == 4 && http_req.status == 200) {
      document.getElementById("res").innerHTML = http_req.responseText;
    }
  }
  http_req.send(params);
}

//Called when the user submits the password
function process_password(){
  var pword = document.getElementById("password").value;
  var res = validate(pword);
  var server_res = make_ajax_req(res);
}
```

We can see that the validate password function hasn't been implemented, so when the
process_password() function runs, our res variable will never be true, which is passed
to the make_ajax_req(input) function. However, we can see that this function makes an
HTTP request using the supplied string as a parameter. So if we call this function
directly, we can get the password. Changing the code in the source using Firebug or
Chrome's inspect, we can hit submit and get our flag.

```
<button type="button" onclick="make_ajax_req(true)">Submit</button>
```

Flag: client_side_is_the_dark_sidee5dbd5f8c6ae5e282766571e06569d50






