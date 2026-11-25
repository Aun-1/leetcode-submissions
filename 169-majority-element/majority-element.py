class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = Counter(nums)
        n = len(nums)

        for num,count in count.items():
            if count>n/2:
                return num