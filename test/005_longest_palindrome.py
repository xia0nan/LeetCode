class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        # Create a DP table
        dp = [[False] * n for _ in range(n)]
        
        start, max_length = 0, 1
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
        
        # Check substrings of length 3 and more
        for length in range(3, n + 1):  # Length of substring
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index
                
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        return s[start:start + max_length]
    