def pattern1():
    n = 4 
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(n-i):
            print("*", end=" ") 
        print()

def hollow_rectangle():
    rows = 4 
    cols = 7 
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print("*",end=" ") 
            else:
                print(" ",end=" ") 
        print()
        
hollow_rectangle()