import tkinter as tk
from tkinter import messagebox

def calculate_results():
    score = 0
    if var1.get() == 1:
        score += 1
    if var2.get() == 1:
        score += 1
    if var3.get() == 1:
        score += 1
    messagebox.showinfo("Wyniki", f"Twój wynik to: {score}/3")

def check_answers():
    # Reset colors
    cb1.config(bg="SystemButtonFace")
    cb2.config(bg="SystemButtonFace")
    cb3.config(bg="SystemButtonFace")
    cb4.config(bg="SystemButtonFace")
    cb5.config(bg="SystemButtonFace")
    cb6.config(bg="SystemButtonFace")
    cb7.config(bg="SystemButtonFace")
    cb8.config(bg="SystemButtonFace")
    cb9.config(bg="SystemButtonFace")
    cb10.config(bg="SystemButtonFace")
    cb11.config(bg="SystemButtonFace")
    cb12.config(bg="SystemButtonFace")

    # Check answers
    if var1.get() == 1:
        cb1.config(bg="green")
    elif var1.get() != 0:
        cb1.config(bg="red")

    if var2.get() == 1:
        cb8.config(bg="green")
    elif var2.get() != 0:
        cb8.config(bg="red")

    if var3.get() == 1:
        cb9.config(bg="green")
    elif var3.get() != 0:
        cb9.config(bg="red")

    if var4.get() == 1:
        cb10.config(bg="green")
    elif var4.get() != 0:
        cb10.config(bg="red")

    if var5.get() == 1:
        cb11.config(bg="green")
    elif var5.get() != 0:
        cb11.config(bg="red")

    if var6.get() == 1:
        cb12.config(bg="green")
    elif var6.get() != 0:
        cb12.config(bg="red")

root = tk.Tk()
root.title("Quiz")

# Pytanie 1
tk.Label(root, text="Ktory jezyk jest skryptowy?").pack()
var1 = tk.IntVar()
cb1 = tk.Radiobutton(root, text="JavaScript", variable=var1, value=1)
cb2 = tk.Radiobutton(root, text="Python", variable=var1, value=2)
cb3 = tk.Radiobutton(root, text="Java", variable=var1, value=3)
cb4 = tk.Radiobutton(root, text="C++", variable=var1, value=4)
cb1.pack()
cb2.pack()
cb3.pack()
cb4.pack()

# Pytanie 2
tk.Label(root, text="Ktory jezyk jest najprostrzy").pack()
var2 = tk.IntVar()
cb5 = tk.Radiobutton(root, text="JavaScript", variable=var2, value=4)
cb6 = tk.Radiobutton(root, text="Java", variable=var2, value=3)
cb7 = tk.Radiobutton(root, text="C++", variable=var2, value=2)
cb8 = tk.Radiobutton(root, text="Python", variable=var2, value=1)
cb5.pack()
cb6.pack()
cb7.pack()
cb8.pack()

# Pytanie 3
tk.Label(root, text="Ktory jezyk jest najpopularniejszy?").pack()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
cb9 = tk.Checkbutton(root, text="JavaScript", variable=var3, onvalue=1, offvalue=0)
cb10 = tk.Checkbutton(root, text="Python", variable=var4, onvalue=1, offvalue=0)
cb11 = tk.Checkbutton(root, text="Java", variable=var5, onvalue=1, offvalue=0)
cb12 = tk.Checkbutton(root, text="C++", variable=var6, onvalue=1, offvalue=0)
cb9.pack()
cb10.pack()
cb11.pack()
cb12.pack()

# Przyciski
tk.Button(root, text="Oblicz wyniki", command=calculate_results).pack()
tk.Button(root, text="Sprawdź", command=check_answers).pack()

root.mainloop()
