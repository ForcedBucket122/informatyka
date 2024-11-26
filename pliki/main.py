from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename


def wybor():
    nazwapliku = askopenfilename()
    file = open(nazwapliku, "r", encoding="UTF-8")
    print(nazwapliku)
def kasuj():
    wyswietl=tekstowy.delete(10.30,1.6)
    print(wyswietl)
glowna=Tk()
tekstowy = Text(glowna,width=40)
przycisk = Button(glowna,text="OK", command=wybor())
przycisk2 = Button(glowna, text="kasuj",command=kasuj())
tekstowy.insert(INSERT, "Pierwotny tekst")
tekstowy.tag_add("MojTag1",1.3,1.6)
tekstowy.pack()
przycisk.pack()
przycisk2.pack()
glowna.mainloop()