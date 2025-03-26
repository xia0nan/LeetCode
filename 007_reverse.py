class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range limits.
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign of the number.
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reversed_num = 0
        
        # Reverse the integer digit by digit.
        while x:
            # Extract the last digit.
            digit = x % 10
            x //= 10
            
            # Check for potential overflow before updating reversed_num.
            if reversed_num > (INT_MAX - digit) // 10:
                return 0
            
            reversed_num = reversed_num * 10 + digit
        
        # Restore the original sign.
        reversed_num *= sign
        
        # Final check to ensure the reversed number is within the 32-bit signed range.
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        
        return reversed_num
