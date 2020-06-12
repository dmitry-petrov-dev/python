# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One - 1
# Two - 2
# Three - 3
# Four - 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


from googletrans import Translator

trans = Translator()
try:
    for line in open("text_4.txt"):
        line_list = line.split()
        line_list[0] = trans.translate(line_list[0], 'ru', 'en').text
        with open("text_result_4.txt", "a") as f_obj:
            print(' '.join(line_list), file=f_obj)
except FileNotFoundError:
    print("File is not found")
