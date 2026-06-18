class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        window=[0]*26
        need=[0]*26

        for i in range(len(s1)):
            window[ord(s2[i])-ord('a')]+=1
            need[ord(s1[i])-ord('a')]+=1
        if window==need:
            return True 
        for i in range(len(s1),len(s2)):
            window[ord(s2[i])-97]+=1
            window[ord(s2[i-len(s1)])-97]-=1
            if window==need:
                return True
        return False
