
def solution(n,m,graph):

    
    def dfs(x,y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
        return False
        
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    return result
        
        
    


n, m = 4, 5


graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

answer = solution(n, m, graph)

print(answer)











# def solution(n, m, graph):
#     result = 0
    
#     def dfs(x,y):
#         if x < 0 or x >= n or y < 0 or y >= m:
#             return False
#         if graph[x][y] == 0:
#             graph[x][y] = 1
#             dfs(x-1,y)
#             dfs(x,y-1)
#             dfs(x+1,y)
#             dfs(x, y+1)
#             return True
#         return False
        
#     for i in range(n):
#         for j in range(m):
#             if dfs(i,j) == True:
#                 result += 1
#     return result
# 실제 실행
n = 4
m = 5