from tkinter import *
def wybor( ):
    wybrano="Wybrano opcję "+ str()
glowna=Tk()

glowna.title("RadioButton")
zmienna=IntVar()
zmienna1=IntVar()
zmienna2=IntVar()

rb1=Radiobutton(glowna, text="Wybor 1", variable=zmienna, value=1, command=wybor())
rb1=Radiobutton(glowna, text="Wybor 2", variable=zmienna, value=2, command=wybor())
rb1=Radiobutton(glowna, text="Wybor 3", variable=zmienna, value=3, command=wybor())