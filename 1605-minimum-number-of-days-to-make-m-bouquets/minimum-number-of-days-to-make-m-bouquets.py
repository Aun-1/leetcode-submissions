class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1

        def bq_calc(mid):
            flowers=0
            bq=0
            for d in bloomDay:
                if d<=mid:
                    flowers+=1
                    if flowers==k:
                        bq+=1
                        flowers=0
                else:
                    flowers=0
            return bq
        
        lo=min(bloomDay)
        hi=max(bloomDay)
        while lo<hi:
            mid=(lo+hi)//2
            if bq_calc(mid)>=m:
                hi=mid
            else:
                lo=mid+1

        return lo