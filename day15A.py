date = "3-12-2020"

list_a = date.split("-")
list_a = "/".join(list_a)

print(list_a)


word = "Leader"
modified_word = word[1:5:-2]

list_a = list(word)
list_a = list_a[1:5:-2]
list_a = "".join(list_a)

is_same = modified_word == list_a

print(is_same)



