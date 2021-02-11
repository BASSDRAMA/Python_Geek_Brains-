def div(*args):

    try:
        n1 = int(input('Введите первое число: '))
        n2 = int(input('Введите второе число: '))
        result = n1 / n2

    except ValueError:
        print('Это не числа')

    except ZeroDivisionError:
        print('На ноль делить нельзя')

    else:
        print(f'Результат составил: {result}')

div()