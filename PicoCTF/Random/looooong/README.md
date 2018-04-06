# PicoCTF 2017 - Level 1 - looooong

**Category:** Random **Points:** 20

**Description:**

> I heard you have some "delusions of grandeur" about your typing speed. How fast can 
> you go at shell2017.picoctf.com:44840?

When we netcat to this service, we will be prompted with something similar to the
following:

```
To prove your skills, you must pass this test.
Please give me the 'e' character '623' times, followed by a single '8'.
To make things interesting, you have 30 seconds.
```

Everytime the characters and counts will change. So we need to write a script to make this
easy. Using python:

```
def fast_print():
	x = int(input("Enter number of times: "))
	y = input("Enter character: ")
	z = input("Enter end character: ")
	for i in range(0,x):
		print(y, end=""),
	print(z)

fast_print()
```

We can open two terminal windows and run our python script in one and copy paste over
the values.

```
You got it! You're super quick!
Flag: with_some_recognition_and_training_delusions_become_glimpses_97b1f7514342008e75bd0238aa007d09
```