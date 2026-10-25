'''
for loop oertathe right pointer 
we will use a while loop that runs until sum>k
chekc if sum ==K at end 
'''
'''
dry run:
[1,1,1]
right = 1
left = 

right = 2

right = 3
left++1
'''
#count[total] = count.get(total, 0) + 1
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ansMap={0:1}
        total=0
        ans=0

        for n in nums:
            total+=n
            ans+=ansMap.get(total-k,0)
            ansMap[total]=ansMap.get(total,0)+1
            
        return ans 




'''
nums not only pos so sliding window doesent work
'''        
        # left = 0
        # total = 0
        # ans = 0

        # for right in range(len(nums)):
        #     total+=nums[right]
        #     while total>k:
        #         total-=nums[left]
        #         left+=1
        #     if total == k:
        #         ans+=1
        # return ans
