class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)

        highest = 0
        for n in nums_set:
            if n-1 not in nums_set:
                length = 1
                while n+length in nums_set:
                    length+=1
                highest=max(highest, length)
        return highest
            

































        # if len(nums)<1:
        #     return 0
        # nums.sort()
        # c = 1
        # prev = nums[0]
        # hi = 0
        # for i,n in enumerate(nums):
        #     if i !=0:
        #         if n == prev + 1:
        #             c += 1
        #         else:
        #             if prev != n:
        #                 c = 1
        #         prev = n
            
        #     hi = max(hi, c)
        # return hi

        # nums_set=set(nums)
        # hi = 0
        # for n in nums_set:
        #     count = 1
        #     if n-1 not in nums_set:
        #         while n + 1 in nums_set:
        #             count+=1
        #             n+=1
        #         if count+1 > hi:
        #             hi = count
                    
        # return hi