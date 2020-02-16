class Vehicle:
	def __init__(self,color,name,worth):
		self.color = color
		self.name = name
		self.worth = worth
car1= Vehicle("red","Fer","$60,000.00")
car2 =Vehicle("blue","Jump","$10,000.00")
print(car1.color,car1.name,car1.worth)
print(car2.color,car2.name,car2.worth)