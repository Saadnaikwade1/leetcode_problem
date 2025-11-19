class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n=len(nums)
        while True:
            if original not in nums:
                return original
            else:
                original=original*2