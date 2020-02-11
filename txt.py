file1 = open("txt.txt", "r")
name_list =[]
year_list = []

for i in file1:
	x = i.split()
	print(x)
	name_list.append(x[0])
	year_list.append(x[1])

print(name_list)
print(year_list)

file1.close()
