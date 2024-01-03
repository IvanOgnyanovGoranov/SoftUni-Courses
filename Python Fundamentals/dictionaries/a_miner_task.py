# resources_keys = []
# resources_values = []
# resources = {}
# string_counter = 0
# while True:
#     user_string = input()
#     if user_string == "stop":
#         break
#     string_counter += 1
#     if string_counter % 2 == 0:
#         resources_values.append(user_string)
#     else:
#         resources_keys.append(user_string)
#
# iterations = 0
# for element in resources_keys:
#     iterations += 1
#     if element not in resources.keys():
#         key = element
#         if iterations % 2 == 0:
#             value = resources_values[iterations - 1]
#             resources[key] = value
#     else:
#         resources[element] += value
#
# for char, values in resources.items():
#     print(f"{char} -> {values}")

resources = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break
    current_value = int(input())
    if current_resource in resources.keys():
        resources[current_resource] += current_value
    else:
        resources[current_resource] = current_value

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")