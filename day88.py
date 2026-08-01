def pattern1():
    n = 4 
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(n-i):
            print("*", end=" ") 
        print()

def pattern2():
    n = 4
    for i in range(4):
        for j in range(n-i-1):
            print(" ", end=" ") 
        for j in range(2*i+1):
            print("*", end=" ") 
        print() 

pattern2()
