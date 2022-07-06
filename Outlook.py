import win32com.client as win32
import os

MailSubject = "Тема письма"  # input('Введите тему письма: \n')  # Тема письма
MailInput = "Текст письма"  # input('Введите текст письма: \n') # Текст письма
MailAdress = "alexeydata@bk.ru"  # input('Введите адрес получателя: \n') # Адресс получателя
Copy_MailAdress = "alexeydata@bk.ru"  # input('Введите адрес копии: \n') # Копия


def Emailer(subject=MailSubject, text=MailInput, recipient=MailAdress, copy_recipient=Copy_MailAdress):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.CC = copy_recipient
    mail.Subject = subject
    mail.HtmlBody = text

    # Прикрепить файл
    # attachment1 = os.getcwd() + "\\test.py"  # os.getcwd() - текущий каталог
    # mail.Attachments.Add(attachment1)  # Прикрепляем файл

    # Открыть окно отправки Outlook
    mail.Display(True)

# Emailer(MailInput, MailSubject, MailAdress, Copy_MailAdress)  # that open a new outlook mail even outlook closed.
