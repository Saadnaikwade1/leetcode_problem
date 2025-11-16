class Solution:
    def numSub(self, s: str) -> int:
        count=0
        result=0

        for ch in s:
            if ch == "1":
                count+=1
            else:
                result += count * (count+1) //2
                count=0
        
        result += count * (count +1)//2

        return result %(10**9+7)