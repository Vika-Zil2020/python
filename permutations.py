my_list = []
for a in range(0,10):
	for b in range(0,10):
		for c in range(0,10):
			num =str(a)+str(b)+str(c)
			if num not in my_list and int(num)<1000:
				my_list.append(num)

print(my_list)
