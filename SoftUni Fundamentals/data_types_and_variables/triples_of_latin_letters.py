
user_input = int(input())

for a in range(0, user_input):
    for b in range(0, user_input):
        for c in range(0, user_input):
            print(f"{chr(97 + a)}{chr(97 + b)}{chr(97 + c)}")
