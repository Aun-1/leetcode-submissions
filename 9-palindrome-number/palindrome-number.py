'''
input -> int 
output -> bool 



approach > convt numbe into str 
edge-> check if len(str)<2: return flase

iterate for len(num//2) check reverse and forqerdpoitner wuqla 

dry run for odd length
12321 len//2->2 -> i and len -1 -i

dry run for even length 
123321 len // 2-> 3

if not equal at any point return flase 

in end return true 
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        length=len(str_x)

        for i in range(length//2):
            if str_x[i]!=str_x[length-1-i]:
                return False
        
        return True
