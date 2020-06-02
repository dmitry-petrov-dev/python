# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками
# товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все
# данные у пользователя.

# [(1, {x: y})
# ()
# ()]
goods = []
key_list = []
val_list = [[]]
item_dict = {}
analytic_dict = {}
ind = 0
while True:
    ind += 1
    item = input("Enter item: ")
    price = int(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    unit = input("Enter unit: ")
    goods.append((ind, {"item": item, "price": price, "quantity": qty, "unit": unit}))
    add_new = input("Do you want to add new item? Press y for continue: ")
    if add_new != 'y':
        break

for num, el in enumerate(goods):
    item_dict = el[1]
    if len(key_list) == 0: #first step
        key_list = item_dict.keys()
        val_list = [[0] * ind for i in range(len(key_list))] #init
    for pos, val in enumerate(item_dict.values()):
        val_list[pos][num] = val
for num, val in enumerate(key_list):
     analytic_dict.update({val: val_list[num]})
print(analytic_dict)