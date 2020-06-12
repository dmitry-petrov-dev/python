# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


import json

comp_counter = 0
total_profit = 0
comp_dict = {}
output_list = []
try:
    for line in open("text_7.txt", encoding='utf-8'):
        # searching subject
        comp_data = line.split()
        profit_loss = int(comp_data[2]) - int(comp_data[-1])
        if profit_loss > 0:
            total_profit += profit_loss
            comp_counter += 1
        comp_dict.update({comp_data[0] + " " + comp_data[1]: profit_loss})

        # check for div by zero
        if comp_counter == 0:
            comp_counter = 1
    output_list = [comp_dict, {"average_profit": int(total_profit / comp_counter)}]
    print(output_list)

    print(json.dumps(output_list, ensure_ascii=False).encode('utf-8'))
    with open("text_result_7.json", "w", encoding='utf-8') as json_file:
        json.dump(output_list, json_file, ensure_ascii=False, sort_keys=True, indent=4)
except FileNotFoundError:
    print("File is not found")
