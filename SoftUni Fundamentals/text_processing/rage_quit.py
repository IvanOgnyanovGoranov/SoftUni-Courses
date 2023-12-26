rage_input = input().upper
temporary_sequence = ""
final_sequence = ""
symbols_used = 0
multiplier = ""

for index in range(rage_input):
    if not rage_input[index].isdigit():
        temporary_sequence += rage_input[index]

print(f"Unique symbols used: {symbols_used}")
print(final_sequence)