class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1={}
        for i,n in enumerate(nums):
            if n in dict1 and abs(dict1[n]-i)<=k:
                    return True
            dict1[n]=i
        return False