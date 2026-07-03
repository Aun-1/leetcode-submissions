class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=s[:len(s)//2]
        b=s[len(s)//2:]
        a_vow=0
        b_vow=0
        vowels=set('aeiouAEIOU')
        for l in a:
            if l in vowels:
                a_vow+=1
        for l in b:
            if l in vowels:
                b_vow+=1
        if a_vow==b_vow:
            return True
        else:
            return False