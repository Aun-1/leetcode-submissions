class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count={0:1}
        ans=0
        odd_c=0

        for n in nums:
            if n%2!=0:
                odd_c+=1
            ans+=count.get(odd_c-k,0)
            count[odd_c]=count.get(odd_c,0)+1
        return ans