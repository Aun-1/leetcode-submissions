class Solution:
    def reverse(self, x: int) -> int:
        
        original = x
        x = abs(x)
        str_x = str(x)
        length= len(str(x))
        reverse = ""
        for i in range(length-1, -1, -1):
            reverse+=str_x[i]
        
        
        reverse_int=int(reverse)

        if reverse_int > 2**31 - 1:          # outside the 32-bit range
            return 0

        if original<0:
            return -reverse_int
        else:
            return reverse_int