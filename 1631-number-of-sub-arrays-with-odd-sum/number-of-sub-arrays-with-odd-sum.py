class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = {0: 1}   # parity → frequency
        total = 0
        ans = 0

        for n in arr:
            total += n
            parity = total % 2
            ans += count.get(1 - parity, 0)  # look up opposite parity
            count[parity] = count.get(parity, 0) + 1
            ans %= MOD

        return ans