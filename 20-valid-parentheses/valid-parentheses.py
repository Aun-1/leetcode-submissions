'''
we make a brakcet pair of key an dvalues 
key will be front facing brakcets (
value bakc facing )
check if the bracket not in keys ([{
in the above case we will store that bracket and pop exisitng -> if pop's key is not what we encountered we give otu false 
else we keep gogn in out loop 
'''
class Solution:
    def isValid(self, s: str) -> bool:
        prev = None
        while prev != s:
            prev = s
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""
        # lst=[]
        # bracketMap={}
        # bracketMap["("]=")"
        # bracketMap["{"]="}"
        # bracketMap["["]="]"
        # frontC=0
        # backC=0

        # for b in s:
        #     if b in bracketMap:
        #         frontC+=1
        #         lst.append(b)
        #     else:
        #         if len(lst)<1:
        #             return False
        #         backC+=1
        #         check=lst.pop()
        #         if b!=bracketMap[check]:
        #             return False
        # if frontC==backC:
        #     return True
        # else:
        #     return False


'''
"{[([])]}"-->True
"{(])"--> False

s = "()[]{}"
dictionary -> the loop iterates until it sees a bracket in the backward direction -> making a doctor 
--> if the last bracket 

'''
