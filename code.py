import numpy as np
def correct_answer_generator():
    prob=np.random.uniform()
    if prob <= 0.7:
        correctanswer="blue"
    else:
        correctanswer="green"

    return correctanswer

def gazing(correct_answer):
    
    prob = np.random.uniform()
    print(prob)
    if prob<=0.7:
        print(correct_answer)
        return correct_answer
    else:
        if correct_answer=="green":
            print("blue")
            return "blue"
        else:
            print("green")
            return "green"
        
    
    
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
        
