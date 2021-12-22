n, m, k = map(int, input().split())
inf = 10 ** 9
g = [[-inf] * n for i in range(n)]
prev = [[-1] * n for i in range(n)]
for i in range(m):
    b, e, w = map(int, input().split())
    b -= 1
    e -= 1
    if g[b][e] < w:
        g[b][e] = w

cities = list(map(lambda x: x - 1, map(int, input().split())))

for i in range(n):
    g[i][i] = 0

f = g

for k in range(n):
    for i in range(n):
        for j in range(n):
            if f[i][k] != -inf and f[k][j] != -inf and f[i][k] + f[k][j] > f[i][j]:
                f[i][j] = f[i][k] + f[k][j]
                prev[i][j] = f[i][j]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if f[i][k] != -inf and f[k][j] != -inf and f[k][k] > 0:
                f[i][j] = inf

cur = cities[len(cities) - 1]
path = []
while cur != -1:
    path.append(cur + 1)
    cur = prev[cur]

path.reverse()
print(*path)
