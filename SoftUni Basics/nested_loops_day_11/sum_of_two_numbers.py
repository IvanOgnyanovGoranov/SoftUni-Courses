first_number = int(input())
last_number = int(input())
magic_number = int(input())

combination_number = 0
is_found = False

for n1 in range(first_number, last_number + 1):
    for n2 in range(first_number, last_number + 1):
        combination_number += 1
        if n1 + n2 == magic_number:
            print(f"Combination N:{combination_number} ({n1} + {n2} = {magic_number})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{combination_number} combinations - neither equals {magic_number}")