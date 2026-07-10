from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Step 1: build max requirement across all words2
        max_req = [0] * 26
        for w in words2:
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord('a')] += 1
            for i in range(26):
                if cnt[i] > max_req[i]:
                    max_req[i] = cnt[i]
        
        result = []
        for w in words1:
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord('a')] += 1
            
            ok = True
            for i in range(26):
                if cnt[i] < max_req[i]:
                    ok = False
                    break
            if ok:
                result.append(w)
        return result