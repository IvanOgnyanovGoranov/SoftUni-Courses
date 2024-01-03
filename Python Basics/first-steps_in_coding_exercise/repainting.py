nylon_amount = int(input())
paint_in_litres = int(input())
thinner_amount = int(input())
hours_of_work = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00

paint_additional_charge = paint_in_litres * 0.10
bags_charge = 0.40

nylon_total_price = (nylon_amount + 2) * nylon_price
paint_total_price = (paint_in_litres + paint_additional_charge) * paint_price
thinner_total_price = thinner_amount * thinner_price

materials_total = nylon_total_price + paint_total_price + thinner_total_price + bags_charge
amount_for_workers = (materials_total * 0.30) * hours_of_work
total_amount = materials_total + amount_for_workers

print(total_amount)