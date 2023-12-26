searched_book = input()

number_of_books = 0

while True:
    text_input = input()

    if text_input == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {number_of_books} books.")
        break

    if text_input == searched_book:
        print(f"You checked {number_of_books} books and found it.")
        break
    number_of_books += 1
