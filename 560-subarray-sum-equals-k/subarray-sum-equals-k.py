class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_record={0:1}
        total=0
        ans=0
        for n in nums:
            total+=n
            ans+=sum_record.get(total-k,0)
            sum_record[total]=sum_record.get(total,0)+1
        return ans