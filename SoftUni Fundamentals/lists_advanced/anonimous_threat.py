def merge(user_string, index1= int, index2= int):
    if index2 > len(user_string):
        pass
    else:
        concatenated_elements = "".join(user_string[index1:index2])
        user_string = user_string[:index1] + [concatenated_elements] + user_string[index2:]
    return user_string


def divide(user_string, index, partitions):
    element = user_string[index]
    partition_size = len(element) // partitions
    remaining_chars = len(element) % partitions

    divided_substrings = []
    start_index = 0

    for index, _ in enumerate(range(partitions)):
        substring_length = partition_size
        if remaining_chars > 0 and index == partitions - 1:
            substring_length += remaining_chars
        divided_substrings.append(element[start_index:start_index + substring_length])
        start_index += substring_length

    return user_string[:index] + divided_substrings + user_string[index + 1:]

string = input().split()

while True:
    command = input()
    if command == "3:1":
        break
    math_function, first_digit, second_digit = command.split()
    first_digit = int(first_digit)
    second_digit = int(second_digit)
    if math_function == "merge":
       string = merge(string, first_digit, second_digit)
    elif math_function == "divide":
        string = divide(string, first_digit, second_digit)

print(string)
