n, s, f = map(int, input().split())
s -= 1
f -= 1
inf = 10**9

g = []

for i in range(n):
    g.append(list(map(int, input().split())))

used = [False] * n
dist = [inf] * n
prev = [-1] * n
cur = s

used[s] = True
dist[s] = 0

while True:
    for i in range(n):
        if g[cur][i] != -1:
            if dist[i] > dist[cur] + g[cur][i]:
                dist[i] = dist[cur] + g[cur][i]
                prev[i] = cur
    
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

if dist[f] == inf:
    print(-1)
else:
    print(dist[f])