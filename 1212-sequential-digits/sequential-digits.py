'''
digits = "123456789"--> len is 8
window of length -> size of oindwo from sie of low to size of hi 
check we go over every possibble wno in digitas achck chek if it first the range given 
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        sol = []
        digits = "123456789"
        for window_lenth in range(len(str(low)),len(str(high))+1):
            start=0
            while int(digits[start:start+window_lenth])<=high and start+window_lenth<=9:#123456789 is of len 8
                if int(digits[start:start+window_lenth])>=low:
                    sol.append(int(digits[start:start+window_lenth]))
                start+=1
        
        return sol