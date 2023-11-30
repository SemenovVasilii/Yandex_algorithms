import sys
N, S, F = map(int, input().split())
matrix = []
for i in range(0, N):
    matrix.append(list(map(int, input().split())))
dist = [sys.maxsize] * N
prev = [sys.maxsize] * N
prev[S-1] = -1
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
            prev[i] = currentDist
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
    otv = []
    foot = F - 1
    for k in range(0, len(prev)):
        if prev[foot] != -1:
            otv.append(foot + 1)
            foot = prev[foot]
        else:
            break
    otv.append(S)
    otv = otv[::-1]
    print(*otv)