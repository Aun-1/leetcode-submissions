class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for l in t:
            if l not in s or t.count(l)>s.count(l):
                return l