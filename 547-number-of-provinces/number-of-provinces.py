class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*len(isConnected)

        def DFS(i):
            visited[i] = True
            for j in range(len(isConnected)):
                if visited[j] == False and isConnected[i][j]==1:
                    DFS(j)

        prov = 0
        for i in range(len(isConnected)):
            if visited[i] == False:
                prov += 1
                DFS(i)
        return prov