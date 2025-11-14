print(user_input)
point = 0
def reward(user_input, correct_answer):

    if user_input == 'r':
        if correct_answer == 'green':
            print('Well done')
            return 1
        else:
            print('Try harder')
            return 0

    if user_input == 'l':
        if correct_answer == 'blue':
            print('Well done')
            return 1
        else:
            print('Try harder')
            return 0

point += reward(user_input, 'green')
print(point)
