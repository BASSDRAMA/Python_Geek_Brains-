elements_counter = int(input('Введите количество элементов в списке: '))
user_list = []

i = 0
el_number = 0

while i < elements_counter:
    user_list.append(input('Введите следующий элемент списка: '))
    i += 1

for elements in range(int(len(user_list) / 2)):
    user_list[el_number], user_list[el_number + 1] = user_list[el_number + 1], user_list[el_number]
    el_number += 2

print(user_list)