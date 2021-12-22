from collections import deque

n, m, x1, y1, x2, y2 = map(int, input().split())
inf = 10 ** 9

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
g = []

for i in range(n):
    row = input()
    temp = []
    for letter in row:
        temp.append(letter)
    g.append(temp)

q = deque([[x1, y1]])
dist = [[inf] * m for i in range(n)]
dist[x1][y1] = 0
prev = [[-1] * m for i in range(n)]

while q:
    u = q.popleft()
    cur_x, cur_y = u[0], u[1]

    neighbours = []
    neighbours.append([cur_x - 1, cur_y])
    neighbours.append([cur_x, cur_y - 1])
    neighbours.append([cur_x + 1, cur_y])
    neighbours.append([cur_x, cur_y + 1])

    for neighbour in neighbours:
        new_x, new_y = neighbour

        if 0 <= new_x < n and 0 <= new_y < m and g[new_x][new_y] != "#":
            if dist[cur_x][cur_y] + 1 < dist[new_x][new_y] and g[new_x][new_y] == ".":
                dist[new_x][new_y] = dist[cur_x][cur_y] + 1
                prev[new_x][new_y] = [cur_x, cur_y]
                q.append([new_x, new_y])
            elif dist[cur_x][cur_y] + 2 < dist[new_x][new_y] and g[new_x][new_y] == "W":
                dist[new_x][new_y] = dist[cur_x][cur_y] + 2
                prev[new_x][new_y] = [cur_x, cur_y]
                q.append([new_x, new_y])

if dist[x2][y2] == inf:
    print(-1)
else:
    print(dist[x2][y2])
    path = []
    cur_x, cur_y = x2, y2
    while dist[cur_x][cur_y] != 0:
        old_x, old_y = cur_x, cur_y
        cur_x, cur_y = prev[cur_x][cur_y]
        if old_x - cur_x == 1:
            path.append("S")
        elif old_x - cur_x == -1:
            path.append("N")
        elif old_y - cur_y == 1:
            path.append("E")
        else:
            path.append("W")
    path.reverse()
    print(*path, sep="")