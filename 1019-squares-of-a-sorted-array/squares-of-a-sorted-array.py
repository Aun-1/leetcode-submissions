class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # for i,n in enumerate(nums):
        #     nums[i]=n*n
        # return sorted(nums)


        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        position = n - 1                          # fill from the back

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                result[position] = left_square    # the left end is bigger
                left += 1
            else:
                result[position] = right_square   # the right end is bigger (or equal)
                right -= 1
            position -= 1

        return result