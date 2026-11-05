import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        ans = []

        heap = []

        for p in points:
            dist = p[0] ** 2 + p[1] ** 2
            heapq.heappush(heap, [dist, p])

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
