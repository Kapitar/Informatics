n = int(input())

d, v = map(int, input().split())
d -= 1
v -= 1

r = int(input())
g = [[] for i in range(n)]
inf = 10**9

for i in range(r):
    u, time_out, c, time_in = map(int, input().split())
    u -= 1
    c -= 1
    g[u].append([c, time_out, time_in])

used = [False] * n
dist = [inf] * n
cur = d

used[d] = True
dist[d] = 0

while True:
    for elem in g[cur]:
        c, time_out, time_in = elem
        if dist[cur] <= time_out and time_in < dist[c]:
            dist[c] = time_in
    
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

print(dist[v])