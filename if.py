bank_account = 5000
user_inputed_item_price = int(input("Enter price of item you want to buy"))

if bank_account >= user_inputed_item_price:
	print ("you can buy this item")
elif input("You can't buy, need a loan? y/n") == "y" and bank_account +int(input("how much money do you need?")) >= user_inputed_item_price:
	 print("Now you can buy")
else:
	print("You can't buy this item")