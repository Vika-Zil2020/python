inputed_element =input("enter elements")
my_list =[]
def unique(inputed_element):
	for i in inputed_element:
		if i not in my_list:
			my_list.append(i)
	return my_list

print(unique(inputed_element))