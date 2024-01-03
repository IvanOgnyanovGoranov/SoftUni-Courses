def positives(user_numbers:list) -> list:
    positives_list = [number for number in user_numbers if int(number) >= 0]
    return positives_list

def negatives(user_numbers:list) -> list:
    negatives_list = [number for number in user_numbers if int(number) < 0]
    return negatives_list
def even_numbers(user_numbers:list) -> list:
    even_list = [number for number in user_numbers if int(number) % 2 == 0]
    return even_list
def odd_numbers(user_numbers:list) -> list:
    odd_list = [number for number in user_numbers if int(number) % 2 != 0]
    return odd_list

numbers = input().split(", ")
print(f"Positive: {', '.join(positives(numbers))}")
print(f"Negative: {', '.join(negatives(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")

