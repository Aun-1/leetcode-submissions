class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calc_days(weight):
            days_c=1
            total=weight
            for n in weights:
                if total-n>=0:
                    total-=n
                else:
                    total=weight
                    total-=n
                    days_c+=1
            return days_c
        
        lo=max(weights)
        total_weight=0
        for n in weights:
            total_weight+=n
        hi=total_weight
        while lo<hi:
            mid=(lo+hi)//2
            if calc_days(mid)<=days:
                hi=mid
            else:
                lo=mid+1
        return lo