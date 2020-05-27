sec = int(input("Please enter time in seconds "))
print(f'You entered {sec} seconds. It is {sec // 3600:02}:{(sec % 3600) // 60:02}:{sec % 60:02}\n.')
