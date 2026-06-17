class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # seen=set(arr)
        # for i in arr:
        #     if i*2 in seen and i!=0:
        #         return True
        # return False

        dict1={}
        for i,n in enumerate(arr):
            dict1[n]=i

        for i,n in enumerate(arr):
            if dict1.get(n*2)!=None and dict1.get(n*2)!=i:
                return True 
        return False