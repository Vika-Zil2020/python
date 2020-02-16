x = int(input("enter fisrt num"))
y = int(input("enter sec num"))
z = int(input("enter third num"))
def ankyun(x,y,z):
	if x**2== y**2 +z**2 or y**2== x**2+ z**2 or z**2==x**2 +y**2:
		print("uxxankyun erankyun")
	else:
		print("uxxankyun chi")

ankyun(x,y,z)

