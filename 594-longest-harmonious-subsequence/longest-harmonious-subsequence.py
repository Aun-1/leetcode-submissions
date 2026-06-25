class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # largest=1
        # result=1
        # for n in set(nums):
        #     if result>largest:
        #         largest=result
        #     result=1
        #     for n2 in nums:
        #         if (n-n2)<=1 and (n-n2)>0:
        #             result+=1
        # return largest
        dict1={}
        for n in nums:
            dict1[n] = dict1.get(n, 0) + 1
        
        largest=0
        total=0
        for n in dict1:
            # total=dict1[n]+dict1.get(n+1, 0) was foing this BS
            if dict1.get(n+1, 0)!=0:
                total=dict1[n]+dict1[n+1]
            if total>largest:
                largest=total
        return largest

