class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_hours(k):
            hours=0
            for n in piles:
                hours+=ceil(n/k)
            return hours
        lo=1
        hi=max(piles)
        while lo<hi:
            mid=(lo+hi)//2
            if calc_hours(mid)<=h:
                hi=mid
            else:
                lo=mid+1
        return lo