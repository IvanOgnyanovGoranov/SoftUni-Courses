number1 = int(input())
number2 = int(input())
symbol = input()

result = 0

if symbol == "+":
    result = number1 + number2
    if result % 2 == 0:
        print(f"{number1} {symbol} {number2} = {result} - even")
    else:
        print(f"{number1} {symbol} {number2} = {result} - odd")
elif symbol == "-":
    result = number1 - number2
    if result % 2 == 0:
        print(f"{number1} {symbol} {number2} = {result} - even")
    else:
        print(f"{number1} {symbol} {number2} = {result} - odd")
elif symbol == "*":
    result = number1 * number2
    if result % 2 == 0:
        print(f"{number1} {symbol} {number2} = {result} - even")
    else:
        print(f"{number1} {symbol} {number2} = {result} - odd")
elif symbol == "/":
    if number1 == 0:
        print(f"Cannot divide {number2} by zero")
    elif number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        print(f"{number1} {symbol} {number2} = {number1 / number2:.2f}")
elif symbol == "%":
    if number1 == 0:
        print(f"Cannot divide {number1} by zero")
    elif number2 == 0:
        print(f"Cannot divide {number2} by zero")
    else:
        print(f"{number1} {symbol} {number2} = {number1 % number2}")
