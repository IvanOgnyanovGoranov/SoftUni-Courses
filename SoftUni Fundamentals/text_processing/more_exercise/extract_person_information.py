import re

def extract_name(string):
    pattern = r"@([A-Za-z]+)\|"
    match = re.search(pattern, string)
    if match:
        return match.group(1)
    return False

def extract_age(string):
    pattern = r"#([0-9]+)\*"
    match = re.search(pattern, string)
    if match:
        return match.group(1)

def extracted_information():
    name = extract_name(user_string)
    age = extract_age(user_string)
    if name is not False and age is not False:
        return f"{name} is {age} years old."


number_of_lines = int(input())

for _ in range(number_of_lines):
    user_string = input()
    print(extracted_information())

