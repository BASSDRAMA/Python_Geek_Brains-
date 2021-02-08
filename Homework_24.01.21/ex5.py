def sum6ex():
    final_res = 0
    ex = False

    while ex == False:
        nums = input('Введите число или нажмите Q для выхода: ').split()
        result1 = 0

        for el in range(len(nums)):
            if nums[el] =='q' or nums[el] == 'Q':
                ex = True
                break

            else:
                result1 = result1 + int(nums[el])

        final_res = int(final_res) + result1
        print(f'Ваш текущий результат: {result1}')
    print(f'Итоговый результат: {final_res}')

sum6ex()


