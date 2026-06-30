class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        track={0:1}
        num_subarray=0
        total=0

        for n in nums:
            total+=n
            num_subarray+=track.get(total-goal,0)
            track[total]=track.get(total,0)+1
        return num_subarray