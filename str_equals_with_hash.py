s = str(input())
Q = int(input())
zapros = []
for i in range(Q):
    L, A, B = map(int, input().split())
    zapros.append([L, A, B])
n = len(s)
p = 10**9 + 7
x_ = 257
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
s = ' ' + s
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p
def isEqual(from1, from2, slen):
    return(
        (h[from1 + slen] + h[from2] * x[slen]) % p ==
        (h[from2 + slen] + h[from1] * x[slen]) % p
    )

for j in zapros:
    if isEqual(j[1], j[2], j[0]):
        print('yes')
    else:
        print('no')