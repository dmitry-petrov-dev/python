curr_num = 0
max_num = 0
number = int(input("Enter positive number: "))

if number < 10:
    max_num = number
else:
    while number > 0:
        curr_num = number % 10
        number = number // 10
        if curr_num > max_num:
            max_num = curr_num

print('Max number is ', max_num)
