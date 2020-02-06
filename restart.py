user_input = input("enter the text")
def add_string(user_input):
  if len(user_input) > 2:
    if user_input[-3:] == 'ing':
     user_input += 'ly'
    else:
      user_input += 'ing'

  return user_input
print(add_string(user_input))