import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for p in points:
            d=p[0]**2+p[1]**2
            heapq.heappush(heap, (-d,p))
            if len(heap)>k:
                heapq.heappop(heap)
        
        result = []
        for pair in heap:
            result.append(pair[1])
        
        return result
            
        

        #sorted() takes: 1. iterable e.g str or list to sort & 2. key= a function that it runs on every element to decide the order
        # def distance(point):
        #     return point[0]**2 + point[1]**2
        
        # sorted_points = sorted(points, key=distance)
        
        # return sorted_points[:k]

