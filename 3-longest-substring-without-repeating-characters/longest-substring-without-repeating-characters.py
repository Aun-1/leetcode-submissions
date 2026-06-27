class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # naive pproach using a while loop and a set to check if a num there 
        # sliding window technique (using a hash map to track the last seen index of each character).
        last_seen={}
        left=0
        max_length=0

        for right,c in enumerate(s):
            if c in last_seen and last_seen[c]>=left:
                left=last_seen[c]+1
            max_length=max(max_length,right-left+1)
            last_seen[c]=right
            
        return max_length