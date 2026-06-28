class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if not nums1 or not nums2:
            return []
        
        min_heap = []
        result = []
        
        # Seed heap: pair each nums1[i] with nums2[0]
        # Heap stores: (sum, i, j)
        for i in range(min(len(nums1), k)):  # no need beyond k elements
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        while min_heap and len(result) < k:
            curr_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # Advance j → next best partner for nums1[i]
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
        
        return result