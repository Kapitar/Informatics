n = int(input())
prices = list(map(int, input().split()))
m = int(input())
g = [[] for i in range(n)]
inf = 10**9

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

used = [False] * n
prev = [-1] * n
dist = [inf] * n
cur = 0

used[0] = True
dist[0] = 0

while True:
    for elem in g[cur]:
        if dist[elem] > dist[cur] + prices[cur]:
            dist[elem] = dist[cur] + prices[cur]
            prev[elem] = cur
    
    min_vertex = -1
    min_dist = inf
    for i in range(n):
        if min_dist > dist[i] and not used[i]:
            min_dist = dist[i]
            min_vertex = i

    if min_dist == inf:
        break
    cur = min_vertex
    used[cur] = True

if dist[n - 1] == inf:
    print(-1)
else:
    print(dist[n - 1])