from tkinter import * #The needed library

#set the root widget
root=Tk() 

#making the Labels and adding them to the window grid
myLabel1=Label(root, text="Hello World").grid(row=0,column=0)
myLabel2=Label(root, text="My name is George").grid(row=1,column=0)

#Must be in the end (Something of an update function)
root.mainloop()
