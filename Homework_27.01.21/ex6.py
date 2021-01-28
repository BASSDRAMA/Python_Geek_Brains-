from itertools import count, cycle
i = 0

for num in count(int(input('Введите стартовове число: '))):
    if i > 10:
        break
    else:
        print(num)
        i += 1


