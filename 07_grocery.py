def grocery_store(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    for product, quantity in sorted_dict:
        result.append(f"{product}: {quantity}")

    return "\n".join(result)

print(grocery_store(
bread=5,
pasta=12,
eggs=12,
))