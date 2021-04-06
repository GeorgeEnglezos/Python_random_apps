import random as ran


max=int(input("Think of a number bigger than 0!\nWhat's the max? "))
min=0

def checkInput(x):
    while not (x=='c' or x=='h' or x=='l'):
        guess = input(f"Is {cur} the correct num?(c,h,l)")
    return x

while(True):
    print(f"min= {min} and max= {max}")
    cur=ran.randint(min,max)
    if min==max:
        print(f"The min and max are the same so: {min}")
        break
    else:
        guess = checkInput(input(f"Is {cur} the correct num?(c,h,l)"))
    if guess=='c':
        print("The bots always win, hehe!")
        break
    elif guess=='h':
        print(f"I will search from 0-{cur} then!")
        max=cur-1
    elif guess=='l':
        print(f"I will search from {cur}-{max} then!")
        min=cur+1

