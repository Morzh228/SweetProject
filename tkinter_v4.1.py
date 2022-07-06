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
        label1 = Label(self.root, text="Выбери АС: ")
        label1.pack()

        self.combo = ttk.Combobox(self.root, values=list_as_name, state="readonly")
        self.combo.pack()

        def checkcmbo(event):
            if self.combo.get() == postgres(select.select_as)[0]:
                list_as_name = postgres(select.select_metric1)

                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                self.combo = ttk.Combobox(self.root, values=list_as_name, state="readonly")
                self.combo.pack()

            elif self.combo.get() == postgres(select.select_as)[1]:
                list_as_name = postgres(select.select_metric2)

                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                self.combo = ttk.Combobox(self.root, values=list_as_name, state="readonly")
                self.combo.pack()

            elif self.combo.get() == postgres(select.select_as)[2]:
                list_as_name = postgres(select.select_metric3)

                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                self.combo = ttk.Combobox(self.root, values=list_as_name, state="readonly")
                self.combo.pack()

            elif self.combo.get() == postgres(select.select_as)[3]:
                list_as_name = postgres(select.select_metric4)

                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                self.combo = ttk.Combobox(self.root, values=list_as_name, state="readonly")
                self.combo.pack()

            elif self.combo.get() == postgres(select.select_as)[4]:
                list_as_name = postgres(select.select_metric5)

                label2 = Label(self.root, text="Выбери метрику: ")
                label2.pack()

                self.combo = ttk.Combobox(self.root, values=list_as_name, state="readonly")
                self.combo.pack()



        self.combo.bind("<<ComboboxSelected>>", checkcmbo)


    def run(self):
        self.root.mainloop()



window = MainWindow()
window.get_menu()
window.run()

