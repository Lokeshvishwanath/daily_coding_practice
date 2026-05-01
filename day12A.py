number = input("") 
number = int(number) 

my_list = [10, 20, 40, 100] 
new_list = [number] + my_list + [number] 

list1 = [number] + my_list 
list2 = my_list + [number] 

print(list1) 
print(list2) 