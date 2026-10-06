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

        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c

        return True