class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=list(s.lower())
        r=[]
        for i in s:
            if i.isalnum():
                r.append(i)
        r="".join(r)
        return r==r[::-1]
        