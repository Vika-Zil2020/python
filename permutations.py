<<<<<<< HEAD
# my_list = []
# for a in range(0,10):
# 	for b in range(0,10):
# 		for c in range(0,10):
# 			num =str(a)+str(b)+str(c)
# 			if num not in my_list and int(num)<1000:
# 				my_list.append(num)

# print(my_list)
# a = 0
# b = 0
# c = 0
# for l in range (a,10):
# 	for j in range(b,10):
# 		for f in range(c,10):
# 			print(l,j,f)

import random
chingachung = ['Scissors', 'Paper', 'Rock']
user = input("Enter your choice: ")
computer = random.choice(chingachung)



def play_chingachung(user, computer):
    continue_game = True
    while continue_game:
        if user == 'Scissors' and computer == 'Scissors':
            return "Player - ", user, "Computer - ", computer, "**** Draw! "
        elif user == 'Scissors' and computer == 'Paper':
            return "Player - ", user, "Computer - ", computer,  "**** Player win! "
        elif user == 'Scissors' and computer == 'Rock':
            return "Player - ", user, "Computer - ", computer, "**** Computer win! "
        elif user == 'Paper' and computer == 'Scissors':
            return "Player - ", user, "Computer - ", computer, "**** Computer win! "
        elif user == 'Paper' and computer == 'Rock':
            return "Player - ", user, "Computer - ", computer, "**** Player win! "
        elif user == 'Paper' and computer == 'Paper':
            return "Player - ", user, "Computer - ", computer, "*** Draw! "
        elif user == 'Rock' and computer == 'Rock':
            return "Player - ", user, "Computer - ", computer, "**** Draw! "
        elif user == 'Rock' and computer == 'Scissors':
            return "Player - ", user, "Computer - ", computer, "**** Player win! "
        elif user == 'Rock' and computer == 'Paper':
            return "Player - ", user, "Computer - ", computer, "**** Second player win! "
print(play_chingachung(user, computer))
=======
my_list = []
for a in range(0,10):
	for b in range(0,10):
		for c in range(0,10):
			num =str(a)+str(b)+str(c)
			if num not in my_list and int(num)<1000:
				my_list.append(num)

print(my_list)
>>>>>>> 3ca10fa45393c9830384d3422159e3e528716334
