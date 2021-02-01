# Как всегда, не все далось легко, это делаю по вашему решению, с 4 раза сам в итоге все написал и понял

new_dict = dict()
with open('new6.txt', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    splt_line = line.split()
    subj = splt_line[0]
    lessons_sum = sum([int(x[:x.find('(')]) for x in splt_line [1:] if '(' in x ])
    new_dict[subj[:-1]] = lessons_sum
print(new_dict)
