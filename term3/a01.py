from tkinter import *
root=Tk()
root.configure(bg="orange")
root.geometry("400x300")
l1=Label(root,text="type your name :",bg="orange")#print
l1.pack()
e1=Entry(root)#input
e1.pack()

root.mainloop()