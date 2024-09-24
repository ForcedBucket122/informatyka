from tkinter import *

def press():
    moj_tekst.config(text="Do widzenia",bg="blue")

root = Tk()
root.geometry("400x300")
moj_tekst = Label(root,text="Dzień dobry",bg="yellow")
moj_przycisk = Button(root,text="ok",width="200",command=press)
moj_tekst.pack(side=RIGHT)
moj_przycisk.pack()

root.mainloop()