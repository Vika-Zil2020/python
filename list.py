my_list = ["BMW", "GG", "626", "clkmjjc"]
count = 0
for i in my_list:
	if len(i)>=2:
		if i[0]==i[-1]:
		    count+=1

print(count)
