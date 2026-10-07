class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        unique_nums=set(nums)
        ans = 0
        if k!=0:
            for n in unique_nums:
                if (n + k) in unique_nums:
                    ans += 1
            return ans
        else:
            for n in unique_nums:
                if nums.count(n)>1:
                    ans+=1
            return ans