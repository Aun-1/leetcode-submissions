class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while k > j:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:  # skip duplicate j
                        j += 1
                    while j < k and nums[k] == nums[k-1]:  # skip duplicate k
                        k -= 1
                    j += 1
                    k -= 1
                else:
                    k -= 1
        return result