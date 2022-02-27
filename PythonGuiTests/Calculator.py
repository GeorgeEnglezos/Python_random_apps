from tkinter import * #The needed library

#set the root widget
root=Tk() 
root.title("Calculator")

#Text Input
e=Entry(root,width=50,borderwidth=5,bg="black",fg="white")
e.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

ActionsToCalculate=[] #All the numbers and actions will be saved here

lastAction="+"

def button_click(number):#Inserts to the current Number
    tmp=str(e.get())
    numsInText=len(tmp)
    e.insert(numsInText,number)
    return

def button_add():

    #get the number 
    if not e.get()=='':
        currentString=str(e.get())
        ActionsToCalculate.append(int(currentString))
    else:
        ActionsToCalculate.append(0)
    ActionsToCalculate.append("+")
    e.delete(0,END) #Clean the Text Field
    return


def button_sub():

    #get the number 
    if not e.get()=='':
        currentString=str(e.get())
        ActionsToCalculate.append(int(currentString))
    else:
        ActionsToCalculate.append(0)
    ActionsToCalculate.append("-")
    e.delete(0,END) #Clean the Text Field
    return

def button_equal():
    counter=0
    finalNum=0
    haveToAdd=False
    haveToSub=False
    if not e.get()=='':
        ActionsToCalculate.append(e.get())
    print(ActionsToCalculate)
    for act in ActionsToCalculate:
        print("CALCULATING...")
        if not ((act=='+' or act=='-') and (counter==0 or counter==len(ActionsToCalculate))): #if there are + or - in the start or end there is no need to check them
            counter+=1
            print("current=",act)
            if act=="+":
                print('+ true')
                haveToAdd=True
            elif act=='-':
                print('- true')
                haveToSub=True
            elif not (haveToAdd or haveToSub): #First number in the list
                print('finalNum =',act)
                finalNum=int(act)
            elif haveToAdd:
                print(finalNum,'+=',act)
                finalNum+=int(act)
                haveToAdd=False
            elif haveToSub:
                print(finalNum,'-=',act)
                finalNum-=int(act)
                haveToSub=False
            else:
                print("ERROR")
    e.delete(0,END)
    e.insert(0,str(finalNum))
    ActionsToCalculate.clear
    ActionsToCalculate.append(finalNum)
    return


def button_clear():
    ActionsToCalculate.clear
    e.delete(0,END) #Clean the Text Field
    print("Numbers in list",len(ActionsToCalculate))
    return

button_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1)) #With the Lambda i can pass parameters to the method 
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0=Button(root,text="0", padx=40,pady=20,command=lambda: button_click(0))

button_add=Button(root,text="+", padx=40,pady=20,command=button_add)
button_sub=Button(root,text="-", padx=40,pady=20,command=button_sub)
button_equal=Button(root,text="=", padx=40,pady=20,command=button_equal)
button_clear=Button(root,text="C", padx=40,pady=20,command=button_clear)

#Buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)
button_clear.grid(row=5,column=0,)
button_equal.grid(row=5,column=1)






#Must be in the end (Something of an update function)
root.mainloop()
