class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        if len(nums)<1:
            return 0
        count = 1 
        high = 1

        for n in seen:
            if n-1 not in seen:
                num=n
                while num+1 in seen:
                    count+=1
                    num+=1
                if count > high:
                    high = count
                count = 1
        
        return high

