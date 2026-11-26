class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        hi=float('-inf')
        total=0
        left = 0
        for right in range(len(nums)):
            total+=nums[right] 
            while right-left+1>k:
                total-=nums[left]
                left+=1
            if right-left+1==k:
                hi=max(hi,total)
        return hi/k