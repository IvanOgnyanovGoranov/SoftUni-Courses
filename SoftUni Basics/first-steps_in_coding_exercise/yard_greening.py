square_meters = float(input())

price = square_meters * 7.61
discount = price * 0.18
total = price - discount

print(f"The final price is: {total} lv.")
print(f"The discount is: {discount} lv.")