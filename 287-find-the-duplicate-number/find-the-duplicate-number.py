class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#using O(n) extra space but only const extra space allowed
        # seen=set()
        # for n in nums:
        #     if n in seen:
        #         return n
        #     else:
        #         seen.add(n)

        #FLoyd's cycle detection
        slow=nums[0]
        fast=nums[0]

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        fast=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return fast