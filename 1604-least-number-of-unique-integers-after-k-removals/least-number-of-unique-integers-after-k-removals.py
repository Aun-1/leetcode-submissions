class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        #works but below is alcearn approach 
        # count = {}
        # for n in arr:
        #     count[n] = count.get(n, 0) + 1
        
        # sorted_items = sorted(count.items(), key=lambda x: x[1])
        
        # k_check = 0
        # for num, freq in sorted_items:
        #     for _ in range(freq):
        #         if k_check == k:  
        #             break
        #         count[num] -= 1
        #         k_check += 1

        # result = 0
        # for c in count:
        #     if count[c] > 0:
        #         result += 1
        # return result

        from collections import Counter
        freq = Counter(arr)
        counts = sorted(freq.values())  # ascending
        
        unique_remaining = len(counts)
        
        for c in counts:
            if k >= c:
                k -= c
                unique_remaining -= 1
            else:
                break
        
        return unique_remaining