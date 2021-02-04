with open('new5.txt', 'w') as f:
    nums = input('Введите целые числа через пробел: ')
    f.write('Вы ввели: ' + nums + '\n')
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
print('Сумма чисел составила: ', sum_nums)
