# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


nr_lines = 0
nr_words = 0
try:
    for line in open("text_input_2.txt"):
        nr_lines += 1  # counter lines
        nr_words += len(line.split())  # counter words
    print(f"Total lines: {nr_lines}; total words: {nr_words}")
except FileNotFoundError:
    print("File is not found")
