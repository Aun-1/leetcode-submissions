class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
            def check_max(mid):
                stores=0
                for q in quantities:
                    stores+=ceil(q/mid)
                return stores


            lo=1
            hi=max(quantities)
            while lo<hi:
                mid=(lo+hi)//2
                if check_max(mid)<=n:
                    hi=mid
                else:
                    lo=mid+1
            return lo
