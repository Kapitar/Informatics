from collections import deque

def neib(n):
    ans = []
    if n // 1000 != 9:
        ans.append(n + 1000)
    if n % 10 != 1:
        ans.append(n - 1)
    s = str(n)
    ans.append(int(s[1:] + s[0]))
    ans.append(int(s[-1] + s[:-1]))
    return ans

dist = [-1] * 10**4
prev = [-1] * 10**4
g = []
q = deque()

start = int(input())
finish = int(input())

q.append(start)
dist[start] = 0

while q:
    u = q.popleft()
    
    neighbours = neib(u)

    for elem in neighbours:
        if 999 < elem < 10000:
            if dist[elem] == -1:
                prev[elem] = u
                dist[elem] = dist[u] + 1
                q.append(elem)

cur = finish
path = []
while cur != -1:
    path.append(cur)
    cur = prev[cur]

path.reverse()
for elem in path:
    print(elem)