class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charTrack=[0]*26
        for c in s:
            charTrack[ord(c)-ord('a')]+=1
        for c in t:
            charTrack[ord(c)-ord('a')]-=1
        for n in charTrack:
            if n!=0:
                return False
        return True