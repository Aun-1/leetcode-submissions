class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count_s = [0] * 26
        count_t = [0] * 26

        for c in s:
            count_s[ord(c) - ord('a')] += 1

        for c in t:
            count_t[ord(c) - ord('a')] += 1

        result = 0
        for i in range(26):
            result += abs(count_s[i] - count_t[i])

        return result//2