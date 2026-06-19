class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                # i, not i+1 — same number can be reused
                backtrack(i, current, remaining - candidates[i])
                current.pop()  # backtrack: undo the choice
        
        backtrack(0, [], target)
        return result