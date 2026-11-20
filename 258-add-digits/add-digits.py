'''
while sum >100: keep adding

make a def fucntion that break alls digial adds into a number 
'''
class Solution:
    def addDigits(self, num: int) -> int:

        def add_digits(n):
            total = 0
            str_n = str(n)
            for d in str_n:
                total+=int(d)
            return total

        while(num>=10):
            num = add_digits(num)
        
        return num