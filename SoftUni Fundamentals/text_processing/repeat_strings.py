strings = input().split()
result = ""

for string in strings:
    for letter in string:
        result += string

print(result)

# txt = "I like bananas bananas bananas"
# x = txt.replace("bananas", "apples", 2)
# print(x)
