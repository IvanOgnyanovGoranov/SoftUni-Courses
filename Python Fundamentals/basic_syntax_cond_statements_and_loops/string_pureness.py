string_number = int(input())

for _ in range(string_number):
    string_name = input()
    pure_or_not = ""
    for element in string_name:
        if element == "_" or element == "." or element == ",":
            print(f"{string_name} is not pure!")
            break
    else:
        print(f"{string_name} is pure.")