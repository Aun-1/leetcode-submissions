class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        numCount = {}
        for n in nums:
            if n not in numCount:
                numCount[n]=1
            else:
                numCount[n]+=1
        
        heap = []
        for num, count in numCount.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for pair in heap:
            result.append(pair[1])
        return result