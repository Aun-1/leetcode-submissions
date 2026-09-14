class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # pre = [1] * n
        # post = [1] * n

        # for i in range(1, n):
        #     pre[i] = nums[i-1] * pre[i-1]

        # for i in range(n-2, -1, -1):
        #     post[i] = nums[i+1] * post[i+1]

        # return [pre[i] * post[i] for i in range(n)]


        prod = [1] * len(nums)

        for i in range(1, len(nums)):
            prod[i] = nums[i-1] * prod[i-1]

        suffix = 1
        for i in range(len(nums)-2, -1, -1):
            suffix *= nums[i+1]
            prod[i] *= suffix

        return prod
'''
PRE:
[1 2 3 4]
[1 1 2 6]
'''
'''
POST:
[1 2 3 4]
[24 12 4 1]
'''


