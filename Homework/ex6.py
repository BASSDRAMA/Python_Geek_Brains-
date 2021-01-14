first_day_dist = float(input('Укажите результат первого дня в километрах: '))
aim_dist = float(input('Укажите желаемый результат в километрах: '))

final_day = 1
final_dist = first_day_dist

while final_dist < aim_dist:
    first_day_dist = first_day_dist + first_day_dist * 0.1
    final_day += 1
    final_dist = final_dist + first_day_dist

print(f"Вы достигнете желаемого результата на %d день" %final_day)