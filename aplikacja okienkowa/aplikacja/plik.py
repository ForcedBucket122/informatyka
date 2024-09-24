from tkinter import *
def press():
    etykieta.config(text="inny")
    etykieta["bg"]="green"
glowna=Tk()
glowna.geometry("600x400")
zmienny_tekst=StringVar()
etykieta=Label(glowna,textvariable=zmienny_tekst,bg="red",width="20",height="10",fg="yellow",justify=CENTER)
przycisk = Button(glowna,text="OK",command=press)
zmienny_tekst.set("Ustaw tekst w etykiecie")
etykieta.pack(side=LEFT)
przycisk.pack(side=LEFT)
glowna.mainloop()