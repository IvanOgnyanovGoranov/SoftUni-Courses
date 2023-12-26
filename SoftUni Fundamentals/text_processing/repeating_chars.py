user_sequence = input()
new_sequence = user_sequence[0] + ""
repeated_letter = user_sequence[0]
for char in user_sequence:
    if char == repeated_letter:
        continue
    else:
        new_sequence += char
        repeated_letter = char
print(new_sequence)
