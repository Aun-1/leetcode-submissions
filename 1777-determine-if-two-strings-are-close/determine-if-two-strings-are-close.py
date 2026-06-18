from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = Counter(word1) #O(n)
        count2 = Counter(word2) #O(m)
        #same output as doing:
        # count1={}
        # count2={}
        # for c in word1:
        #     count1[c]=count1.get(c,0)+1
        # for c in word2:
        #     count2[c]=count2.get(c,0)+1

        #Same set of distinct characters used
        if set(count1.keys()) != set(count2.keys()):
            return False

        #Same multiset of frequencies
        return sorted(count1.values()) == sorted(count2.values())#O(1) as k<=26 in O(klogk)