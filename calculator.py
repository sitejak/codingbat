from tkinter import *
root = Tk()
root.title("Simple Calculator")

e = Entry(root,width=35,borderwidth =5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#e.insert(0,"Enter our Name:")
def button_add():
    return

button1 = Button(root,text="1",padx=40,pady=40,command=button_add)
button2 = Button(root,text="2",padx=40,pady=40,command=button_add)
button3 = Button(root,text="3",padx=40,pady=40,command=button_add)
button4 = Button(root,text="4",padx=40,pady=40,command=button_add)
button5 = Button(root,text="5",padx=40,pady=40,command=button_add)
button6 = Button(root,text="6",padx=40,pady=40,command=button_add)
button7 = Button(root,text="7",padx=40,pady=40,command=button_add)
button8 = Button(root,text="8",padx=40,pady=40,command=button_add)
button9 = Button(root,text="9",padx=40,pady=40,command=button_add)
button0 = Button(root,text="0",padx=40,pady=40,command=button_add)

button1.grid(row= 3, column=0)
button2.grid(row= 3, column=1)
button3.grid(row= 3, column=2)
button4.grid(row= 2, column=0)
button5.grid(row= 2, column=1)
button6.grid(row= 2, column=2)
button7.grid(row= 1, column=0)
button8.grid(row= 1, column=1)
button9.grid(row= 1, column=2)
button0.grid(row= 4, column=0)

def myClick():
    return


myButton = Button(root,text= "Enter your stock Quote",command=myClick)



root.mainloop()