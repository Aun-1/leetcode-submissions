class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1={}
        w2={}
        total=0
        for w in words1:
            w1[w]=w1.get(w,0)+1
        for w in words2:
            w2[w]=w2.get(w,0)+1
        for w in w1:
            if w1[w]==1 and w in w2 and w2[w]==1:
                total+=1
        return total