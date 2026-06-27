from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Merge words2 into one "max needed per letter" counter
        max_req = Counter()
        for w in words2:
            c = Counter(w)
            for letter, cnt in c.items():
                max_req[letter] = max(max_req[letter], cnt)

        result = []
        for w in words1:
            c1 = Counter(w)
            if all(c1[letter] >= cnt for letter, cnt in max_req.items()):
                result.append(w)
        return result