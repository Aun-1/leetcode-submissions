class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()

        if len(s)!=len(pattern):
            return False
        pattern_to_s = {}
        s_to_pattern = {}

        for i in range(len(s)):
            if pattern[i] in pattern_to_s and pattern_to_s[pattern[i]]!=s[i]:
                return False
            if s[i] in s_to_pattern and s_to_pattern[s[i]]!=pattern[i]:
                return False
            
            pattern_to_s[pattern[i]]=s[i]
            s_to_pattern[s[i]]=pattern[i]

        return True