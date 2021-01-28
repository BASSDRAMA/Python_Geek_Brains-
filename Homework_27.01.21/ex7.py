from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

x = 0
for i in fibo_gen():
    if x < 16:
        print(i)
        x += 1
    else:
        break


