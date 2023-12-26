def start_spring(**kwargs):
    collections = {}
    for collection in kwargs.items():
        if collection[1] not in collections.keys():
            collections[collection[1]] = []
        collections[collection[1]] += [collection[0]]

    result = ""
    sorted_collections = dict(sorted(collections.items(), key=lambda item:(-len(item[1]), item[0])))
    for type, item in sorted_collections.items():
        result += f"{type}:\n"
        result += '\n'.join(f"-{x}" for x in sorted(item))
        result += "\n"

    return result

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
