n, m= map(int, input().split())
g = []
inf = 10 ** 9
for i in range(n):
    g.append(list(map(int, input().split())))

f = g

for i in range(n):
    for j in range(n):
        if f[i][j] == -1:
            f[i][j] = inf

for k in range(n):
    for i in range(n):
        for j in range(n):
            if f[i][k] != inf and f[k][j] != inf and f[i][k] + f[k][j] < f[i][j]:
                f[i][j] = f[i][k] + f[k][j]

if f[s][t] != inf:
    print(f[s][t])
else:
    print(-1)