yearly_training_price = int(input())

basketball_snickers_price = yearly_training_price * 0.60
basketball_clothes_price = basketball_snickers_price * 0.80
ball_price = basketball_clothes_price / 4
accessories = ball_price / 5

total_equipment_price = yearly_training_price\
                        + basketball_snickers_price\
                        + basketball_clothes_price + ball_price + accessories

print(total_equipment_price)