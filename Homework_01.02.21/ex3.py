with open('sal.txt', encoding='utf-8') as f:
    lines = f.readlines()

salaries = []

for line in lines:
    name, salary = line.split(' - ')
    salaries.append(float(salary))
    if float(salary) < 20000:
        print(line, end='')
print('\n Средняя зарплата составляет: ', sum(salaries) / len(salaries))