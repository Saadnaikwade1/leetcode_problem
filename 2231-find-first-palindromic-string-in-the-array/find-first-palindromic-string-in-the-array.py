class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            sub=w[::-1]
            if sub==w:
                return w
        return ""
        