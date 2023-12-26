money_needed_for_vacation = float(input())
current_amount = float(input())

days = 0
money_saved = current_amount
number_of_spending_days = 0

while True:
    action = input()
    days += 1

    if action == "save":
        saved_amount = float(input())
        money_saved += saved_amount
        number_of_spending_days = 0
        if money_saved >= money_needed_for_vacation:
            print(f"You saved the money for {days} days.")
            break
    if action == "spend":
        number_of_spending_days += 1
        spend_amount = float(input())
        money_saved = money_saved - spend_amount
        if number_of_spending_days == 5:
            print("You can't save the money.")
            print(f"{days}")
            break
    if money_saved <= 0:
        money_saved = 0
