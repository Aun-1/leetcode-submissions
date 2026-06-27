class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq #O(nlogn)
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap) 
        return heap[0] 