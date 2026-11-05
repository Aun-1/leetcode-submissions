class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        length = len(stones)
        stones.sort()

        while length > 1:
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones.insert(0,stones[-1]-stones[-2])
                stones.pop()
                stones.pop()
                stones.sort()
            
            length = len (stones)
        
        if length==1:
            return stones[0]
        else: return 0
