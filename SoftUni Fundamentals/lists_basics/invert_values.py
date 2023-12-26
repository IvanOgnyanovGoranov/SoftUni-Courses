numbers = input()
my_list = numbers.split(" ")
my_list = map(int, my_list)

new_list = []

for i in my_list:
    if i > 0:
        i = -abs(i)
    elif i < 0:
        i = abs(i)
    new_list.append(i)
    #or -int(i) - converts to int and changes to opposite
print(new_list)