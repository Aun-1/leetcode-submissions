class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo=0
        hi=len(nums)
        while lo<hi:
            mid=(lo+hi)//2
            if nums[mid]<target:
                lo=mid+1
            elif nums[mid]>target:
                hi=mid
            else:
                start=mid
                while start > 0 and nums[start-1]==target:
                    start-=1
                end=mid
                while end < len(nums) and nums[end]==target:
                    end+=1
                return [start,end-1]
        return [-1,-1]