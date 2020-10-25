def text_palindrome(text):
    text = text.lower()
    return len(text) > 1 and text == text[::-1]
