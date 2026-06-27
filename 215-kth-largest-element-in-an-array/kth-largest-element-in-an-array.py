class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse=True)
        # return nums[k-1]  

        #heap slighly better bcz because you never process more than k elements at a time.

        import heapq #O(nlogn)
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap) 
        return heap[0] 

