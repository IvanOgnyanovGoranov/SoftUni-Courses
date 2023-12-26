from datetime import datetime, timedelta

def extract_food_information(input_text):
    items = input_text.split('|')
    food_list = []

    for item in items:
        if '#' in item:
            item_info = item.split('#')
        else:
            item_info = item.split('|')

        if len(item_info) == 4:
            item_name = item_info[1].strip()
            expiration_date = item_info[2].strip()
            calories = item_info[3].strip()

            food_list.append({
                'item_name': item_name,
                'expiration_date': expiration_date,
                'calories': calories
            })

    return food_list

def calculate_total_calories(food_list):
    total_calories = 0

    for food in food_list:
        total_calories += int(food['calories'])

    return total_calories

def calculate_days_with_food(total_calories):
    calories_per_day = 2000
    return total_calories // calories_per_day

def find_days_until_expired(food_list):
    if not food_list:
        return None

    food_list.sort(key=lambda x: datetime.strptime(x['expiration_date'], "%d/%m/%y"))
    first_item = food_list[0]
    expiration_date = datetime.strptime(first_item['expiration_date'], "%d/%m/%y")

    return (expiration_date - datetime.now()).days

def print_food_information(food_list):
    print(f"You have food to last you for: {calculate_days_with_food(calculate_total_calories(food_list))} days!\n")

    for food in food_list:
        print(f"Item: {food['item_name']}, Best before: {food['expiration_date']},\nNutrition: {food['calories']}\n")

# Example usage:
input_text = "#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|"

food_list = extract_food_information(input_text)
print_food_information(food_list)