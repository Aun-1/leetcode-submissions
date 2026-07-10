class Solution:
    def reorganizeString(self, s: str) -> str:
        count={}
        for c in s:
            count[c]=count.get(c,0)+1
        if max(count.values())>(len(s)+1)//2:
            return ""
        
        result = [''] * len(s)
        idx = 0
        
        for char, freq in sorted(count.items(), key=lambda x: -x[1]):
            for _ in range(freq):
                if idx >= len(s):
                    idx = 1
                result[idx] = char
                idx += 2
        
        
        return "".join(result)