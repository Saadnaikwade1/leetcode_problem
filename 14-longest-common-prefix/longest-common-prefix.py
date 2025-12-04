class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        last=strs[-1]
        first=strs[0]
        ans=""
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return ans
            ans=ans+first[i]
        return ans
            
