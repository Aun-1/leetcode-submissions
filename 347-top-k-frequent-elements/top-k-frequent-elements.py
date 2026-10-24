class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        nums_map={}
        for n in nums:
            if n not in nums_map:
                nums_map[n]=1
            else:
                nums_map[n]+=1
            
        tuple_list=[]
        for num,count in nums_map.items():
            tuple_list.append([count,num])

        tuple_list.sort(reverse=True)
        sol=[]

        i=0
        while i<k:
            sol.append(tuple_list[i][1])
            i+=1

        return sol