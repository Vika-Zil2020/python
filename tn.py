limit= int(input("Enter the limit"))
def show_numbers(limit):
	for i in range(0, limit):
		if i %2==0:
			print(i, "Even")
		elif i %2!=0:
			print(i, "Odd")

show_numbers(limit)
