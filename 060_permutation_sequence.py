from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        answer = []
        total = factorial(n)
        numbers = list(range(1,n+1))

        k -= 1

        while numbers:
            block_size = factorial(len(numbers)-1)
            index = k // block_size
            k %= block_size
            answer.append(str(numbers.pop(index)))

        return "".join(answer)