class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        ans = 0
        charMap={}


        for right in range(len(s)):
            if s[right] in charMap:
                charMap[s[right]]+=1
            else:
                charMap[s[right]]=1
            
            #len of window - max of same lements
            while (right-left+1) - max(charMap.values())>k:
                charMap[s[left]]-=1
                left+=1
        
            ans=max(ans, right-left+1)

        return ans