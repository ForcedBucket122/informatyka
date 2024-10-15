import tkinter as tk
from tkinter import ttk

def przelicz():
    try:
        pln = float(entry_pln.get())
        kurs = float(entry_kurs.get())
        eur = pln / kurs
        wynik_label.config(text=f"{eur:.2f} EUR")
    except ValueError:
        wynik_label.config(text="Błąd: Wprowadź poprawne liczby")

# Tworzenie głównego okna
root = tk.Tk()
root.title("Kalkulator PLN na EUR")

# Etykiety i pola wejściowe
label_pln = ttk.Label(root, text="Kwota w PLN:")
label_pln.grid(column=0, row=0, padx=10, pady=10)

entry_pln = ttk.Entry(root)
entry_pln.grid(column=1, row=0, padx=10, pady=10)

label_kurs = ttk.Label(root, text="Kurs wymiany (PLN/EUR):")
label_kurs.grid(column=0, row=1, padx=10, pady=10)

entry_kurs = ttk.Entry(root)
entry_kurs.grid(column=1, row=1, padx=10, pady=10)

# Przycisk do przeliczania
przelicz_button = ttk.Button(root, text="Przelicz", command=przelicz)
przelicz_button.grid(column=0, row=2, columnspan=2, pady=10)

# Etykieta do wyświetlania wyniku
wynik_label = ttk.Label(root, text="Wynik w EUR:")
wynik_label.grid(column=0, row=3, columnspan=2, pady=10)

# Uruchomienie aplikacji
root.mainloop()
