class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x+1
        ans = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * mid <= x:
                ans = mid      # mid is a valid candidate, try for bigger
                lo = mid + 1
            else:
                hi = mid    # mid too big, search smaller
        return ans