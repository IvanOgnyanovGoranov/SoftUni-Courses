budget = float(input())
number_of_cards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

CARD_PRICE = 250
PROCESSOR_PRICE = (CARD_PRICE * number_of_cards) * 0.35
RAM_PRICE = (CARD_PRICE * number_of_cards) * 0.10

money_needed = (number_of_cards * CARD_PRICE) + (PROCESSOR_PRICE * number_of_processors) + (number_of_ram * RAM_PRICE)

if number_of_cards > number_of_processors:
    money_needed *= 0.85

if budget >= money_needed:
    print(f"You have {budget - money_needed:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_needed - budget:.2f} leva more!")