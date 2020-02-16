class Person:
	def __init__(self,name,surname,age,eye_color,hair_color):
		self.name = name
		self.surname = surname
		self.age = age
		self.eye_color = eye_color
		self.hair_color = hair_color

	def name_surname (self):
		return self.name + " " + self.surname


my_person = Person("Vika","Baghdasaryan", 34, "Black", "Dark")
print(my_person.name)
print(my_person.hair_color)

print(my_person.name_surname())

my_person1 =Person("Nara","Baghdasaryan", 17,"Green","Shaten")
print(my_person1.name_surname())
# my_person =Person()
# print(my_person.name,my_person.age)