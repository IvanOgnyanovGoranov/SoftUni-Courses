phonebook = {}

while True:
    entry = input()
    if "-" not in entry:
        break
    name, number = entry.split("-")
    phonebook[name] = number

for num in range(int(entry)):
    search_name = input()
    if search_name in phonebook.keys():
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")

