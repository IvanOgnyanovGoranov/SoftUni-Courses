k = int(input())
l = int(input())
m = int(input())
n = int(input())

for n1 in range(k, 8 + 1):
    for n2 in range(9, l - 1, - 1):
        for n3 in range(m, 8 + 1):
            for n4 in range(9, n - 1, - 1):
                if n1 % 2 == 0 and n3 % 2 == 0 and n2 % 2 != 0 and n4 % 2 != 0:
                    if n1 == n3 and n2 == n4:
                        print("Cannot change the same player.")
                    else:
                        print(f"{n1}{n2} - {n3}{n4}")