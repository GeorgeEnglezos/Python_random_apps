from tkinter import * #The needed library

#set the root widget
root=Tk() 

#Text Input
e=Entry(root,width=50,bg="black",fg="white",borderwidth=10)
#adding the button to the window
e.pack()
e.insert(1,"Enter Your Name:")

#Label
buttonLabel=Label(root,text="")
buttonLabel.pack()

#Creating buttons
def myClick():
    buttonLabel=Label(root,text=e.get())
    buttonLabel.pack()

myButton=Button(root,text="print text",command=myClick)
myButton.pack()





#Must be in the end (Something of an update function)
root.mainloop()
