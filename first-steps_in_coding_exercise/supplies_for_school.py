number_of_pens = int(input())
markers_pack = int(input())
cleaning_supplies = int(input())
percentage = int(input())

discount_percentage = percentage / 100

pens = 5.80
markers = 7.20
detergent = 1.20

price_of_pens = number_of_pens * pens
price_of_markers = markers * markers_pack
price_of_detergent = cleaning_supplies * detergent

total_price = price_of_pens + price_of_markers + price_of_detergent
price_after_discount = total_price - (total_price * discount_percentage)

print(price_after_discount)