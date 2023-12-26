
card_deck = input().split(", ")
number_of_commands = int(input())

for command_number in range(1, number_of_commands + 1):
    commands = input().split(", ")
    action = commands[0]
    if action == "Add":
        card_name = commands[1]
        if card_name not in card_deck:
            card_deck.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif action == "Remove":
        card_name = commands[1]
        if card_name in card_deck:
            card_deck.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action == "Remove At":
        index = int(commands[1])
        if len(card_deck) < index:
            print("Index out of range")
        else:
            del card_deck[index]
            print("Card successfully removed")

    elif action == "Insert":
        index = int(commands[1])
        new_card = commands[2]
        if len(card_deck) < index:
            print("Index out of range")
        elif new_card in card_deck:
            print("Card is already added")
        else:
            card_deck.insert(index, new_card)
            print("Card successfully added")
print(*card_deck, sep=', ')