def fast_print():
	x = int(input("Enter number of times: "))
	y = input("Enter character: ")
	z = input("Enter end character: ")
	for i in range(0,x):
		print(y, end=""),
	print(z)

fast_print()