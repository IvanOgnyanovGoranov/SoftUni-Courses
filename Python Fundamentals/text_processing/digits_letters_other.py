single_string = input()
letter_string = ""
digit_string = ""
other_string = single_string
for letter in single_string:
    if letter.isalpha():
        letter_string += letter
        other_string = other_string.replace(letter, "")
for digit in single_string:
    if digit.isdigit():
        digit_string += digit
        other_string = other_string.replace(digit, "")
print(digit_string)
print(letter_string)
print(other_string)
# not efficient (check lectures)