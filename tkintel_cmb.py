from tkinter import *
from tkinter import ttk
from main_sql import postgres
from Outlook import Emailer
from tkinter import messagebox

### Внешняя составляющая текста
text_size = '12'  # размер
test_style = 'Verdana'  # стиль текста
content = 'normal'  # жирность
width_ = 40


class select():
    select_as = "SELECT as_name FROM as_name"
    select_metric1 = "SELECT metric_name FROM metric WHERE as_name_id = 1"
    select_metric2 = "SELECT metric_name FROM metric WHERE as_name_id = 2"
    select_metric3 = "SELECT metric_name FROM metric WHERE as_name_id = 3"
    select_metric4 = "SELECT metric_name FROM metric WHERE as_name_id = 4"
    select_metric5 = "SELECT metric_name FROM metric WHERE as_name_id = 5"
    select_metric5_7 = "SELECT theme FROM theme_letter WHERE metric_id = 54"
    select_metric5_7_2 = "SELECT text_letter FROM text_letter WHERE metric_id = 54"


class MainWindow():
    def __init__(self):  # Создаю окно
        self.root = Tk()
        self.root.geometry("500x650")
        # self.root["bg"] = "gray50"

    def get_menu(self):  # Создаю выпадающие списки
        list_as_name = postgres(select.select_as)
        list_metric = []

        def checkcmb_as(event):
            # Если выбрана первая АСка
            if cmb1.get() == postgres(select.select_as)[0]:
                # Вывод метрик:
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.grid(row=2, column=0, sticky='w', padx=10, pady=10)
                list_metric = []
                list_metric.extend(postgres(select.select_metric1))
                cmb2 = ttk.Combobox(self.root, values=list_metric, state="readonly", width=width_,
                                    font=f"{test_style} {text_size} {content}")
                cmb2.grid(row=3, column=0, sticky='w', padx=10, pady=10)

            # Если выбрана вторая АСка
            elif cmb1.get() == postgres(select.select_as)[1]:
                # Вывод метрик:
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.grid(row=2, column=0, sticky='w', padx=10, pady=10)
                list_metric = []
                list_metric.extend(postgres(select.select_metric2))
                cmb2 = ttk.Combobox(self.root, values=list_metric, state="readonly", width=width_,
                                    font=f"{test_style} {text_size} {content}")
                cmb2.grid(row=3, column=0, sticky='w', padx=10, pady=10)

            # Если выбрана третья АСка
            elif cmb1.get() == postgres(select.select_as)[2]:
                # Вывод метрик:
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.grid(row=2, column=0, sticky='w', padx=10, pady=10)
                list_metric = []
                list_metric.extend(postgres(select.select_metric3))
                cmb2 = ttk.Combobox(self.root, values=list_metric, state="readonly", width=width_,
                                    font=f"{test_style} {text_size} {content}")
                cmb2.grid(row=3, column=0, sticky='w', padx=10, pady=10)

            # Если выбрана четвертая АСка
            elif cmb1.get() == postgres(select.select_as)[3]:
                # Вывод метрик:
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.grid(row=2, column=0, sticky='w', padx=10, pady=10)
                list_metric = []
                list_metric.extend(postgres(select.select_metric4))
                cmb2 = ttk.Combobox(self.root, values=list_metric, state="readonly", width=width_,
                                    font=f"{test_style} {text_size} {content}")
                cmb2.grid(row=3, column=0, sticky='w', padx=10, pady=10)

            # Если выбрана пятая АСка
            elif cmb1.get() == postgres(select.select_as)[4]:

                def checkcmb_metric(event):
                    if cmb2.get() == list_metric[0]:
                        print(1)
                    elif cmb2.get() == list_metric[1]:
                        print(2)
                    elif cmb2.get() == list_metric[2]:
                        print(3)
                    elif cmb2.get() == list_metric[3]:
                        print(4)
                    elif cmb2.get() == list_metric[4]:
                        print(5)
                    elif cmb2.get() == list_metric[5]:
                        print(6)
                    elif cmb2.get() == list_metric[6]:
                        IMTS, watch = StringVar(), StringVar()

                        def btn_play():
                            k = float(watch.get())
                            if k > 8:
                                messagebox.showinfo("Внимание!", "Оповещать не надо")
                            elif 3 < k <= 8:
                                Emailer(postgres(select.select_metric5_7)[0].replace("#", f"{IMTS.get()}"),
                                        postgres(select.select_metric5_7_2)[0].replace("#", f"{IMTS.get()}"), 0, 0)
                            elif 1 < k <= 3:
                                Emailer(postgres(select.select_metric5_7)[1].replace("#", f"{IMTS.get()}"),
                                        postgres(select.select_metric5_7_2)[1].replace("#", f"{IMTS.get()}"), 0, 0)
                            elif 0.5 < k <= 1:
                                Emailer(postgres(select.select_metric5_7)[2].replace("#", f"{IMTS.get()}"),
                                        postgres(select.select_metric5_7_2)[2].replace("#", f"{IMTS.get()}"), 0, 0)
                            else:
                                messagebox.showerror("Внимание!", "Звони исполнителю.")
                            exit()
                            # Emailer()

                        label2 = Label(self.root, text="Описание метрики: горит, когда приближается крайний срок")
                        label2.grid(row=4, column=0, sticky='w', padx=10, pady=10)
                        label3 = Label(self.root, text="Введите номер инцидента: ")
                        label3.grid(row=5, column=0, sticky='w', padx=10, pady=10)
                        IMTS = Entry(textvariable=IMTS, width=width_)
                        IMTS.grid(row=6, column=0, sticky='w', padx=10, pady=10)
                        label4 = Label(self.root, text="Введите количество часов до КС: ")
                        label4.grid(row=7, column=0, sticky='w', padx=10, pady=10)
                        watch = Entry(textvariable=watch, width=width_)
                        watch.grid(row=8, column=0, sticky='w', padx=10, pady=10)
                        btn = Button(text='Сформировать письмо', width=30, command=btn_play)
                        btn.grid(row=9, column=0, sticky='w', padx=10, pady=10)
                    elif cmb2.get() == list_metric[7]:
                        print(8)
                    elif cmb2.get() == list_metric[8]:
                        print(9)
                    elif cmb2.get() == list_metric[9]:
                        print(10)
                    elif cmb2.get() == list_metric[10]:
                        print(11)
                    elif cmb2.get() == list_metric[11]:
                        print(12)
                    elif cmb2.get() == list_metric[12]:
                        print(13)
                    elif cmb2.get() == list_metric[13]:
                        print(14)
                    elif cmb2.get() == list_metric[14]:
                        print(15)
                    elif cmb2.get() == list_metric[15]:
                        print(16)
                    elif cmb2.get() == list_metric[16]:
                        print(17)
                    elif cmb2.get() == list_metric[17]:
                        print(18)
                    elif cmb2.get() == list_metric[18]:
                        print(19)
                    elif cmb2.get() == list_metric[19]:
                        print(20)

                # Вывод метрик:
                label2 = Label(self.root, text="Выбери метрику: ")
                label2.grid(row=2, column=0, sticky='w', padx=10, pady=10)
                list_metric = []
                list_metric.extend(postgres(select.select_metric5))
                cmb2 = ttk.Combobox(self.root, values=list_metric, state="readonly", width=width_,
                                    font=f"{test_style} {text_size} {content}")
                cmb2.bind("<<ComboboxSelected>>", checkcmb_metric)
                cmb2.grid(row=3, column=0, sticky='w', padx=10, pady=10)

        # Выбор АСок
        label1 = Label(self.root, text="Выбери АС: ")
        label1.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        cmb1 = ttk.Combobox(self.root, values=list_as_name, state="readonly", width=width_,
                            font=f"{test_style} {text_size} {content}")
        cmb1.bind("<<ComboboxSelected>>", checkcmb_as)
        cmb1.grid(row=1, column=0, sticky='w', padx=10, pady=10)

    def run(self):
        self.root.mainloop()


window = MainWindow()
window.get_menu()

window.run()


