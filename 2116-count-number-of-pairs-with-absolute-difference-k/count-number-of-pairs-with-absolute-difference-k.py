class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen={}
        result=0
        for i in nums:
            diff1=i+k
            diff2=i-k
            if diff1 in seen:
                result+=seen[diff1]
            if diff2 in seen:#not elif -> so both cases can be consdiered nums = [1,5,3], k=2-->Pairs: (1,3) diff=2 ✓, (5,3) diff=2 ✓ → answer should be 2
                result+=seen[diff2]
            seen[i]=seen.get(i,0)+1
        return result