filename = 'text.txt'

with open(filename, 'w') as f_obj:
    while True:
        line = input('Введите данные: ')
        if line == '':
            break
        f_obj.write(line + '\n')
