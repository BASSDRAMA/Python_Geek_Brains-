goods_amount = int(input('Введите количество разновидностей товара: '))
i = 1
goods_dict = {}
goods_list = []
review = {}

while i <= goods_amount:
    goods_dict = dict({'название': input('Введите название товара: '),
                       'Цена': input('Укажите цену товара: '),
                       'Количество': input('Укажите количество товара: '),
                       'ЕИ': input('Укажите единицы измерения: ')})
    goods_list.append((i, goods_dict))
    i += 1
    review = dict({'название': goods_dict.get('название'),
                   'Цена': goods_dict.get('Цена'),
                   'Количество': goods_dict.get('Количество'),
                   'Единицы измерения': goods_dict.get('ЕИ')})

    print(goods_list)
    print(review)







