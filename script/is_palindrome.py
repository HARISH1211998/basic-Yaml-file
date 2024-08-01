def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    return s == s[::-1]

# Test the function
string = "A man a plan a canal Panama"
print(f"Is '{string}' a palindrome? {is_palindrome(string)}")
