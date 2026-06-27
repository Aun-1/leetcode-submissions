class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = [0]*26
        seen = set()
        for w in words2:
            c2 = [0]*26
            for c in w:
                c2[ord(c)-ord('a')] += 1
                seen.add(c)
            for i in range(26):
                count[i] = max(count[i], c2[i])
        result=[]
        for w in words1:
            temp=count[:]
            for c in w:
                if c in seen:
                    temp[ord(c)-ord('a')]-=1
                    if all(x <= 0 for x in temp):
                        result.append(w)
                        break
        return result