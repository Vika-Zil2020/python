my_list1 = [33,"apple","69"]
my_list2 = ["banana"]
def common(my_list1,my_list2):
	for i in my_list1:
		for j in my_list2:
			return bool(i == j)

print(common(my_list1,my_list2))