n = int(input())
left_sum = 0
right_sum = 0
diff = 0

for i in range(1, n + 1):
    left_sum += int(input())

for i in range(1, n + 1):
    right_sum += int(input())

if left_sum < right_sum:
    diff = right_sum - left_sum
elif left_sum > right_sum:
    diff = left_sum - right_sum
elif right_sum == left_sum:
    diff = 0

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")