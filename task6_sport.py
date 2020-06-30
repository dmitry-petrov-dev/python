nr_day = 1
a = int(input("Enter the number of kilometers on the first day: "))
b = int(input("Enter target the number of kilometers : "))
if a > 0 and b > 0:
    while True:
        if a >= b:
            break
        a *= 1.1
        nr_day += 1
    print(f"The sportsman achieved result - no less {b} kilometer(s) on {nr_day} day ")
else:
    print("Your entered invalid values\n")
