def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    return s == s[::-1]

# Test the function
string = input()
print(f"Is '{string}' a palindrome? {is_palindrome(string)}")
