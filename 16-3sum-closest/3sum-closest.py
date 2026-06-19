class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() #nums = sorted(nums) Creates a new sorted list, Original list is unchanged
        closest = float('inf') 
        
        for i in range(len(nums) - 2):#at -2 space for j&k and last 2 indices
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                if total < target:
                    j += 1      
                elif total > target:
                    k -= 1       
                else:
                    return total
        
        return closest