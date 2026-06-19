class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen={}
        result=0
        for i in nums:
            if i in seen:
                result+=seen[i]
            seen[i]=seen.get(i,0)+1
        return result