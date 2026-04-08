n = int(input()) 

for row in range(n):
    if row == 0:
        each_row = "|"
    else:
        spaces = " " * row 
        each_row = "|" + spaces + "\\" 
    print(each_row)
for row in range(n):
    if row == n - 1:
        each_row = "|" 
    else:
        spaces = " " * (n - row - 1) 
        each_row = "|" + spaces + "/" 
    print(each_row) 