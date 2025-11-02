class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b=nlargest(2,map(abs,nums))
        return a*b*10**5
