import random

old_list = []
i = 0

while i < 15:
    a = random.randrange(1, 10)
    old_list.append(a)
    i += 1

print(old_list)
new_list = [x for x in old_list if old_list.count(x) == 1]
print(new_list)
