filename = 'new2.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()
print('Всего строк: ', len(lines))
for num_line, line in enumerate(lines, start=1):
    print(f'В {num_line} строке {len(line.split())} слов')
