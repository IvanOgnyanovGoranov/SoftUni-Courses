screening_type = str(input())
rows = int(input())
columns = int(input())

price = 0

if screening_type == "Premiere":
    price = (rows * columns) * 12
elif screening_type == "Normal":
    price = (rows * columns) * 7.50
elif screening_type == "Discount":
    price = (rows * columns) * 5

print(f"{price:.2f}")