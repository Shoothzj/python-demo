from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        resultList = [0] * (n + 1)
        i = 0
        b = 1
        while b <= n:
            while i < b and i + b <= n:
                resultList[i + b] = resultList[i] + 1
                i += 1
            i = 0
            b <<= 1
        return resultList
