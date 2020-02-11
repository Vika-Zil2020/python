file1 = open("txt.txt", "r")
list1 = []

for i in file1:
	x = i.split()
	
	list1.append(x[0])
	list1.append(" new word ")
	list1.append(x[3])
	
file2 = open("txt.txt", "w")
file2.writelines(list1)

file1.close()
file2.close()