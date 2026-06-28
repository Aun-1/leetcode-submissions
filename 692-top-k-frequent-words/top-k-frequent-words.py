class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq={}
        result=[]
        for w in words:
            freq[w]=freq.get(w,0)+1
        items = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        
        return items[:k]
        