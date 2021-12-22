n, u, d, i, j, l = map(int, input().split())
floors = []

for i in range(l):
    k = input().split()
    for j in range(1, int(k[0]) + 1):
        floors.append(k[j])

while True:
    