class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)
        for i in range(len(haystack)-k+1):
            sub=haystack[i:i+k]
            if sub==needle:
                return i
        else:
            return -1
