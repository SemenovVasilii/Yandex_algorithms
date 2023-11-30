import sys
N, S, F = map(int, input().split())
matrix = []
for i in range(0, N):
    matrix.append(list(map(int, input().split())))
dist = [sys.maxsize] * N
dist[S-1] = 0
currentDist = S - 1
visited = []
mass = []
while currentDist != -1:
    mass = []
    for k in range(0, N):
        if matrix[currentDist][k] > 0 and k not in visited:
            mass.append(k)
    for i in mass:
        if matrix[currentDist][i] + dist[currentDist] < dist[i]:
            dist[i] = matrix[currentDist][i] + dist[currentDist]
    visited.append(currentDist)
    maxx = max(dist)
    temp = -1
    for j in range(0, N):
        if dist[j] < maxx and j not in visited:
            temp = j
            maxx = dist[j]
    currentDist = temp
if dist[F-1] == sys.maxsize:
    print(-1)
else:
    print(dist[F-1])