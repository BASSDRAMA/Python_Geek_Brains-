# я не понял, что значит "получить результат вычисления", тк вроде как любые арифметические операции -
# это вычисление, поэтому у меня будет сложение :))000))0000))00))))

from functools import reduce
def wow_its_a_func(n1, n2):
    return n1 + n2

new_list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(wow_its_a_func, new_list))
