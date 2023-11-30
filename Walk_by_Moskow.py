from math import atan2, sqrt, pi
s = list(map(int, input().split(' ')))
a = atan2(s[1], s[0])
b = atan2(s[3],s[2])
r1 = sqrt(s[0]**2 + s[1]**2)
if a < 0:
    a += (2*pi)
r2 = sqrt(s[2]**2 + s[3]**2)
if b < 0:
    b += (2*pi)
g = abs(b - a)
l1 = (max(r1, r2) - min(r1, r2) + (min(r1, r2) * g))
l2 = r1 + r2
print(min(l1,l2))