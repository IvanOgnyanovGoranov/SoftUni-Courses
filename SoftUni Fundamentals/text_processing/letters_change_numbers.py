user_string = input().split()
total_sum = 0

for word in user_string:
    letters = ""
    digit = ""
    current_sum = 0
    for element in word:
        if element.isalpha():
            letters += element
        elif element.isdigit():
            digit += element

    digit = int(digit)

    if letters[0].isupper():
        current_sum = digit / (ord(letters[0]) - 64)
    elif letters[0].islower():
        current_sum = digit * (ord(letters[0]) - 96)

    if letters[1].isupper():
        current_sum -= (ord(letters[1])- 64)
    elif letters[1].islower():
        current_sum += (ord(letters[1]) - 96)

    total_sum += current_sum

print(f"{total_sum:.2f}")