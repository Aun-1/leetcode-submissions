class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connection = [False]*len(isConnected)

        def DFS(idx):
            connection[idx] = True
            for j in range(len(isConnected)):
                if connection[j]==False and isConnected[idx][j]==1:
                    DFS(j)



        prov = 0
        for i in range(len(isConnected)):
            if connection[i] == False:
                prov+=1
                DFS(i)
        return prov