# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Необходимо использовать написанную ранее функцию int_func().

# def int_func(word):
#    word[0] =


def check_word(my_word):
    """ Function checks that words is contain only latin symbols
    a - 97    A - 65
    z - 122   Z - 90
    """

    for symbol in my_word:
        if ord(symbol) < 97 or ord(symbol) > 122:
            return False
    return True


def int_func(my_word):
    """ Function replaces first latin symbol to capital """
    return my_word.replace(my_word[0], chr(ord(my_word[0]) - 32), 1)


converted_text = ""
my_text_list = input("Input text using latin symbols in lowercase: ").split()
for i, word in enumerate(my_text_list):
    if check_word(word) and len(word) > 0:
        converted_text = converted_text + " " + int_func(word)
    else:
        converted_text = "None"
        print("Invalid text")
print(f"RESULT: {converted_text}")
