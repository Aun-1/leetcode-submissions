class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() #nums = sorted(nums) Creates a new sorted list, Original list is unchanged
        closest = float('inf')  # track closest sum found
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                # update if this sum is closer to target
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                if total < target:
                    j += 1       # need larger sum
                elif total > target:
                    k -= 1       # need smaller sum
                else:
                    return total # exact match, can't get closer
        
        return closest