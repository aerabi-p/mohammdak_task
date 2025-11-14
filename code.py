import numpy as np
def correct_answer_generator():
    prob=np.random.uniform()
    if prob <= 0.7:
        correctanswer="blue"
    else:
        correctanswer="green"

    return correctanswer

print(correct_answer_generator())