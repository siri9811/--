n = 4
m = 4

character = [1, 1, 0]

maps = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

    

def solution(n, m, character, maps):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    x = character[0]
    y = character[1]
    direction = character[2]
    
    count = [[0] * m for _ in range(n)]
    
    turn_count = 0
    result = 0
    count[x][y] = 1
    
    while True:
        direction = (direction - 1) % 4
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if count[nx][ny] == 0 and maps[nx][ny] == 0:
            
            x = nx
            y = ny
            print(f'한칸 이동 후 현재 좌표 : {x, y}')
            
            count[nx][ny] = 1
            turn_count = 0
            result += 1
        else:
            turn_count += 1
            
        if turn_count == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if maps[nx][ny] == 1:
                break
            x = nx
            y = ny
            print(f'뒤로 한칸 이동 후 좌표 {x,y}')
            turn_count = 0
    
    return result
print(solution(n, m, character, maps))