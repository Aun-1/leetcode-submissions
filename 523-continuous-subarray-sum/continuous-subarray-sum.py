class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0: -1}  
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k
            
            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                        remainder_index[remainder] = i

        return False


'''
nums = [1, 1, 2, 3, 1, 1]
k = 5

Initial:
remainder_map = {0: -1}
running_sum = 0

┌─────┬─────┬─────────────┬───────────┬──────────────────────┬───────────────────────────────┐
│ i   │ num │ running_sum │ remainder │ map before action    │ action                        │
├─────┼─────┼─────────────┼───────────┼──────────────────────┼───────────────────────────────┤
│ 0   │ 1   │ 1           │ 1         │ {0: -1}             │ 1 not in map → store {1: 0}  │
│ 1   │ 1   │ 2           │ 2         │ {0:-1, 1:0}         │ 2 not in map → store {2: 1}  │
│ 2   │ 2   │ 4           │ 4         │ {0:-1,1:0,2:1}      │ 4 not in map → store {4: 2}  │
│ 3   │ 3   │ 7           │ 2         │ {0:-1,1:0,2:1,4:2}  │ 2 already in map (index = 1) │
└─────┴─────┴─────────────┴───────────┴──────────────────────┴───────────────────────────────┘
'''