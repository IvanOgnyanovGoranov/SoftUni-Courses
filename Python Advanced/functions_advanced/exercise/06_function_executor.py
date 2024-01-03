def func_executor(*args):
    result = []

    for key, value in args:
        result.append(f"{key.__name__} - {key(*value)}")

    return "\n".join(result)

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


def other(num1, num2, num3):
    return num1 * num2 - num3
print(func_executor((sum_numbers, (1, 2)),(multiply_numbers, (2, 4)), (other, (2, 2, 3))))