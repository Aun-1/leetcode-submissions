class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check_threshold(divisor):
            total=0
            for n in nums:
                total+=ceil(n/divisor)
            return total

        lo=1
        hi=max(nums)

        while lo<hi:
            mid=(lo+hi)//2
            if check_threshold(mid)<=threshold:
                hi=mid
            else:
                lo=mid+1
        return lo