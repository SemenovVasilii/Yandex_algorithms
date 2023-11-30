s = str(input())
def manacker_nechet(s):
    n = len(s)
    l = 0
    r = -1
    m_chet = [0] * n
    k = 0
    for i in range(0, n):
        if i > r:
            k = 1
        else:
            k = min(r - i + 1, m_chet[l + r - i])
        while (i + k < n) and (i - k >= 0) and (s[i + k] == s[i - k]):
            k += 1
        m_chet[i] = k
        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1
    return m_chet

def manacker_chet(s):
    n = len(s)
    l = 0
    r = -1
    m_nechet = [0] * n
    k = 0
    for i in range(0, n):
        if i > r:
            k = 0
        else:
            k = min(r - i + 1, m_nechet[l + r - i + 1])
        while (i + k < n) and (i - k - 1 >= 0) and (s[i + k] == s[i - k - 1]):
            k += 1
        m_nechet[i] = k
        if i + k - 1 > r:
            l = i - k
            r = i + k - 1
    return m_nechet

print(sum(manacker_nechet(s))+sum(manacker_chet(s)))