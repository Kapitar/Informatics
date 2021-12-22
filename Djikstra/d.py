n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    u, v, time, weight = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append([v, time, weight])
    g[v].append([u, time, weight])

def dijkstra(k):
    cur = 0

    inf = 10**9
    used = [False] * n
    prev = [-1] * n
    dist = [inf] * n

    used[cur] = True
    dist[cur] = 0
    while True:
        for elem in g[cur]:
            v, time, weight = elem[0], elem[1], elem[2]
            if dist[v] > dist[cur] + time and k * 100 + 3 * 1000000 < weight:
                dist[v] = dist[cur] + time
                prev[v] = cur

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

    return dist[n - 1] <= 24 * 60 ** 2

l = 0
r = 10**7

if not dijkstra(l):
    ans = 0
elif dijkstra(r):
    ans = r
else:
    while r - l > 1:
        m = (r + l) // 2
        if dijkstra(m):
            l = m
        else:
            r = m
    ans = l

print(ans)