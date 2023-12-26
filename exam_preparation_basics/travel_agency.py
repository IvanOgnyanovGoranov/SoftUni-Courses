import sys

name_of_town = input()
type_of_package = input()
vip_discount = input()
stay_days = int(input())

price_per_day = 0
total_price = 0

if stay_days < 1:
    print("Days must be positive number!")
    sys.exit()

if name_of_town == "Bansko" or name_of_town == "Borovets":
    if type_of_package == "withEquipment":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day = 90
    elif type_of_package == "noEquipment":
        price_per_day = 80
        if vip_discount == "yes":
            price_per_day = 80 * 0.95
    else:
        print("Invalid input!")
        sys.exit()

    total_price = price_per_day * stay_days
    if stay_days > 7:
        total_price -= price_per_day

    print(f"The price is {total_price:.2f}lv! Have a nice time!")

elif name_of_town == "Varna" or name_of_town == "Burgas":
    if type_of_package == "withBreakfast":
        price_per_day = 130
        if vip_discount == "yes":
            price_per_day = 130 * 0.88
    elif type_of_package == "noBreakfast":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day = 100 * 0.93
    else:
        print("Invalid input!")
        sys.exit()

    total_price = price_per_day * stay_days
    if stay_days > 7:
        total_price -= price_per_day
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")


