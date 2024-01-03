string_one = input()
string_two = input()

last_string = string_one

for char_index in range(len(string_one)):
    left_part = string_two[:char_index + 1]
    right_part = string_one[char_index + 1:]
    new_string = left_part + right_part
    if new_string == last_string:
        continue
    print(new_string)
    last_string = new_string