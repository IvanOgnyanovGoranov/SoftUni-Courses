sequence_1 = set(int(x) for x in input().split())
sequence_2 = set(int(x) for x in input().split())

for number_of_commands in range(int(input())):
    line = input().split()
    command = line[0] + " " + line[1]
    numbers = [int(n) for n in line[2:]]
    if command == "Add First":
        sequence_1.update(numbers)
    elif command == "Add Second":
        sequence_2.update(numbers)
    elif command == "Remove First":
        sequence_1.difference_update(numbers)
    elif command == "Remove Second":
        sequence_2.difference_update(numbers)
    elif "Check" in command:
        if sequence_1.issubset(sequence_2) or sequence_2.issubset(sequence_1):
            print("True")
        else:
            print("False")

if sequence_1:
    print(*sorted(sequence_1), sep=", ")
if sequence_2:
    print(*sorted(sequence_2), sep=", ")