class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen={}
        result=0
        for i in nums:
            diff1=i+k
            diff2=i-k
            if diff1 in seen:
                result+=seen[diff1]
            if diff2 in seen:
                result+=seen[diff2]
            seen[i]=seen.get(i,0)+1
        return result