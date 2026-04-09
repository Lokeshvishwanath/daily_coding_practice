string = input()
for each_character in string:
    if each_character != " ":
        unicode_value = ord(each_character) - 1
        character = chr(unicode_value)
        
        print(character) 