divisor = int(input())
boundary = int(input())

largest_number = 0

for i in range(divisor, boundary + 1):
    if i % divisor == 0:
        largest_number = i

print(largest_number)