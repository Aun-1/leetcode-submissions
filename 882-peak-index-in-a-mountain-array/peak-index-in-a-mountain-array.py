class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo=0
        hi=len(arr)-1
        while lo<hi:
            mid=(lo+hi)//2
            if arr[mid]>arr[mid+1]:
                hi=mid
            else:
                lo=mid+1
        return lo