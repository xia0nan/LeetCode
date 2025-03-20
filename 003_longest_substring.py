"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(min(m, n)) where m is the size of the charset/alphabet
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.
        
        Args:
            s (str): Input string
            
        Returns:
            int: Length of the longest substring without repeating characters
        """
        if not s:
            return 0
            
        char_dict = {}  # Dictionary to store character indices
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # If character exists and its index is >= left pointer,
            # move left pointer to the right of the duplicate
            if char in char_dict and char_dict[char] >= left:
                left = char_dict[char] + 1
            else:
                # Update max_length if current window is larger
                max_length = max(max_length, right - left + 1)
                
            # Update character's position
            char_dict[char] = right

        return max_length
