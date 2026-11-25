'''
step 1: remove all ocuurence of val
step 2: return no of occurenece not equalto val (called k)
step 3: changre arr nums that first k elemnt not equal to val
'''
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0                      # next spot to write a kept value
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k