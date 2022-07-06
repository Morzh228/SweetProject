from main_sql import postgres
from Outlook import Emailer


class selects():
    select_as = "SELECT as_name FROM as_name"
    select_metric1 = "SELECT metric_name FROM metric WHERE as_name_id = 1"
    select_metric2 = "SELECT metric_name FROM metric WHERE as_name_id = 2"
    select_metric3 = "SELECT metric_name FROM metric WHERE as_name_id = 3"
    select_metric4 = "SELECT metric_name FROM metric WHERE as_name_id = 4"
    select_metric5 = "SELECT metric_name FROM metric WHERE as_name_id = 5"
    select_metric5_7 = "SELECT theme FROM theme_letter WHERE metric_id = 54"
    select_metric5_7_2 = "SELECT text_letter FROM text_letter WHERE metric_id = 54"


def metric(select):
    k = 0
    for i in postgres(select):
        k += 1
        print(f'{k}. {i}')
    metric_name = input("[INFO] < < < < < По какой метрике проблема? > > > > >\nВы ввели: ")
    if metric_name == "7":
        print("Горит, когда приближается крайний срок")
        incident = input("Введите инцидент: ")
        k = int(input("Введите количество часов до КС: "))
        if k > 8:
            print("Оповещать не надо")
            exit()
        elif 3 < k <= 8:
            k = 8
            Emailer(postgres(selects.select_metric5_7)[0].replace("#", f"{incident}"),
                    postgres(selects.select_metric5_7_2)[0].replace("#", f"{incident}"), 0, 0)
        elif 1 < k <= 3:
            k = 3
            Emailer(postgres(selects.select_metric5_7)[1].replace("#", f"{incident}"),
                    postgres(selects.select_metric5_7_2)[1].replace("#", f"{incident}"), 0, 0)
        elif 0.5 < k <= 1:
            k = 1
            Emailer(postgres(selects.select_metric5_7)[2].replace("#", f"{incident}"),
                    postgres(selects.select_metric5_7_2)[2].replace("#", f"{incident}"), 0, 0)
        else:
            print("Звони!")
        for i in postgres(selects.select_metric5_7):
            if i.find(f"{k}") == 47:
                print(i)


def as_():
    k = 0
    for i in postgres(selects.select_as):
        k += 1
        print(f'{k}. {i}')
    as_name = input("[INFO] < < < < < По какой АС проблема? > > > > >\nВы ввели: ")
    if as_name == "1":
        metric(selects.select_metric1)

    elif as_name == "2":
        metric(selects.select_metric2)

    elif as_name == "3":
        metric(selects.select_metric3)

    elif as_name == "4":
        metric(selects.select_metric4)

    elif as_name == "5":
        metric(selects.select_metric5)

    else:
        print("[INFO] Что-то пошло не так. Попробуйте снова!")
        exit()


def main():
    as_()


if __name__ == '__main__':
    main()
