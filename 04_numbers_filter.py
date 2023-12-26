def even_odd_filter(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        new_dict[key] = []
        if key == "odd":
            for num in value:
                if num % 2 != 0:
                    new_dict[key] += [num]
        else:
            for num in value:
                if num % 2 == 0:
                    new_dict[key] += [num]

    sorted_dict = dict(sorted(new_dict.items(), key=lambda item: len(item[1]), reverse=True))
    return sorted_dict

print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))