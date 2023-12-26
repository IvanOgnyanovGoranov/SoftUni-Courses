symbols = input()

for char in sorted(set(symbols)):
    count = symbols.count(char)
    print(f"{char}: {count} time/s")
