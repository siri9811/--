from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    queue = deque([(0,0)])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
    # 여기에 코드를 작성해 주세요.
    answer = maps[n-1][m-1]
    
    return answer if answer > 1 else -1

maps1 = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]

maps2 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

print("Test 1 Result:", solution(maps1))  # 기대값: 11
print("Test 2 Result:", solution(maps2))  # 기대값: 9