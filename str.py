class Action:
	def __init__(self):
	    self.string = ""

	def get_string(self):
		self.string=input()

	def print_string(self):
		print(self.string.upper())

string=Action()
string.get_string()
string.print_string()