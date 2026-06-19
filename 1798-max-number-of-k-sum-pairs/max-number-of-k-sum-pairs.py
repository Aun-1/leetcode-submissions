class Solution:
    # def maxOperations(self, nums: List[int], k: int) -> int:
    #     #2 pointer and in i not in seen 
    #     diff_count={}
    #     count=0
    #     for n in nums:
    #         if n in diff_count and diff_count[n]>0:
    #             count+=1
    #             diff_count[n]-=1
    #         else:
    #             diff_count[k-n]=diff_count.get(k-n,0)+1
    #     return count 
    '''
problem with using abs(k-n) with above approach:
Concrete counterexample — nums = [5, 2], k = 3:

n = 5: not matched yet → store diff_count[abs(3-5)] = diff_count[2] = 1
n = 2: diff_count[2] = 1 > 0 → counted as a match!

But 5 + 2 = 7 ≠ 3. There's no valid pair, so the answer should be 0, yet your code returns 1. The abs made the leftover "garbage" entry from 5 look like a legitimate partner for 2.
    '''

    #alternative sol:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #2 pointer and in i not in seen 
        diff_count={}
        count=0
        for n in nums:
            if n in diff_count and diff_count[n]>0:
                count+=1
                diff_count[n]-=1
            else:
                diff_count[k-n]=diff_count.get(k-n,0)+1
        return count 
