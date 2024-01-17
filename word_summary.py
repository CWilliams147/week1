def word_histogram(sentence):
    histogram = {}

    words = sentence.split()

    for word in words:
        
        word = word.lower()

        histogram[word] = histogram.get(word, 0) + 1

    return histogram

user_input = input("Please enter a sentence: ")

result = word_histogram(user_input)
print(result)