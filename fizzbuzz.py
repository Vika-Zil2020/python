input_number = int(input("Enter the number"))
def fizzbuzz(input_number):
	if input_number %3==0 and input_number %5==0:
		return "fizzbuzz"
	elif input_number%3==0:
		return "fizz"
	elif input_number%5==0:
		return"buzz"
	else:
		return input_number

print (fizzbuzz(input_number))