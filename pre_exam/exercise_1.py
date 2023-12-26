packing_paper_rolls = int(input())
fabric_rolls = int(input())
glue_litres = float(input())
discount_in_percentage = int(input()) / 100

PAPER = 5.80
FABRIC = 7.20
GLUE = 1.20

price = packing_paper_rolls * PAPER + fabric_rolls * FABRIC + glue_litres * GLUE
discount = price * discount_in_percentage
total_price = price - discount

print(f"{total_price:.3f}")