from tkinter import *

from tkinter import ttk
from main_sql import postgres


class select():
    select_as = "SELECT as_name FROM as_name"
    select_metric1 = "SELECT metric_name FROM metric WHERE as_name_id = 1"
    select_metric2 = "SELECT metric_name FROM metric WHERE as_name_id = 2"
    select_metric3 = "SELECT metric_name FROM metric WHERE as_name_id = 3"
    select_metric4 = "SELECT metric_name FROM metric WHERE as_name_id = 4"
    select_metric5 = "SELECT metric_name FROM metric WHERE as_name_id = 5"


class MainWindow():
    def __init__(self):  # Создаю окно
        self.root = Tk()
        self.root.geometry("600x300")

    def get_menu(self):  # Создаю выпадающие списки

        list_as_name = postgres(select.select_as)
        variable = StringVar(self.root)
        variable.set(list_as_name[0])

        label1 = Label(self.root, text="Выбери АС: ")
        label1.pack()

        def checkcmbo(event):
            if variable.get() == postgres(select.select_as)[0]:
                list_metric = postgres(select.select_metric1)
                variable2 = StringVar(self.root)
                variable2.set(list_metric[0])
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                opt2 = OptionMenu(self.root, variable2, *list_metric)
                opt2.config(width=90, font=('Helvetica', 12))
                opt2.pack(side="top")


            elif variable.get() == postgres(select.select_as)[1]:
                list_metric = postgres(select.select_metric2)
                variable2 = StringVar(self.root)
                variable2.set(list_metric[0])
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                opt2 = OptionMenu(self.root, variable2, *list_metric)
                opt2.config(width=90, font=('Helvetica', 12))
                opt2.pack(side="top")

            elif variable.get() == postgres(select.select_as)[2]:
                list_metric = postgres(select.select_metric3)
                variable2 = StringVar(self.root)
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                opt2 = OptionMenu(self.root, variable2, *list_metric)

                opt2.config(width=90, font=('Helvetica', 12))
                opt2.pack(side="top")

            elif variable.get() == postgres(select.select_as)[3]:
                list_metric = postgres(select.select_metric4)
                variable2 = StringVar(self.root)
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                opt2 = OptionMenu(self.root, variable2, *list_metric)
                opt2.config(width=90, font=('Helvetica', 12))
                opt2.pack(side="top")

            elif variable.get() == postgres(select.select_as)[4]:
                list_metric = postgres(select.select_metric5)
                variable2 = StringVar(self.root)
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                opt2 = OptionMenu(self.root, variable2, *list_metric)
                opt2.config(width=90, font=('Helvetica', 12))
                opt2.pack(side="top")

        opt = OptionMenu(self.root, variable, *list_as_name, command=checkcmbo)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack(side="top")

        # self.combo.bind("<<ComboboxSelected>>", checkcmbo)

    def run(self):
        self.root.mainloop()




window = MainWindow()
get_menu_ = window.get_menu()
window.run()
