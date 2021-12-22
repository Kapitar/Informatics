m, n = map(int, input().split())

g = []
used = [[False] * n for i in range(m)]

for i in range(m):
    g.append(input())

def dfs(cur_x, cur_y, g, used):
    used[cur_x][cur_y] = True
    neighboards = []

    neighboards.append([cur_x - 1, cur_y])
    neighboards.append([cur_x + 1, cur_y])
    neighboards.append([cur_x, cur_y - 1])
    neighboards.append([cur_x, cur_y + 1])

    for elem in neighboards:
        new_x = elem[0]
        new_y = elem[1]

        if(0 <= new_x <= m - 1) and (0 <= new_y <= n - 1) and not used[new_x][new_y] and g[new_x][new_y] == "#":
            dfs(new_x, new_y, g, used)

cnt = 0

for i in range(m):
    for j in range(n):
        if not used[i][j] and g[i][j] == "#":
            cnt+=1
            dfs(i, j, g, used)

print(cnt)