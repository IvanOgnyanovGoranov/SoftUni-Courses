number_of_queries = int(input())
my_stack = []

for _ in range(number_of_queries):
    data = [int(x) for x in input().split()]
    command = data[0]
    if command == 1:
        my_stack.append(data[1])
    elif command == 2:
        if my_stack:
            my_stack.pop()
    elif command == 3:
        if my_stack:
            print(max(my_stack))
    elif command == 4:
        if my_stack:
            print(min(my_stack))

my_stack.reverse()
print(*my_stack, sep= ", ")