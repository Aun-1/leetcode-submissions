'''
each map car store letter and count
another map cans tore letter and i 


if count exceeds 1 del the letter from both 
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1