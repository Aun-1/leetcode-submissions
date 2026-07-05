class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #TC O(n+m) SC O(n+m)
        # result=[]
        # dict1={}
        # dict2={}
        # for n in nums1:
        #     if n in dict1:
        #         dict1[n]+=1
        #     else:
        #         dict1[n]=1
        
        # for n in nums2:
        #     if n in dict2:
        #         dict2[n]+=1
        #     else:
        #         dict2[n]=1

        # for n in dict1:
        #     if n in dict2:
        #         result+=[n]*min(dict1[n],dict2[n])
        
        # return result

        #TC O(n+m)  SC O(n)
        dict1 = {}
        for n in nums1: #O(n)
            dict1[n] = dict1.get(n, 0) + 1
        
        result = []
        for n in nums2: #O(m)
            if n in dict1 and dict1[n] > 0:
                result.append(n)
                dict1[n] -= 1  # consume one occurrence
        
        return result


        #TOOK THIS APPROACH FIRST WHICH WAS WRONG
        # def Intersect_Small(list1, list2):
        #     result=[]
        #     for i in (list1):
        #         if i in list2:
        #             result.append(i)
        #     return result
        # if len(nums1)<len(nums2):
        #     return (Intersect_Small(nums1,nums2))
        # else:
        #     return (Intersect_Small(nums2,nums1))