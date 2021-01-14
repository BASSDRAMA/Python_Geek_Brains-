proc = float(input('Введите выручку: '))
outlay = float(input('Введите издержки: '))
rent = (proc - outlay) / proc

if proc > outlay:
    print('Ваша фирма закончила год с прибылью')
    print('Рентабельность выручки составляет: ', rent)

elif proc < outlay:
    print('Тяжелый год - тяжелые последствия, Вы работаете в убыток')

elif proc == outlay:
    print('Прибыль составляет 0. Как и расходы. Хотя бы не ушли в минус, уже хорошо')

staff_amount = int(input('Введите количество сотрудников, чтобы узнать прибыль фирмы в расчете на каждого из них'))
income_per_worker = (proc - outlay) / staff_amount
print('Прибыль на каждого сотрудника составила ', income_per_worker)