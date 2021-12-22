from collections import deque

config = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}

n = 8
first, second = input().split()
x1, y1 = config[first[0]], int(first[1]) - 1
x2, y2 = config[second[0]], int(second[1]) - 1

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


if dist[x2][y2] % 2 == 0:
    print(dist[x2][y2] // 2)
else:
    print(-1)