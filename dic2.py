class Pow:
	def __init__(self,num1,n):
		self.num1 = num1
		self.n = n
	def function(self):
		self.num1 = int(input("enter your number"))
		self.n =int(input("enter other number"))
		return pow(self.num1,self.n)

result = Pow("num1","n")
print(result.function())




