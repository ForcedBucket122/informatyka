import tkinter as tk
from tkinter import filedialog, messagebox

current_file_path = None

def open_file():
    global current_file_path
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        current_file_path = file_path
        root.title(f"Edytor - {file_path}")

def save_file():
    global current_file_path
    if current_file_path:
        with open(current_file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Zapisano", f"Plik został zapisany: {current_file_path}")
    else:
        save_as_file()

def save_as_file():
    global current_file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        current_file_path = file_path
        root.title(f"Edytor - {file_path}")

root = tk.Tk()
root.title("Edytor")
root.geometry("600x400")

tk.Button(root, text="Open", command=open_file).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(root, text="Save", command=save_file).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(root, text="Save as", command=save_as_file).pack(side=tk.LEFT, padx=10, pady=10)

text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

root.mainloop()
