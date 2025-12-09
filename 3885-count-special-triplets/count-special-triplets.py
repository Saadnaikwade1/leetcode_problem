from collections import Counter
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left=Counter()
        right=Counter(nums)
        MOD=10**9+7
        res=0

        for x in nums:
            right[x]-=1
            double_val=x*2
            res=(res+left[double_val]*right[double_val])%MOD
            left[x]+=1
        return res
        