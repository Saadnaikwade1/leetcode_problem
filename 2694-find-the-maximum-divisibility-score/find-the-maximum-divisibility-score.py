class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        mp={}
        for d in divisors:
            c=0
            for num in nums:
                if num%d==0:
                    c+=1
            mp[d]=c
        div=sorted(mp.items(),key=lambda x:(-x[1],x[0]))
        print(div)
        return div[0][0]
