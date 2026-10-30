'''
mid -> 4
left = 0 right = 3, mid 1
left = 2, right 3, mid 2

'''
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid*mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return left-1