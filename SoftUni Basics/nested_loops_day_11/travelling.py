while True:
    destination = input()

    if destination == "End":
        break

    money_needed = float(input())
    saved_money = 0

    while money_needed > saved_money:
        saved_money += float(input())

    print(f"Going to {destination}!")