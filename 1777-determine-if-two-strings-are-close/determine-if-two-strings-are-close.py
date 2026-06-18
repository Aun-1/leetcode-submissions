# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:

#         freq1 = [0] * 26
#         freq2 = [0] * 26

#         for ch in word1:
#             freq1[ord(ch) - ord('a')] += 1

#         for ch in word2:
#             freq2[ord(ch) - ord('a')] += 1

#         for i in range(26):
#             if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
#                 return False

#         freq1.sort()
#         freq2.sort()

#         for i in range(26):
#             if freq1[i] != freq2[i]:
#                 return False

#         return True

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # count1 = Counter(word1) #O(n)
        # count2 = Counter(word2) #O(m)
        count1={}
        count2={}
        for c in word1:
            count1[c]=count1.get(c,0)+1
        for c in word2:
            count2[c]=count2.get(c,0)+1

        #Same set of distinct characters used
        if set(count1.keys()) != set(count2.keys()):
            return False

        #Same multiset of frequencies
        return sorted(count1.values()) == sorted(count2.values())#O(1) as k<=26 in O(klogk)