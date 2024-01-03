def sum_numbers(first, second):
    return  first + second

def substract(sum, third):
    return sum - third

def  add_and_subtract(number_one, number_two, number_three):
    sum_of_first_and_second_numbers = sum_numbers(number_one, number_two)
    result = substract(sum_of_first_and_second_numbers, number_three)
    return result

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))