def digits_to_characters(messages):
    new_words = []
    for message in messages:
        digits = []
        letters = ""
        for i in message:
            if str.isdigit(i):
                digits += i
            else:
                letters += i
        digits = "".join(digits)
        digit_to_integer = int(digits)
        digit_to_character = chr(digit_to_integer)
        whole_word = digit_to_character + letters
        new_words.append(whole_word)
    return new_words


def switching_characters(ready_words):
    final_list = []
    for word in ready_words:
        char_list = []
        for char in word:
            char_list.append(char)
        second_char = char_list[1]
        last_char = char_list[-1]
        if len(char_list) > 2:
            char_list.pop(1), char_list.pop(-1)
            char_list.insert(1, last_char), char_list.append(second_char)
        word = "".join(char_list)
        final_list.append(word)
    list_to_words = " ".join(final_list)
    return list_to_words

secret_message = input().split(" ")
print(switching_characters(digits_to_characters(secret_message)))
