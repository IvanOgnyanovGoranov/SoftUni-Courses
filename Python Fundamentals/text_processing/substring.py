first = input()
second = input()
while first in second:
    second = second.replace(first, "")
print(second)

# text = "this is softuni"
# new = text[:-4]
# # : = до т.е. режи от началото до минус 4, което ще принтира изрязаното
# print(new)