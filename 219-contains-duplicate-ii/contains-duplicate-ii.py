class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:


#Too slow 
        # if k >= len(nums):
        #     return len(nums) != len(set(nums))
        # for i in range(len(nums)-k):
        #     if len(nums[i:i+k+1])!=len(set(nums[i:i+k+1])):
        #         return True
        # return False


        last ={}
        for i,n in enumerate(nums):
            if n in last:
                if abs(last[n]-i)<=k:
                    return True
            last[n]=i
        return False

        #sliding window solution
        # window = set()
        # for i,num in enumerate(nums):
        #     if num in window:
        #         return True
        #     window.add(num)
        #     if len(window) > k:
        #         window.remove(nums[i-k])
        # return False