def filter(numbers):
    even_numbers = []
    for n in numbers:
        if int(n) % 2 == 0:
            even_numbers.append(int(n))
    return even_numbers

sequence_of_numbers = input().split(" ")
print(filter(sequence_of_numbers))