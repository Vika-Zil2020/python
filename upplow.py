inputed_text = input("enter the text")
def letters(inputed_text):
	upper=0
	lower=0
	for i in inputed_text:
		if i.isupper()==True:
			upper+=1
		else:
			lower+=1
	print("your upper letters are: "+ str(upper) + " " + "your lower letters are: " +str(lower))
letters(inputed_text)