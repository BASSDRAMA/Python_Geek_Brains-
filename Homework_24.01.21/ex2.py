def user_data_pick(**kwargs):
    return kwargs

print(user_data_pick(
    name=(input('Введите Имя: ').capitalize()),
    surname=(input('Введите Фамилию: ').capitalize()),
    bday_year=(input('Введите год рождения: ')),
    city=str(input('Укажите ваш город: ').capitalize()),
    email=input('Укажите адрес электронной почты '),
    contact_num=(input('Введите ваш номер телефона без пробелов и кода страны (8/+7) : '))))











    



