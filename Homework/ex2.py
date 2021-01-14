user_sec = int(input('Введите время в секундах: '))

hours = user_sec // 3600
minutes = (user_sec - hours * 3600) // 60
sec = user_sec - (hours * 3600 + minutes * 60)

print(f"Время: {hours} : {minutes} : {sec}")