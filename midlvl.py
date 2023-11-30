std = int(input())
mass = (list(map(int, input().split())))
up = []
down = []
current = 0
s_current = 0
s_previous = 0
for i in range(0, std):
    s_current = i * mass[i]
    current = s_current - s_previous
    up.append(current)
    s_previous += mass[i]


s_previous = 0
for j in range(std - 1, -1, -1):
    i = abs(std - 1 - j)
    s_current = mass[j] * i
    current = s_previous - s_current
    down.append(current)
    s_previous += mass[j]
    i += 1

down = down[::-1]
otv = []
for k in range(0, len(down)):
    otv.append(up[k] + down[k])
print(*otv)