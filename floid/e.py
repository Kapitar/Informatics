n, m = map(int, input().split())
g = []
inf = 10 ** 9
for i in range(n):
    row = []
    for letter in input():
        if letter == "0":
            row.append(0)
        elif letter == "1":
            row.append(inf)
        else:
            row.append(1)
    g.append(row)
f = g

k = int(input())
entries = []
for i in range(k):
    x, y = map(int, input().split())
    entries.append([x, y])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if f[i][k] != inf and f[k][j] != inf and f[i][k] + f[k][j] < f[i][j]:
                f[i][j] = f[i][k] + f[k][j]

minn_entry = -1
for entry in entries:


print(minn)