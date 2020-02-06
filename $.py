user_input = "restart"
def change_letter(user_input):
	simb = user_input[0]
	user_input = user_input.replace(simb, "$")
	user_input = simb + user_input[1:]
	return user_input


print(change_letter(user_input))

