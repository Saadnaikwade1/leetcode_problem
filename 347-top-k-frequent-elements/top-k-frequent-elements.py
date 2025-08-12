from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=Counter(nums)
        nums=sorted(freq_map,key=freq_map.get,reverse=True)
        return nums[:k]

        