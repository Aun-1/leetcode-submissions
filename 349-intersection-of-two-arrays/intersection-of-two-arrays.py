class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_set=set(nums2)#O(m)
        ans_set=set()
        for n in nums1: #O(n)
            if n in nums_set:
                ans_set.add(n)
        return list(ans_set)
        
#total TC O(n+m)