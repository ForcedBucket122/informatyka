from tkinter import *
def press():
    pobierz=wpisz.get()
    tekstowy["text"]=pobierz
def press2():
    # wpisz.insert(0,"Tak wpisujemy tekst")
    wpisz.delete(0,4)
glowna= Tk()
glowna.geometry("600x400")
glowna.title("Widget entry")
wpisz = Entry(glowna,width="20",text="Jestem tu")
przycisk = Button(glowna,text="OK",command=press)
przycisk2=Button(glowna,text="Wstaw",command=press2)
tekstowy = Label(glowna,width=20)
wpisz.pack()
tekstowy.pack()
przycisk.pack()
przycisk2.pack()
glowna.mainloop()
