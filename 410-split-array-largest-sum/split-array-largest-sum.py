class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check_splits(mid):
            pieces=1
            curr_sum=0
            for n in nums:
                if curr_sum+n>mid:
                    pieces+=1
                    curr_sum=0
                curr_sum+=n
            return pieces
   
        lo=max(nums)
        hi=sum(nums)
        while lo<hi:
            mid=(lo+hi)//2
            if check_splits(mid)<=k:
                hi=mid
            else:
                lo=mid+1
        return lo

