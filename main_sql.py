"""
=======================================================================================================
Суть:

=======================================================================================================
Всё о проектах:
 - Проект main_sql.py является главным и в нем находится всё. Будет переименован в main.py. Не удалять;
 - Проект v1.0.py существует для тестов. Будут появляться новые. Удалять можно;
 - Проект test.py существует для проверки модулей, функций и т.п. Удалять можно;
 - Данные для подключения к СУБД PostgreSQL находятся к проекте config_sql.py. Не удалять;
 - Проект HeartBeat пока не используется. Вероятно, будет удален;
 - Проект Outlook отвечает за рассылку писем в Outlook'e;
 - Проект tkinter_v - windows приложение
 - Проект GradientFrame отвечает за градиент
=======================================================================================================
Этап:
   1/10
=======================================================================================================
Задачи:
 - Необходимо решить проблему с отключением от БД. Блок finally не работает - система заполняется подключениями.
=======================================================================================================
"""

# Подключаем модули
import psycopg2
from config_sql import *

sql_text = 'SELECT as_name FROM as_name'  # По умолчанию будет


def postgres(sql_text):
    # Подключение к базе данных
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    try:
        # sql_text = '' #input("Введите SQL запрос на выборку данных в одну строку: \n")
        print()
        # Создание объекта курсор
        with connection.cursor() as cursor:
            # Пишем запрос сюда
            cursor.execute(
                f"""{sql_text}"""  # SELECT * FROM metric
            )
            records = cursor.fetchall()

            # Переписываем всё в список Python
            record = []
            for i in range(len(records)):
                record.extend(records[i])

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    # Закрытие подключения к СУБД
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

    return record


def main():
    print(postgres("SELECT as_name FROM as_name"))


if __name__ == '__main__':
    main()

    # Запуск сообщения в Outlook
    # Emailer(str(postgres.record), MailSubject, MailAdress, Copy_MailAdress)
    # input("Нажмите Enter, чтобы выйти")  # Существует, чтоб ехе сразу не закрывалось
