class Solution:
    def expand_around_center(self, s: str, left: int, right: int) -> str:
        """
        Expands around the center and returns the longest palindromic substring.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        """
        Returns the longest palindromic substring in the given string.
        """
        if not s:
            return ""
        
        longest = ""
        for i in range(len(s)):
            # Odd-length palindromes (single character center)
            odd_palindrome = self.expand_around_center(s, i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            
            # Even-length palindromes (two-character center)
            even_palindrome = self.expand_around_center(s, i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest
