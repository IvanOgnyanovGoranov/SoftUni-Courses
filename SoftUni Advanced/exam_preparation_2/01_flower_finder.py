from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

flowers = {"rose": "rose",
           "tulip": "tulip",
           "lotus": "lotus",
           "daffodil": "daffodil"
           }


while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in flowers:
        flowers[word] = flowers[word].replace(vowel, '')
        flowers[word] = flowers[word].replace(consonant, '')

        if not flowers[word]:
            print(f"Word found: {word}")
            break
    else:
        continue

    break

else:
    print("Cannot find any word!")

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
