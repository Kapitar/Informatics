inf = 10 ** 7
n, m = map(int, input().split())
edges = []

for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

start = 0
f = [inf for i in range(n)]
prev = [-1 for i in range(n)]
f[start] = 0


for k in range(n - 1):
    for edge in edges:
        u, v, w = edge
        print(edge)
        if f[u] + w < f[v] and f[u] != inf:
            f[v] = f[u] + w
            prev[v] = u

for i in range(n):
    print(f[i])