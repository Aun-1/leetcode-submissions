class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        track={0:-1}
        result=0
        total=0
        for i,n in enumerate(nums):
            if n==1:
                total+=1
            else:
                total-=1
            if total in track:
                result=max(result,i-track[total])
            else:
                track[total]=i
        return result