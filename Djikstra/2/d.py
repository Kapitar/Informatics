n = int(input())
prices = list(map(int, input().split()))
m = int(input())
g = [[] for i in range(n * 3)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    g[3 * u + 2].append([3 * v + 1, 0])
    g[3 * u + 1].append([3 * v, 0])

    g[3 * v + 2].append([3 * u + 1, 0])
    g[3 * v + 1].append([3 * u, 0])


for i in range(n):
    g[3 * i].append([3 * i + 1, prices[i]])
    g[3 * i + 1].append([3 * i + 2, prices[i]])

inf = 10**9
used = [False] * 3 * n
prev = [-1] * 3 * n
dist = [inf] * 3 * n
cur = 0

used[0] = True
dist[0] = 0

while True:
    for elem in g[cur]:
        v, price = elem[0], elem[1]
        if dist[v] > dist[cur] + price:
            dist[v] = dist[cur] + price
            prev[v] = cur
    
    min_vertex = -1
    min_dist = inf
    for i in range(n * 3):
        if min_dist > dist[i] and not used[i]:
            min_dist = dist[i]
            min_vertex = i

    if min_dist == inf:
        break
    cur = min_vertex
    used[cur] = True

if dist[3 * (n - 1)] == inf:
    print(-1)
else:
    print(dist[3 * (n - 1)])