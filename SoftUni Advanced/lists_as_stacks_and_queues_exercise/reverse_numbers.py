user_int = input().split()
reversed_stack = []
while user_int:
    removed_element = user_int.pop()
    reversed_stack.append(removed_element)
print(" ".join(reversed_stack))


# from collections import deque
#
# numbers = deque(input().split())
#
# for _ in range(len(numbers)):
#     print(numbers.pop(), end=" ")
