class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1 or string length is less than numRows
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows as empty strings
        rows = [''] * numRows
        
        # Variables to track current direction and row
        index = 0
        step = 1  # 1 means moving down, -1 means moving up
        
        # Iterate through each character in the string
        for char in s:
            # Add the character to the current row
            rows[index] += char
            
            # Change direction if we reach the first or last row
            if index == 0:
                step = 1  # Start moving down
            elif index == numRows - 1:
                step = -1  # Start moving up
            
            # Move to the next row based on the current direction
            index += step
        
        # Combine all rows to get the final result
        return ''.join(rows)
        