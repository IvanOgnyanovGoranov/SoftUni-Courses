dancers_number = int(input())
point_given = float(input())
season = input()
place = input()

money_award = 0
money_per_dancer = 0
charity = 0

if place == "Bulgaria":
    money_award = point_given * dancers_number
    if season == "summer":
        money_award = money_award * 0.95
    elif season == "winter":
        money_award = money_award * 0.92
elif place == "Abroad":
    money_award = point_given * dancers_number
    money_award = money_award + (money_award / 2)
    if season == "summer":
        money_award = money_award * 0.90
    elif season == "winter":
        money_award = money_award * 0.85

charity = money_award * 0.75
money_award *= 0.25
money_per_dancer = money_award / dancers_number

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")