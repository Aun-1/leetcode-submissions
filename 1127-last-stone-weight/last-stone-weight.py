import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        '''
Time complexity of your sorting version:

Worst case: O(n² log n)
“If every smash leaves a stone, each turn removes only one stone, so there are n − 1 turns. Each of those turns does insert(0, ...) in O(n) and re-sorts in O(n log n). So n turns × O(n log n) = O(n² log n).”

Best case: O(n log n)
“If stones always come in equal pairs, like [3, 3, 5, 5], every turn takes the equal branch, which is just two O(1) pops. The only real cost is the initial sort, O(n log n).”

Space: O(n)
“I modify the list in place, but Python’s sort uses up to O(n) extra memory internally.”
        '''
        # length = len(stones)
        # stones.sort()

        # while length > 1:
        #     if stones[-1]==stones[-2]:
        #         stones.pop()
        #         stones.pop()
        #     else:
        #         stones.insert(0,stones[-1]-stones[-2])
        #         stones.pop()
        #         stones.pop()
        #         stones.sort()
            
        #     length = len (stones)
        
        # if length==1:
        #     return stones[0]
        # else: return 0


        heap = []
        for s in stones:
            heap.append(-s)

        heapq.heapify(heap)

        length = len(heap)
        
        while length > 1:
            larger = -heapq.heappop(heap)
            smaller = -heapq.heappop(heap)

            if larger != smaller:
                heapq.heappush(heap, -(larger - smaller))
            
            length = len(heap)

        if length==1:
            return -heap[0]
        else: return 0