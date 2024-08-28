from collections import Counter

numbers = [1, 2, 3, 4, 5, 6, 1, 2, 1, 2]

# Count the occurrences of each number
counter = Counter(numbers)
print(counter)

# Find numbers that are repeated
repeated_numbers = [num for num, count in counter.items() if count > 1]

print(repeated_numbers)
