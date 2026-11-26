from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0                              # i walks s, j walks t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:                     # LOOK + DECIDE: does s's letter match t's?
                i += 1                           # MOVE: matched → next letter of s
            j += 1                               # MOVE: t always moves forward
        return i == len(s)                       # LEFTOVER: did we match all of s?