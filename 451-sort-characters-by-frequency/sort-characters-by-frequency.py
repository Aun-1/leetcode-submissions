class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for c in s:
            freq[c]=freq.get(c,0)+1

        pairs=[]
        for c in freq:
            pairs.append((freq[c],c))

        pairs.sort(reverse=True)#O(k log k)

        result=[]
        for count,c in pairs:
            result.append(c*count)#O(n) TC if we did c+another str it would be O(n2)

        return ''.join(result)
        #total TC: O(n+klogk)