def age_assignment(*args, **kwargs):
    string_list = []
    for name in sorted(args):
        first_letter = name[0]
        for letter, age in kwargs.items():
            if str(letter) == first_letter:
                string_list.append(f"{name} is {age} years old.")
                break

    return "\n".join(string_list)



print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))