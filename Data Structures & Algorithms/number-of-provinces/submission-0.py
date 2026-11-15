class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        def dfs(j):
            visited.add(j)
            for r, connected in enumerate(isConnected[j]):
                if connected == 1 and r not in visited:
                    dfs(r)
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                count+=1
        return count