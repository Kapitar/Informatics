n, m = map(int, input().split())
g = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    v-=1
    u-=1
    g[u].append(v)
    g[v].append(u)

used = [False] * n
colors = [-1] * n
bipartite = True

def dfs(used, g, cur, color):
    global bipartite
    used[cur] = True
    colors[cur] = color

    for i in g[cur]:
        if color == colors[i]:
            bipartite = False
        if not used[i]:
            dfs(used, g, i, (color + 1) % 2)

for i in range(n):
    if not used[i]:
        dfs(used, g, i, 0)

if bipartite:
    print("YES")
    for i in range(n):
        if(colors[i] == 0):
            print(i + 1, end=" ")
else:
    print("NO")
