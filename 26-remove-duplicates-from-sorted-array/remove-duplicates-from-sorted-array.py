'''
using while loop until length 
using while idx j=j+1 inisde the while

[1,2,2,2,3]
k=0
i=0

[1,2,2,2,3]
k=1


k=0
i=0
while i<len(nums)-1:
    if nums[i]<nums[i+1]:
        nums[k]=nums[i]
        k+=1

    else:
        while nums[i]==nums[i+1]:
            i+=1
    
        k+=1
    i+=1


'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:



        k = 0
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] < nums[i + 1]:   # last of its run
                nums[k] = nums[i]
                k += 1
        return k