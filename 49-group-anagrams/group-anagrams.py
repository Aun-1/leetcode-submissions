class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for n in strs:
            arr=[0]*26
            for c in n:
                arr[ord(c)-ord('a')]+=1
            strMap[tuple(arr)].append(n)

        return list(strMap.values()) 