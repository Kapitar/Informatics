from collections import deque

n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

x1-=1
y1-=1
x2-=1
y2-=1

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

q = deque([[x1, y1]])
dist = [[-1] * n for i in range(n)]
dist[x1][y1] = 0

prev = [[-1] * n for i in range(n)]

while q:
    u = q.popleft()
    cur_x, cur_y = u[0], u[1]

    for i in range(8):
        new_x = cur_x + dx[i]
        new_y = cur_y + dy[i]

        if 0 <= new_x < n and 0 <= new_y < n:
            if dist[new_x][new_y] == -1:
                dist[new_x][new_y] = dist[cur_x][cur_y] + 1
                prev[new_x][new_y] = [cur_x, cur_y]
                q.append([new_x, new_y])

print(dist[x2][y2])
path = []
cur_x, cur_y = x2, y2
path.append([x2+1, y2+1])
while dist[cur_x][cur_y] != 0:
    cur_x, cur_y = prev[cur_x][cur_y]
    path.append([cur_x+1, cur_y+1])

path.reverse()
for elem in path:
    print(*elem)