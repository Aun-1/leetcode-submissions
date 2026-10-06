# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         s_list=s.split()
#         if len(s_list)!=len(pattern):
#             return False

#         map_c_to_w = {}#char to word
#         map_w_to_c = {}
        
#         for c, w in zip(pattern, s_list):
#             if c in map_c_to_w:
#                 if map_c_to_w[c] != w:
#                     return False
#             else:
#                 map_c_to_w[c] = w
            
#             if w in map_w_to_c:
#                 if map_w_to_c[w] != c:
#                     return False
#             else:
#                 map_w_to_c[w] = c
        
#         return True
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(words)):
            if words[i] in word_to_char:
                if word_to_char[words[i]]!=pattern[i]:
                    return False
            if pattern[i] in char_to_word:
                if char_to_word[pattern[i]]!=words[i]:
                    return False
            char_to_word[pattern[i]]=words[i]
            word_to_char[words[i]]=pattern[i]
        return True