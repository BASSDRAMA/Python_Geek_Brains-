# Иван, эти задания показались мне сложнее, поэтому я делал как вы объясняли на вебинаре.
# Раз за разом просматривал ваше решение, вникал в него и писал код самостоятельно
# в итоге вроде бы все понял
# пояснения больше оставлял для себя, чтобы окончательно вникунть в суть того, что я пишу

user_str = input('Введите ваши данные: ')
words = user_str.split()
# разделяем их методом сплит
for i, word in enumerate(words, start=1):
    #  задаем i, это будет номер, старт - цифра, с которой начнется
    # нумерация, фор - чтобы проггнать все введенные пользователем слова через цикл нумерации
    print(i, word[:10])
