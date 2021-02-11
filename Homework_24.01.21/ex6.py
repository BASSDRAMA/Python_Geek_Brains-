def int_func(a):
    return a.title()

print(int_func('text'))

###

def another_int_func(*args):
    word = input('Введите текст: ')
    print(word.title())
    return

another_int_func()

###

def another_galaxy_int_func(b):
    return int_func(b)

print(another_galaxy_int_func('jtututu tututut tutut'))


