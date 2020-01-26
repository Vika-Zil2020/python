num1= int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
if num1 + num2 == 7 or num1 + num2 == 11:
	print("Winner")
elif num1 + num2 == 2 or num1 + num2 ==3 or num1 + num2 ==12:
    print ("Loser")
else:
	print ("Not loser but not Winner:)")