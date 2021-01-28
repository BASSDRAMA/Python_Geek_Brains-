import random

old_list = []
i = 0
while i < 15:
    a = random.randrange(1, 201)
    old_list.append(a)
    i += 1

new_list = [x for el, x in enumerate(old_list) if x > old_list[el - 1] and el !=0]

print(new_list)

