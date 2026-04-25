n = int(input())
 
for i in range(1, n + 1):
    if i == 1:
        row = ""
        row += (n - 1) * (" ") + "5 "
        print(row)
    elif (i==n):
        for j in range(n):
            print(5 + j, end=" ")
        print()
    else:
        row = ""
        left_spaces = n - i
        middle_spaces = 2 * i - 4
        row += left_spaces * " " + "5 " + middle_spaces * " " + str(i + 4) + " "
        print(row)