class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #make two pointers left and right 
        #left and rigth location
        #both satrt ofwith 0
        #right pointer in loop 
        #intialzie a list of aphatebts from t and keep popping
        #left += if not in seen simuultrnaouely 
        #if list==[]then left point +=
        
        if len(t)>len(s) or not t or not s:
            return ""
        if t==s:
            return s
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        have = {}
        formed = 0
        required = len(need)  # number of unique chars in t
        left = 0
        best = (float("inf"), 0, 0)  # (length, left, right)
        
        for right,c in enumerate(s):
            have[c] = have.get(c, 0) + 1
            
            if c in need and have[c] == need[c]:
                formed += 1
            
            # Contract: shrink from left while window is valid
            while formed == required:
                # Update best answer
                if (right - left + 1) < best[0]:
                    best = (right - left + 1, left, right)
                
                # Remove leftmost character
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        
        return "" if best[0] == float("inf") else s[best[1] : best[2] + 1]