from tkinter import *
from Outlook import *


def show_message():
    MailSubject = message1.get()  # Тема письма
    MailInput = message2.get()  # Текст письма
    MailAdress = message3.get()  # Адресс получателя
    Copy_MailAdress = message4.get()  # Копия
    Emailer(text=MailInput, subject=MailSubject, recipient=MailAdress, copy_recipient=Copy_MailAdress)


root = Tk()
root.title("Outlook")
root.geometry("600x300")

message1, message2, message3, message4 = StringVar(), StringVar(), StringVar(), StringVar()
# Тема письма
MailSubject1 = Label(root, text="Введите тему письма: ").place(x=100, y=20, anchor="c")
MailSubject_entry1 = Entry(textvariable=message1).place(x=300, y=20, anchor="c")
# Текст письма
MailSubject2 = Label(root, text="Введите текст письма: ").place(x=100, y=50, anchor="c")
MailSubject_entry2 = Entry(textvariable=message2).place(x=300, y=50, anchor="c")
# Адресс получателя
MailSubject3 = Label(root, text="Введите адрес получателя: ").place(x=100, y=80, anchor="c")
MailSubject_entry3 = Entry(textvariable=message3).place(x=300, y=80, anchor="c")
# Копия
MailSubject4 = Label(root, text="Введите копию: ").place(x=100, y=110, anchor="c")
MailSubject_entry4 = Entry(textvariable=message4).place(x=300, y=110, anchor="c")
# Кнопка
button = Button(text="Сформировать письмо", command=show_message).place(relx=.5, rely=.6, anchor="c")

# Создать письмо
# text_info = Label(root, text="Нажмите кнопку, чтоб сформировать письмо").place(x=30, y=50)
# b = Button(root, text='кнопка', command=Emailer).place(x=30, y=70)
root.mainloop()
