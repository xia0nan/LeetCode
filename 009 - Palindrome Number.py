class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_list = [i for i in x_str]
        is_pal = True
        x_len = len(x_list)
        for i in range(x_len//2):
            if x_list[i] != x_list[x_len-i-1]:
                is_pal = False
        return is_pal