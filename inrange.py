inputed_number = int(input("enter a number: "))
def any_number (inputed_number):
	if inputed_number in range(100):
		print("in range: ")
	else:
		print("not in range: ")
any_number(inputed_number)