'''
forward num=1
replace num with foward num then multupli b tisel ffotuurre 
        '''
'''
1 1 2 6

prod 4
   12 8  6

reverse prod =1 eahc time first multow ith forard arrya num X prpdo replace
and update revese po by curr num  nultmlying i y
        '''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        forward=1
        output=[1]*len(nums)
        for i,n in enumerate(nums):
            output[i]=forward
            forward*=n
        
        backward=1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=backward
            backward*=nums[i]
        
        return output