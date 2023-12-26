version_number = [int(number) for number in input().split(".")]
version_number[-1] += 1
for index in range(len(version_number) -1, -1, -1):
    if version_number[index] > 9 and index != 0:
        version_number[index] = 0
        if index -1 >= 0:
            version_number[index-1] += 1
print(".".join(str(number) for number in version_number))

# version = input().split(".")
# version_as_string = "".join(version)
# version_as_int = int(version_as_string) + 1
# version_as_string = str(version_as_int)
# print(".".join(version_as_string))












