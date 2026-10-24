from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    #can we make fixed tupes to compae
        list_map=defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            list_map[tuple(count)].append(s)
        return list(list_map.values())
        