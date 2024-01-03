def min_max_sum(list):
    sum_of_num = 0
    list_of_int = []
    for num in list:
        list_of_int.append(int(num))
        sum_of_num += int(num)
    max_num = max(list_of_int)
    min_num = min(list_of_int)
    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {sum_of_num}")

list_of_numbers = input().split(" ")
min_max_sum(list_of_numbers)
