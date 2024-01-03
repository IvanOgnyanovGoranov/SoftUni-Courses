def palindrome(word, index=0):
    word = word.lower()

    if index >= len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] == word[-(index + 1)]:
        return palindrome(word, index + 1)
    else:
        return f"{word} is not a palindrome"

print(palindrome("abcba", 0))
print(palindrome("peter", 0))
print(palindrome("assa", 0))