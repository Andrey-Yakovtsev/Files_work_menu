# 1. Создать пустой словарь, в котором ключ - название блюда = 1 строка, после разрыва,
# а значения = список словарей из списка продуктов и количеств
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
# 2. кол-во значений в списке указано сразу после названия. Как нам это поможет?
# 3. Строки можно разделять сепаратором "|"
from pprint import pprint
cook_book = {} #Это словарь из ключа = название блюда и значений = список из словарей ингридиентов
dish_items_list = [] #список из словарей ингридиентов
dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) #Это словарь ингридиентов
with open("reciepts_new.txt", 'r') as file:
    for line in file.readlines():
        line = line[0:-1] #обрезаем символ переноса строки
        line.strip()

        if line and len(line) > 2 and not "|" in line: #если одно слово и знаков в нем больше 2 (типа, не цифра)
            cook_book = dict.fromkeys([line], [])
            new_list = list(cook_book.values())
            print('список new_list - занчения словаря кукбук', new_list)
            print("Ключи словаря кукбук", cook_book)
        if line and len(line) <= 2 and not "|" in line: #выловили счетчик кол-ва ингридиентов в блюде
            counter = int(line)
            print(counter)
        if "|" in line: #строки с ингридиентами и порциями
            newdict = line.split(" | ")
            print(newdict)
            for item in range(int(counter)):
                dish_items['ingredient_name'] = newdict[0]
                dish_items['quantity'] = newdict[1]
                dish_items['measure'] = newdict[2]
                new_list.append(dish_items)
        print(new_list)
            # print(dish_items_list)
            # f = list(cook_book['line'])
            # print(f)
            # f.append(dish_items_list)
            # print(f)
    #         dish_items_list.append(dish_items)
    # print(dish_items_list)
            # print(cook_book.values())
        #
        # pprint(cook_book)


        #     cook_book = dict.fromkeys([line])
        #     cook_book['line'].append(dish_items_list)
        # pprint(cook_book)
        # if not line:
        #     break
        # elif:
        #     pass

