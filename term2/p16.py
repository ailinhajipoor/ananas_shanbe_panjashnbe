from tkinter import *
from random import randint
def fall():

    a = ["1.gif", "2.gif", "3.gif", "4.gif"]
    num = randint(0, 3)
    logo1=PhotoImage(file=a[num])
    l1=Label(root,image=logo1)
    l1.grid(row=1,column=0)
root=Tk()

logo=PhotoImage(file="click.png")

b=Button(root,image=logo,command=fall)
b.grid(row=1,column=0)


root.mainloop()