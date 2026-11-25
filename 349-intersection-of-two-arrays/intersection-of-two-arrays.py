class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num1=set(nums1)
        nums2=set(nums2)
        result=set()

        for n in nums1:
            if n in nums2:
                result.add(n)

        return list(result)