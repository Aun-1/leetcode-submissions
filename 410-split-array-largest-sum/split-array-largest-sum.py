class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def count_pieces(min_large):
            total_sum=0
            pieces=1
            for n in nums:
                if total_sum+n>min_large:
                    total_sum=0
                    pieces+=1
                total_sum+=n
            return pieces
        
        lo=max(nums)
        hi=sum(nums)
        while lo<hi:
            mid=(lo+hi)//2
            if count_pieces(mid)<=k:
                hi=mid
            else:
                lo=mid+1

        return lo