n = int(input())
smallest_number = 99999999

for num in range(n):
    number = int(input()) 
    if number < smallest_number:
        smallest_number = number 
print(smallest_number)