class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list=[]

        for c in s:
            if c.isalnum():
                s_list.append(c.lower())

        for i in range(len(s_list)//2):
            if s_list[i]!=s_list[len(s_list)-i-1]:
                return False
        return True