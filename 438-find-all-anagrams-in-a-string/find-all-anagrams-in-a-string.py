class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        p=''.join(sorted(p))
        f={}
        for i in range(len(s)-k+1):
            f[i]=s[i:i+k]
        l=[]
        for key,values in f.items():
            if p=="".join(sorted(values)):
                l.append(key)
        return l
        

        



        