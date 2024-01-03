def loading_bar(percentage):
    bar_list = []
    number_of_percentages = int(percentage[0])
    number_of_dots = 10 - number_of_percentages
    if percentage == "100":
        for num in range(10):
            bar_list.append("%")
    else:
        for num in range(number_of_percentages):
            bar_list.append("%")
        for dots in range(number_of_dots):
            bar_list.append(".")
    result = ''.join(bar_list)
    return result
    # print(*bar_list, sep="")

user_percentage = input()

if user_percentage == "100":
    print("100% Complete!")
    print(f"[{(loading_bar(user_percentage))}]")
else:
    print(f"{user_percentage}% [{(loading_bar(user_percentage))}]")
    print("Still loading...")