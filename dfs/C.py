n = int(input())

g = [[] for i in range(n)]

for i in range(n):
    g[i] = list(map(int, input().split()))

used = [False] * n
acyclic = True

def dfs(used, g, cur, parent):
    global cnt, acyclic
    used[cur] = True
    for i in range(n):
        if used[i] and g[cur][i] == 1 and i != parent:
            acyclic = False
        if g[cur][i] == 1 and not used[i]:
            dfs(used, g, i, cur)
            

dfs(used, g, 0, -1)
if(False not in used and acyclic):
    print("YES")
else:
    print("NO")