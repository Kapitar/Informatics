from collections import deque

r, c = map(int, input().split())
g = []
x = 0
y = 0

for i in range(r):
    row = input()
    temp = []
    j = 0
    for letter in row:
        if letter == "S":
            x = j
            y = i
        temp.append(letter)
        j += 1
    g.append(temp)

dist = [[[-1] * 4 for i in range(c)] for i in range(r)]
q = deque()
for i in range(4):
    dist[x][y][i] = 0
    q.append([x, y, i])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    u = q.popleft()
    cur_x, cur_y, direction = u

    for i in range(2):
        new_direction = (i + direction) % 4

        new_x = dx[new_direction] + cur_x
        new_y = dy[new_direction] + cur_y

        if 0 <= new_x < c and 0 <= new_y < r and g[new_x][new_y] != "X":
            if dist[new_x][new_y][new_direction] == -1 and g[new_x][new_y] == " ":
                dist[new_x][new_y][new_direction] = dist[cur_x][cur_y][direction] + 1
                q.append([new_x, new_y, new_direction])
            elif dist[new_x][new_y][new_direction] == -1 and g[new_x][new_y] == "F":
                dist[new_x][new_y][new_direction] = dist[cur_x][cur_y][direction] + 1
                print(dist[new_x][new_y][new_direction])
                exit(0)
