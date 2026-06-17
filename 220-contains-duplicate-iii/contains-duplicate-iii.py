from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()
        
        for i, num in enumerate(nums):
            # Find closest value >= num - valueDiff
            idx = window.bisect_left(num - valueDiff)
            if idx < len(window) and window[idx] <= num + valueDiff:
                return True
            
            window.add(num)
            
            # Shrink window
            if len(window) > indexDiff:
                window.remove(nums[i - indexDiff])
        
        return False