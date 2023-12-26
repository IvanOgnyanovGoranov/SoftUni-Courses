math_string = list(input())
stack = []

for index in range(len(math_string)):
    if math_string[index] == "(":
        stack.append(index)
    elif math_string[index] == ")":
        start_index = stack.pop()
        print("".join(math_string[start_index:index + 1]))
