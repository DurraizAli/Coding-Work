def find_letter_occurrences(words, letter):
    for word in words:
        yield word.count(letter)
words = ["apple", "banana", "cherry"]
letter = "a"
output = find_letter_occurrences(words, letter)
print(next(output))
print(next(output))