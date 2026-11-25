class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = Counter(arr)
        seen=set()

        for num in count.values():
            if num not in seen:
                seen.add(num)
            else:
                return False
        return True