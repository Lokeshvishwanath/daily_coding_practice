n = int(input())

start_number = 1

for row in range(1, n + 1):
    if row == 1:
        first_row = ""
        for column in range(n):
            first_row += str(start_number) + " "
            start_number += 1
        print(first_row)
    elif row == n:
        last_row = str(start_number)
        print(last_row)
    else:
        each_row = str(start_number) + " "
        hollow_spaces = "  " * (n - row - 1)
        each_row += hollow_spaces
        start_number += int(len(hollow_spaces) / 2) + 1
        each_row += str(start_number) + " "
        start_number += 1
        print(each_row)