class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res=[]
        for num in nums:
            if num%3==0 and num%2==0:
                res.append(num)
        if len(res)==0:
            return 0
        return sum(res)//len(res)
            