import numpy as np
def gazing(correct_answer):
    
    prob = np.random.uniform()
    print(prob)
    if prob<=0.7:
        print(correct_answer)
    else:
        if correct_answer=="green":
            print("blue")
        else:
            print("green")
    
        
gazing("blue")