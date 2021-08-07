from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        resultList = [0] * (n + 1)
        i = 1
        while i <= n:
            resultList[i] = resultList[i & (i - 1)] + 1
            i += 1
        return resultList
