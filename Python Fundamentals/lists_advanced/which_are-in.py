list1 = input().split(", ")
list2 = input().split(", ")
list3 = []

for x in list1:
    for y in list2:
        if x in y:
            list3.append(x)
            break

print(list3)




