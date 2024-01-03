def all_the_charecters(first, second):
    characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character))
    return characters

first_character = input()
second_charecter = input()

print(" ".join(all_the_charecters(first_character, second_charecter)))