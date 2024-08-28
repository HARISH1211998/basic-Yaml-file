from collections import Counter

sentence = "Would you like additional like customization or any any any other resources included in this setup"
words = sentence.lower().split()

# Count occurrences of each word
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Count how many words are repeated
repeated_words_count = sum(1 for count in word_count.values() if count > 1)

# Print the count of repeated words
print(f"Number of repeated words: {repeated_words_count}")

# Print each word with its count
for word, count in word_count.items():
    print(f"'{word}': {count}")



### Added number repeated
number = [1,1,12,2,3,4,44,45,44,2,2]

counter_number = Counter(number)

repeated_number_count = [ num for num,count in counter_number.items() if count > 1]

print(repeated_number_count)
for repeated_number in repeated_number_count:
    print(f"{repeated_number} is repeated {counter_number[repeated_number]} times")

