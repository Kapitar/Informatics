n = int(input())
g = []
inf = 10 ** 9
for i in range(n):
    g.append(list(map(int, input().split())))

f = g

for i in range(n):
    for j in range(n):
        if f[i][j] == 0:
            f[i][j] = inf

for k in range(n):
    for i in range(n):
        for j in range(n):
            if f[i][k] != inf and f[k][j] != inf and f[i][k] + f[k][j] < f[i][j]:
                f[i][j] = f[i][k] + f[k][j]

for i in range(n):
    for j in range(n):
        if(f[i][j] != inf):
            print(1, end=" ")
        else:
            print(0, end=" ")

    print()