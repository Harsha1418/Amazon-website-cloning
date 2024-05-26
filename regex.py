def  hello(val):
	print("Hi {}, Hello How are U".format(val))
	hello(val) # RecursionError: maximum recursion depth exceeded

#Main program
hello("Rossum")