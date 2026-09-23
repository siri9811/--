def solution(n, roads, k, x):
    INF = float('inf')
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n+1):
        for j in range(n+1):
            if i==j:
                graph[i][j] = 0
    
    for a, b in roads:
        graph[a][b] = 1
        graph[b][a] = 1
        
    for mid in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(
                    graph[i][j], 
                    graph[i][mid] + graph[mid][j])
                print(graph[i][j])
    
    distance =  graph[1][k] + graph[k][x]
    if distance == float('inf'):
        return -1
    return distance
        
test_cases = [
    (
        5,
        [
            [1, 2],
            [1, 3],
            [2, 4],
            [3, 4],
            [4, 5]
        ],
        4,
        5,
        3
    ),
    (
        5,
        [
            [1, 2],
            [1, 3],
            [2, 4],
            [3, 4],
            [4, 5]
        ],
        2,
        5,
        3
    ),
    (
        5,
        [
            [1, 2],
            [2, 3],
            [3, 4]
        ],
        2,
        5,
        -1
    ),
    (
        6,
        [
            [1, 2],
            [1, 3],
            [2, 4],
            [3, 4],
            [4, 5],
            [5, 6]
        ],
        4,
        6,
        4
    )
]


for n, roads, k, x, expected in test_cases:
    result = solution(n, roads, k, x)
    print(f"결과: {result}, 예상: {expected}")