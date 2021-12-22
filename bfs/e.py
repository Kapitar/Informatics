from collections import deque

g = []
minn = 10**5

n, m = map(int, input().split())
for i in range(n):
    g.append(list(map(int, input().split())))

dist = [[-1] * m for i in range(n)]
prev = [[-1] * m for i in range(n)]
q = deque([[0, 0]])
dist[0][0] = 0

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

while q:
    u = q.popleft()
    cur_x, cur_y = u[0], u[1]

    for i in range(4):
        cur_x, cur_y = u[0], u[1]
        while 0 <= cur_x + dx[i] < n and 0 <= cur_y + dy[i] < m and g[cur_x + dx[i]][cur_y] != 1 and g[cur_x][cur_y + dy[i]] != 1:
            if g[cur_x][cur_y] == 2:
                print(dist[u[0]][u[1]] + 1)
                exit(0)
            cur_x += dx[i]
            cur_y += dy[i]
        if 0 <= cur_x < n and 0 <= cur_y < m:
            if g[cur_x][cur_y] == 2:
                print(dist[u[0]][u[1]] + 1)
                exit(0)

        if dist[cur_x][cur_y] == -1:
            dist[cur_x][cur_y] = dist[u[0]][u[1]] + 1
            q.append([cur_x, cur_y])
