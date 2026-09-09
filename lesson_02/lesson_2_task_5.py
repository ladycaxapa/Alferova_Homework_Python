def month_to_season(month_num):

    if month_num in [12, 1, 2]:
        return "Зима"

    elif month_num in [3, 4, 5]:
        return "Весна"

    elif month_num in [6, 7, 8]:
        return "Лето"

    elif month_num in [9, 10, 11]:
        return "Осень"

    else:
        return "Неверный номер месяца"


print(month_to_season(7))
