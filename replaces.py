N = int(input())
mass = []
def permutations(mass):
    if len(mass) == 0:
        return []
    if len(mass) == 1:
        return mass
    final = []
    for i in range(len(mass)):
        m = mass[i]
        rMass = mass[:i] + mass[i+1:]
        for j in permutations(rMass):
            final.append(m + j)
    return final

for k in range(1, N+1):
    mass.append(str(k))
for l in permutations(mass):
    print(l)