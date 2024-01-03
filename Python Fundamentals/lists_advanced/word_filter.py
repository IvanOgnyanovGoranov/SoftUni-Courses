user_list = input().split(" ")
evens_list = [word for word in user_list if len(word) % 2 == 0]
print("\n".join(evens_list))