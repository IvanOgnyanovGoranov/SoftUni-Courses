number_of_lines = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, number_of_lines + 1):
    number = int(input())

    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print (f"Yes\nSum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No\nDiff = {diff}")

