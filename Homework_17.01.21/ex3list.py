seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']

month = int(input('Введите номер месяца: '))

try:
    if month > 12 or month < 1:
        print('Месяца под таким номером не существует, попробуйте еще раз')
finally:

    month = int(input('Введите номер месяца: '))

    if month == 1 or month == 2 or month == 12:
        print(seasons_list[0])

    elif month == 3 or month == 4 or month == 5:
        print(seasons_list[1])

    elif month == 6 or month == 7 or month == 8:
        print(seasons_list[2])

    elif month == 9 or month == 10 or month == 11:
        print(seasons_list[3])
