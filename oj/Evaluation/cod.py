I = input
R = lambda: map(int, I().split())
for _ in [0] * int(I()):
    n = int(I())
    d, z = {}, 0
    for v in R():
        while v & 1 == 0:
            v >>= 1
        d[v] = d.get(v, 0) + 1
    for v in R():
        while v and (v not in d or d[v] == 0):
            v >>= 1
        if v:
            d[v] = d.get(v, 0) - 1
        else:
            z = 1
    print(["YES", "NO"][z])
