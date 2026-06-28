class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        maxFreq = 0
        for v in freq.values():
            if v > maxFreq:
                maxFreq = v
        
        maxCount = 0
        for v in freq.values():
            if v == maxFreq:
                maxCount += 1
        
        frames = (n + 1) * (maxFreq - 1) + maxCount
        
        return max(len(tasks), frames)