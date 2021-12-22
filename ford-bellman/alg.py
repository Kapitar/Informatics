inf = 10 ** 7
n = int(input())
m = int(input())
start = int(input())
edges = []

for i in range(m):
    u, v, w = map(int, input().split())
    edges.append(tuple(u, v, w))

f = [inf for i in range(n)]
f[start] = 0

for k in range(n - 1):
    for edge in edges:
        u, v, w = edge
        if f[u] + w < f[v] and f[u] != inf:
            f[v] = f[u] + w
            prev[v] = u