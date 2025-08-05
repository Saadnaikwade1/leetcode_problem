from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)  # Track used baskets
        alloted = 0

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if not used[j] and fruits[i] <= baskets[j]:
                    alloted += 1
                    used[j] = True  # Mark basket as used
                    break
        return len(fruits) - alloted
