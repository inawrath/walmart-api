from helpers.palindrome import text_palindrome


class TestPalindrome:
    def test_is_palindrome(self):
        assert text_palindrome('arenera') is True

    def test_is_not_palindrome(self):
        assert text_palindrome('ivan') is False
