def run_djikstra():
    n, m = map(int, input().split())
    g = [[] for i in range(n)]
    inf = 2009000999
    for i in range(m):
        u, v, weight = map(int, input().split())

        g[u].append([v, weight])
        g[v].append([u, weight])

    start = int(input())

    dist = [inf] * n
    dist[start] = 0

    s = {tuple([0, start])}
    while len(s):
        cur = min(s)[1]
        s.remove(tuple(min(s)))
        
        for elem in g[cur]:
            u, weight = elem
            if dist[u] > dist[cur] + weight:
                if tuple([dist[u], u]) in s:
                    s.remove(tuple([dist[u], u]))
                dist[u] = dist[cur] + weight
                s.add(tuple([dist[u], u]))
            
    print(*dist)

num = int(input())
for i in range(num):
    run_djikstra()