user_string = input()
encoded_string = ""
for char in user_string:
    char = ord(char)
    char += 3
    encoded_string += chr(char)
print(encoded_string)