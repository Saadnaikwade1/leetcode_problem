class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p_count = Counter(p)
        s_count = Counter(s[:k-1])
        res = []

        for i in range(k-1, len(s)):
            s_count[s[i]] += 1
            
            
            if s_count == p_count:
                res.append(i - k + 1)
            
           
            s_count[s[i - k + 1]] -= 1
            if s_count[s[i - k + 1]] == 0:
                del s_count[s[i - k + 1]]

        return res
