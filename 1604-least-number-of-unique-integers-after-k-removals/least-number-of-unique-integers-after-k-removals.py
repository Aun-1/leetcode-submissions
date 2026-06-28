class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = {}
        for n in arr:
            count[n] = count.get(n, 0) + 1
        
        sorted_items = sorted(count.items(), key=lambda x: x[1])
        
        k_check = 0
        # for num, freq in sorted_items:
        #     for _ in range(freq):
        #         if k_check == k:  
        #             break
        #         count[num] -= 1
        #         k_check += 1
        for num, freq in sorted_items:
            if k >= freq:      # ← just one check, no inner loop
                k -= freq
                count[num] = 0
            else:
                break
        
        result = 0
        for c in count:
            if count[c] > 0:
                result += 1
        return result