file_path = input().split("\\")
last_file = [file_path[-1]]
new_name = ""

for char in last_file:
    new_name += char
new_name = new_name.split(".")
file_name = new_name[0]
extension = new_name[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")