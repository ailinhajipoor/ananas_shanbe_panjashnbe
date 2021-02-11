from tkinter import *
from PIL import Image, ImageTk
#from playsound import playsound


def play():
    window = Toplevel()
    window.attributes('-fullscreen', True)
    img = ImageTk.PhotoImage(Image.open("click.png"))
    label = Label(window, image=img).pack()
    #playsound("song.mp3", block=False)
    label.draw()


buttonWindow = Tk()
b = Button(buttonWindow, text="Press Button", command=play)
b.pack()
buttonWindow.mainloop()
