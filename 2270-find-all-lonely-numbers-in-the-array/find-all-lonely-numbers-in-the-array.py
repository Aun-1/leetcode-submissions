class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        result = []
        seen = {}
        for n in nums:
            if n not in seen:
                seen[n]=1
            else:
                seen[n]+=1
        for n in seen:
            if seen[n] == 1 and n-1 not in seen and n+1 not in seen:
                result.append(n)
        return result
