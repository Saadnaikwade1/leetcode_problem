class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        
        # smallest elements with remainder 1 or 2
        rem1 = float("inf")
        rem2 = float("inf")
        
        for num in nums:
            if num % 3 == 1:
                rem2 = min(rem2, rem1 + num)
                rem1 = min(rem1, num)
            elif num % 3 == 2:
                rem1 = min(rem1, rem2 + num)
                rem2 = min(rem2, num)
        
        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            return total - rem1
        else:   
            return total - rem2


