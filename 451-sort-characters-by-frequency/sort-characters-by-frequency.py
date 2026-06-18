class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for c in s:
            freq[c]=freq.get(c,0)+1

        pairs=[]
        for c in freq:
            pairs.append((freq[c],c))

        pairs.sort(reverse=True)

        result=[]
        for count,c in pairs:
            result.append(c*count)

        return ''.join(result)