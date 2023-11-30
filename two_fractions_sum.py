a, b, c, d = map(int, input().split())
up = 0
down = 0
maxx_krat = 1
if b == d:
    down = b
    up = a + c
else:
    down = b * d
    up = (a * d) + (c * b)
for i in range(1, up + 1):
    if (up % i == 0) and (down % i == 0):
        maxx_krat = i
print(up // maxx_krat, down // maxx_krat)
