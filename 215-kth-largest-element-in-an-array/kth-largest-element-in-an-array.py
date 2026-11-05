import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # heapq.heapify(nums)

        # while len(nums)>k:
        #     heapq.heappop(nums)
        
        # return nums[0]
        '''
        ABOVE SOLUTION
        Time: O(n + (n−k) log n)
        “Heapify builds the heap in O(n). Then I pop until k items are left, which is n − k pops, each O(log n) because the heap has up to n items.”
        Space: O(1)
        “Heapify works in place on nums, so I use no extra memory.”


        BELOW SOLUTION (BETTER FOR SMALL K ALSO STANDARD)
        Time: O(n log k)
        “I loop over all n numbers. Each push or pop is O(log k), because the heap never grows past k + 1 items.”

        Space: O(k)
        “The heap holds at most k + 1 items at any time.”
        '''

        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:          
                heapq.heappop(heap)
        return heap[0] 