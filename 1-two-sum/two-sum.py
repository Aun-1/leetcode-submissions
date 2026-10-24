class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    #dict to store num and idx
    #4  target- num  
        nums_map={}
        for i, n in enumerate(nums):
            if target - n in nums_map:
                return [nums_map[target-n], i]
            else:
                nums_map[n] = i