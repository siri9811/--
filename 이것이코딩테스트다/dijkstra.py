import heapq

graph = [
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5)],
    []
]
INF = float('inf')
m = len(graph)

distance = [INF] * m
distance[0] = 0

pq = []
heapq.heappush(pq,(0,0))
while pq:
    dist, now = heapq.heappop(pq)
    if distance[now] < dist:
        continue
    for next_node, cost in graph[now]:
        if distance[next_node] > dist + cost:
            distance[next_node] = dist + cost
            heapq.heappush(pq,(distance[next_node],next_node))
for i in distance:
    print(i)

    
    
    
    

    
       