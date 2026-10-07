class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loss_m = {}
        win_m = {}
        for m in matches:
            if m[1] not in loss_m:
                loss_m[m[1]]=1
            else:
                loss_m[m[1]]+=1
            if m[0] not in win_m:
                win_m[m[0]] = 1
            else:
                win_m[m[0]] +=1
        result=[[],[]]
        for p in win_m:
            if p not in loss_m:
                result[0].append(p)
        for p in loss_m:
            if loss_m[p]==1:
                result[1].append(p)
        result[0].sort()
        result[1].sort()
        return result