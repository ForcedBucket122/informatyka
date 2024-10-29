from tkinter import *
from tkinter.ttk import Combobox

def przelicz():
    kwota = float(entry_kwota.get())
    waluta_z = waluta_wej.get()
    waluta_na = waluta_wyj.get()

    kursy = {
        'PLN': {'EUR': 4.30, 'USD': 3.94, 'CHF': 4.61, 'GBP': 5.18},
        'EUR': {'PLN': 4.30, 'USD': 1.14, 'CHF': 1.07, 'GBP': 0.86},
        'USD': {'PLN': 3.94, 'EUR': 0.88, 'CHF': 0.94, 'GBP': 0.76},
        'CHF': {'PLN': 4.61, 'EUR': 0.93, 'USD': 1.06, 'GBP': 0.81},
        'GBP': {'PLN': 5.18, 'EUR': 1.16, 'USD': 1.31, 'CHF': 1.23}
    }

    if waluta_z == 'PLN':
        wynik = kwota / kursy[waluta_z][waluta_na]
    else:
        wynik = kwota * kursy[waluta_z][waluta_na]

    label_wynik.config(text=f'{wynik:.2f} {waluta_na}')

glowne_okno = Tk()
glowne_okno.title("Przelicznik walut")
glowne_okno.geometry("500x300")

label_kwota = Label(glowne_okno, text="Kwota:")
label_kwota.pack()
entry_kwota = Entry(glowne_okno)
entry_kwota.pack()

label_waluta_wej = Label(glowne_okno, text="Z waluty:")
label_waluta_wej.pack()
waluta_wej = Combobox(glowne_okno, values=['PLN', 'EUR', 'USD', 'CHF', 'GBP'], state='readonly')
waluta_wej.set('PLN')
waluta_wej.pack()

label_waluta_wyj = Label(glowne_okno, text="Na walutę:")
label_waluta_wyj.pack()
waluta_wyj = Combobox(glowne_okno, values=['EUR', 'USD', 'CHF', 'GBP'], state='readonly')
waluta_wyj.set('EUR')
waluta_wyj.pack()

button_przelicz = Button(glowne_okno, text="Przelicz", command=przelicz)
button_przelicz.pack()

label_wynik = Label(glowne_okno, text="")
label_wynik.pack()

glowne_okno.mainloop()
