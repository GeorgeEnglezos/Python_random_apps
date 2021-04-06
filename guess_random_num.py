import random as ran
def createNum(x):
    num=ran.randint(0,x)
    return num


max=int(input("What is the max number:"))
numberToGuess=createNum(max)

while(True):
    cur=input(f"Guess the number between 0 and {max} :")
    if(int(cur)==int(numberToGuess)):
        print("CORRECT")
        break
    else:
        print("WRONG TRY AGAIN")



