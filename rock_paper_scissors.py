import random as ran

playerWins=0
botWins=0

def checkInput(x):
    while(True):
        if not x=='r' or x=='p' or x=='s':
            x=input('Correct input is: r,p,s').lower()
        else:
            break
    return x

if __name__ == '__main__':

    while(playerWins<10 and botWins<10):
        user=input('Choose r,p,s :').lower()
        bot=ran.choice(['r','p','s']) # needs the [] to work

        if user=='r' and bot=='s' or user=='s' and bot=='p' or user=='p' and bot=='r':
            print("You Won :) ")
            playerWins+=1
        elif user==bot:
            print("it's a tie")
        else:
            print("Bot won :( ")
            botWins += 1
        print(f"Score is Player: {playerWins} :Bot: {botWins}")
    else:
        if playerWins>botWins:
            print("Player won!!!")
        else:
            print("Bot Won!!!")