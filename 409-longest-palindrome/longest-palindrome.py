class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0
        for c in s:
            if c in seen:
                ans+=2
                seen.remove(c)
            else:
                seen.add(c)
        #any char can be in the middle
        if len(seen)>0:
            return ans + 1
        else:
            return ans
        # #check if even if even then sum of even +1
        # freq=[0]*58
        # for c in s:
        #     freq[ord(c)-ord('A')]+=1
        # total=0
        # has_odd = False
        # for count in freq:
        #     if count % 2 == 0:
        #         total += count
        #     elif count>0:  #elif (count - 1) % 2 == 0 not required
        #         total += count - 1
        #         has_odd = True

        # return total + 1 if has_odd else total