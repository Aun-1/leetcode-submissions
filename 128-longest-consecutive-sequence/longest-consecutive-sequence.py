class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums_set=set(nums)
        hi = 0
        for n in nums_set:
            count = 1
            if n-1 not in nums_set:
                while n + 1 in nums_set:
                    count+=1
                    n+=1
            if count+1 > hi:
                hi = count
                    
        return hi