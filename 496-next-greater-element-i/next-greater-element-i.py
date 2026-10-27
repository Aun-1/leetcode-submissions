'''
INPUT: 
nums1: list[int]
nums2: list[int]
OUTPUT
greater_indexes: list[int]

EXAMPLES:
nums1 = [4,1,2], nums2 = [1,3,4,2]
OUTPUT: [-1,3,-1]

nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]

nums1 = [100, 120, 105], nums2 = [100, 98, 80, 105, 120]
OUTPUT: [3, -1, 4]
'''
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nge = {}
        stack = []
        ans=[]
        for x in nums2:
            while stack and x > stack[-1]:
                nge[stack.pop()] = x
            stack.append(x)
        for n in nums1:
            if n in nge:
                ans.append(nge[n])
            else:
                ans.append(-1)
        return ans