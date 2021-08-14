from tkinter import *
from tkinter import Button

root = Tk()
root.title("Window page")


e = Entry(root,width=200,borderwidth =300)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)



def button_add():

    return


icon1 = Button(root,text="google chrome",padx=40,pady=40,command=button_add)

def myClick():
    return


myButton = Button(root,text= "Enter your stock Quote",command=myClick)

root.mainloop()