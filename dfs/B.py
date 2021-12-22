import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())

g = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)

def dfs(cur, used, g, comp):
    used[cur] = True
    comp.append(cur + 1)
    for elem in g[cur]:
        if not used[elem]:
            dfs(elem, used, g, comp)

used = [False] * n
comps = []
for i in range(n):
    if not used[i]:
        comp = []
        dfs(i, used, g, comp)
        comps.append(comp)

print(len(comps))
for elem in comps:
    print(len(elem))
    print(*elem)