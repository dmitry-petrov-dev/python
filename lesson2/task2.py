# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и
# 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

my_list = list(input("Enter any text: "))
print('Original list: ', my_list)
for ind in range(1, len(my_list), 2):
    my_list[ind-1], my_list[ind] = my_list[ind], my_list[ind-1]
print('New list: ', my_list)


