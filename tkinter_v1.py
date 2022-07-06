from tkinter import *
from Outlook import *



root = Tk()
root.title("Outlook")
root.geometry("400x250")

MailSubject = Label(root, text = "Введите тему письма: ").place(x = 30, y = 10)
e1 = Entry(root).place(x = 30, y = 30)


text_info = Label(root, text="Нажмите кнопку, чтоб сформировать письмо").place(x=30, y=50)
b = Button(root, text='кнопка', command=Emailer).place(x=30, y=70)
root.mainloop()
