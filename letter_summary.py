def letter_histogram(word):
    histogram = {}

    for letter in word:
        histogram[letter] = histogram.get(letter, 0) + 1

    return histogram

user_input = input("Please enter a word: ")

user_input = user_input.lower()

result = letter_histogram(user_input)
print(result)