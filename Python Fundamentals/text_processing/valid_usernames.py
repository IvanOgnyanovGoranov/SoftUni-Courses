def length(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def letters_and_numbers(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True

def redundant_symbols(username):
    if " " in username:
        return False
    return True

def username_check(username):
    if length(username) and letters_and_numbers(username) and redundant_symbols(username):
        print(username)
    return False

usernames = input().split(", ")

for username in usernames:
    if username_check(username):
        print(username_check(username))


