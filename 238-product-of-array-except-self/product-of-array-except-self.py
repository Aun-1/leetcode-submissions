class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n

        for i in range(1, n):
            pre[i] = nums[i-1] * pre[i-1]

        for i in range(n-2, -1, -1):
            post[i] = nums[i+1] * post[i+1]

        return [pre[i] * post[i] for i in range(n)]

'''
pre = 3
[1 2 3 4]
[1 1 2 6]
pre = 2
'''
'''
post = 1
[1 2 3 4]
[1 1 2 6]
[24 ]
post = 4
'''