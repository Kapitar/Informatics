n, m = map(int, input().split())
start, finish = map(int, input().split())
start-=1
finish-=1
inf = 10 ** 9
g = [[inf] * n for i in range(n)]
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
for i in range(m):
    s, e, p = map(int, input().split())
    s -= 1
    e -= 1
    p = 1 - (p / 100)

    g[s][e] = p
    g[e][s] = p

for i in range(n):
    g[i][i] = 1

f = g

for k in range(n):
    for i in range(n):
        for j in range(n):
            if f[i][k] != inf and f[k][j] != inf and f[i][k] * f[k][j] > f[i][j]:
                f[i][j] = f[i][k] * f[k][j]

print(toFixed(1 - f[start][finish], 100))