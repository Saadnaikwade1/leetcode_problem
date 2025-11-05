from collections import Counter
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)
            sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            top_x = sorted_items[:x]
            total = 0
            for num, count in top_x:
                total += num * count
            res.append(total)

        return res
