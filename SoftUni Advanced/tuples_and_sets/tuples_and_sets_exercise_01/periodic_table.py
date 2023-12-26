n = int(input())
ch_elements = set()

for _ in range(n):
    chemicals = input().split()
    for chemical in chemicals:
        ch_elements.add(chemical)

print(*ch_elements, sep="\n")
