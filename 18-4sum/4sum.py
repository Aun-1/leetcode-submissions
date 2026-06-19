class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                k=j+1
                l=len(nums)-1
                while k<l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        while k<l and nums[k] == nums[k + 1]:
                            k+=1
                        while k<l and nums[l] == nums[l - 1]:
                            l-=1
                        k+=1
                        l-=1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k+=1
                    else:
                        l-=1
        seen = set()
        filtered = []
        for i in result:
            t = tuple(i)        # lists aren't hashable, convert to tuple
            if t not in seen:
                seen.add(t)
                filtered.append(i)
        result = filtered
        return result






        # for i in range(len(nums)-1):
        #     for j in range(len(nums)-2,0,-1):
        #         k=i+1
        #         l=j-1
        #         while l>k:
        #             if nums[i] + nums[j] + nums[k] + nums[l] == target:
        #                 result.append([nums[i],nums[j],nums[k],nums[l]])
        #             elif nums[i] + nums[j] + nums[k] + nums[l] < target:
        #                 k+=1
        #             else:
        #                 l-=1
        # return result


