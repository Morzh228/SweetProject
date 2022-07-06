from tkinter import *
from Outlook import *
from GradientFrame import GradientFrame
from main_sql import *


def show_message():
    MailSubject = message1.get()  # Тема письма
    MailInput = message2.get()  # Текст письма
    MailAdress = message3.get()  # Адресс получателя
    Copy_MailAdress = message4.get()  # Копия
    Emailer(text=MailInput, subject=MailSubject, recipient=MailAdress, copy_recipient=Copy_MailAdress)


def application():
    # Внешний вид, размер, название
    root = Tk()
    root.title("Outlook")
    root.geometry("600x300")
    gf = GradientFrame(root, colors=("yellow", "black"), width=800, height=600)
    gf.config(direction=gf.top2bottom)

    # Создание полей
    global message1, message2, message3, message4
    message1, message2, message3, message4 = StringVar(), StringVar(), StringVar(), StringVar()

    # Тема письма
    MailSubject1 = Label(root, text="Введите тему письма: ").place(x=100, y=50, anchor="c")
    MailSubject_entry1 = Entry(textvariable=message1).place(x=300, y=50, anchor="c")

    # Текст письма
    MailSubject2 = Label(root, text="Введите текст письма: ").place(x=100, y=80, anchor="c")
    MailSubject_entry2 = Entry(textvariable=message2).place(x=300, y=80, anchor="c")

    # Адресс получателя
    MailSubject3 = Label(root, text="Введите адрес получателя: ").place(x=100, y=110, anchor="c")
    MailSubject_entry3 = Entry(textvariable=message3).place(x=300, y=110, anchor="c")

    # Копия
    MailSubject4 = Label(root, text="Введите копию: ").place(x=100, y=140, anchor="c")
    MailSubject_entry4 = Entry(textvariable=message4).place(x=300, y=140, anchor="c")

    #Выпадающий список АС
    list_as_name = postgres("SELECT as_name FROM as_name")
    variable = StringVar(root)
    variable.set(list_as_name[0])

    opt = OptionMenu(root, variable, *list_as_name)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack(side="top")



    # Выпадающий список метрик
    list_as_name = postgres("SELECT metric_name FROM metric")
    variable = StringVar(root)
    variable.set(list_as_name[0])

    opt = OptionMenu(root, variable, *list_as_name)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack(side="top")


    gf.pack()
    # Кнопка
    button = Button(text="Сформировать письмо", command=show_message).place(relx=.5, rely=.7, anchor="c")

    root.mainloop()  # Задержка экрана


def main():
    application()
    print(postgres("SELECT as_name FROM as_name"))


if __name__ == '__main__':
    main()
