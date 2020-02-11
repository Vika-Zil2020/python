file1 = open("content.txt", "r")
file2 = open("content2.txt", "w")
file2.writelines(file1)

file1.close()
file2.close()

