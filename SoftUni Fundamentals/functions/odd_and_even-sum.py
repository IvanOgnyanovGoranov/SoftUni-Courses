def sum_of_odd_and_even_digits(all_numbers):
    even_num_sum = 0
    odd_num_sum = 0
    for i in all_numbers:
        if int(i) % 2 == 0:
            even_num_sum += int(i)
        else:
            odd_num_sum += int(i)
    print(f"Odd sum = {odd_num_sum}, Even sum = {even_num_sum}")

single_number = input()
sum_of_odd_and_even_digits(single_number)