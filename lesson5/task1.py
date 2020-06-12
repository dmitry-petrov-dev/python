# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

seq = 0
print("Enter text. For exit please press SPACE")
with open("text_result_1.txt", "w") as output:
    while True:
        seq += 1
        text = input(f"line {seq}: ")
        if text == " ":
            break
        output.write(text + "\n")
print("Process is finished")
