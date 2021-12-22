n = int(input())
g = []
dist = [-1] * n
q = []
prev = [-1] * n

for i in range(n):
    g.append(list(map(int, input().split())))

start, end = map(int, input().split())
start-=1
end-=1


dist[start] = 0
q.append(start)

while q:
    u = q[0]
    q.pop(0)
    
    for i in range(n):
        if g[u][i] == 1 and dist[i] == -1:
            prev[i] = u
            dist[i] = dist[u] + 1
            q.append(i)

if end == start:
    print(0)
elif dist[end] != -1:
    print(dist[end])
    cur = end
    path = []
    while cur != -1:
        path.append(cur + 1)
        cur = prev[cur]

    path.reverse()
    print(*path)
else:
    print(-1)