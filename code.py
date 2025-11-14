import numpy as np

def correct_answer_generator():
    prob=np.random.uniform()
    if prob <= 0.7:
        correct_answer="blue"
    else:
        correct_answer="green"

    return correct_answer

def gazing(correct_answer):
    
    prob = np.random.uniform()
    print(prob)
    if prob<=0.7:
        return correct_answer
    else:
        if correct_answer=="green":
            return "blue"
        else:
            return "green"
        
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
import pandas as pd
point = 0
count = 0
data = []
for i in range(5) :     
    count +=1  
    user_input = input('please enter your answer: ')
    print(user_input)
    correct_answer = correct_answer_generator()
    gaze = gazing(correct_answer)
    print(gaze)
    point += reward(user_input, correct_answer)
    print(point)
    data.append([count, gaze,user_input, correct_answer, point])
print(data)
columns=["trial", "gaze_direction", "chosen_card", "correct_card", "reward"]
data_csv = pd.DataFrame(data, columns=columns)
print(data_csv)
data_csv.to_csv()



 