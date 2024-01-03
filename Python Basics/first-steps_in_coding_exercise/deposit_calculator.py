deposit_sum = float(input())
months_of_deposit = int(input())
percentage = float(input()) / 100

interest_rate = deposit_sum * percentage
monthly_interest_rate = interest_rate / 12
total = deposit_sum + months_of_deposit * monthly_interest_rate

print(total)

