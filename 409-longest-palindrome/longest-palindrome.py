class Solution:
    def longestPalindrome(self, s: str) -> int:
        #check if even if even then sum of even +1
        freq=[0]*58
        for c in s:
            freq[ord(c)-ord('A')]+=1
        total=0
        has_odd = False
        for count in freq:
            if count % 2 == 0:
                total += count
            elif (count - 1) % 2 == 0:
                total += count - 1
                has_odd = True

        return total + 1 if has_odd else total