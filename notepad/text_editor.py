import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

text_area = tk.Text(root, font=("Arial", 12))
text_area.pack(fill="both", expand=True)

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()