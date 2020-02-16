class Bank:
	def __init__(self,name,surname,email,bank_balance =0):
		self.name = name
		self.surname = surname
		self.email = email
		self.bank_balance = bank_balance

	def get_balance(self):
		return self.bank_balance

	def withdraw(self, amount):
		self.bank_balance-=amount
		self.get_balance()

	def deposit(self,amount):
		self.balance+=amount
		self.get_balance()

def create_instance():
    global user_dict
user_dict ={}
name = input("enter your name")
surname = input("enter your surname")
email = input("enter your email")
user_dict[name] = Bank(name,surname,email)

def get_balance():
	name = input("enter your name")
	print(user_dict[name].get_balance())

while True:
	print("1)Create acconut")
	print("2)Withdraw")
	print("3)Deposit")
	print("4)Check balance") 
	print("5) Exit Programm")
	user_choice = input("Choose one of the options")
	if user_choice=="1":
		creat_instance()
	elif user_choice =="4":
		get_balance()
	else:
		break

		