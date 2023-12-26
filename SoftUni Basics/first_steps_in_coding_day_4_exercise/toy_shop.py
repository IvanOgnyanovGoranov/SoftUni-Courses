price_of_holiday = float(input())

puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
toy_trucks_number = int(input())

PUZZLE_PRICE = 2.60
DOLLS_PRICE = 3
BEARS_PRICE = 4.10
MINIONS_PRICE = 8.20
TRUCKS_PRICE = 2

price_of_toys = puzzles_number * PUZZLE_PRICE + dolls_number * DOLLS_PRICE + bears_number * BEARS_PRICE + \
                minions_number * MINIONS_PRICE + toy_trucks_number * TRUCKS_PRICE
number_of_toys = puzzles_number + dolls_number + bears_number + minions_number + toy_trucks_number

if number_of_toys >= 50:
    price_of_toys *= 0.75

price_of_toys *= 0.90

if price_of_toys > price_of_holiday:
    price_of_toys = price_of_toys - price_of_holiday
    print(f"Yes! {price_of_toys:.2f} lv left.")
else:
    price_of_toys = price_of_holiday - price_of_toys
    print(f"Not enough money! {price_of_toys:.2f} lv needed.")