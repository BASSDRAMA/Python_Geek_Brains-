from itertools import cycle

bart_simpson_quots = ['I will not xerox my butt', 'I will finish what I sta']
stop = ''

while stop != 'q':
    for el in cycle(bart_simpson_quots):
        print(el)
        stop = input()



