def kwargs_length(**kwargs):
    return len(kwargs)



dictionary = {'name': 'Peter', 'age': [25, 3]}

print(kwargs_length(**dictionary))