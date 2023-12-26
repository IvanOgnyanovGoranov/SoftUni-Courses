def concatenate(*args, **kwargs):
    string = "".join(args)
    # for el in args:
    #     string += el

    for key, value in kwargs.items():
        if key in string:
            string = string.replace(key, value)
    return string

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))