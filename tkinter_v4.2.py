from tkinter import *
from tkinter import ttk
from main_sql import postgres

root = Tk()
root.geometry("600x300")


select = "SELECT as_name FROM as_name"
list_as_name = postgres(select)
combo = ttk.Combobox(root, values=list_as_name, state="readonly")
combo.pack()

def checkcmbo(event):
    if combo.get() == postgres(select)[0]:
        print(1)
    elif combo.get() == postgres(select)[1]:
        print(2)
    elif combo.get() == postgres(select)[2]:
        print(3)
    elif combo.get() == postgres(select)[3]:
        print(4)
    elif combo.get() == postgres(select)[4]:
        print(5)

combo.bind("<<ComboboxSelected>>", checkcmbo)
root.mainloop()
