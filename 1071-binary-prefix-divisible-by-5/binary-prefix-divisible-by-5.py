class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        rem=0
        res=[]
        for bit in nums:
            rem=(rem*2+bit)%5
            if rem==0:
                res.append(True)
            else:
                res.append(False)
        return res