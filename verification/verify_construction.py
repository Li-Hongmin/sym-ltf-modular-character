"""Brute-force check of Theorem 1: build the U_j exactly as in the proof and compare both sides."""
import itertools, cmath, random
def ltf(w, th):
    return lambda v: int(sum(a*b for a, b in zip(w, v)) >= th)
def check(h, q, seed):
    rnd = random.Random(seed)
    T = [(([rnd.randint(-3, 3) for _ in range(h)]), rnd.randint(-3, 3)) for _ in range(q)]
    f = [rnd.randint(0, 1) for _ in range(q + 1)]
    l = 1
    while 2**l <= q: l += 1
    R = 2**l; om = cmath.exp(2j*cmath.pi/R)
    fz = lambda t: f[t] if t <= q else 0
    n = h + 2*l + 1  # variables: x (h), a (l), s (l), u
    U = []
    for (w, th) in T:
        B = abs(th) + sum(abs(c) for c in w) + 1
        for b in range(l):
            W = w + [0]*(2*l+1); W[h+b] = B
            U += [ltf(W, th + B)] * (2**b)
    const = 0
    for b in range(l):
        for c in range(l):
            if b + c < l:
                W = [0]*n; W[h+b] = -1; W[h+l+c] = -1
                U += [ltf(W, -1)] * (2**(b+c)); const -= 2**(b+c)
    U += [ltf([0]*n, 0)] * (const % R)
    for t in range(R):
        if fz(t) == 0:
            W = [0]*n
            th = l + 1
            for c in range(l):
                if (t >> c) & 1: W[h+l+c] = 1
                else: W[h+l+c] = -1; th -= 1
            W[n-1] = 1
            U += [ltf(W, th)] * (R//2)
    lhs = 0
    for v in itertools.product([0, 1], repeat=n):
        lhs += om ** (sum(g(v) for g in U) % R)
    lhs /= 2**n
    acc = sum(fz(sum(ltf(w, th)(x) for (w, th) in T)) for x in itertools.product([0, 1], repeat=h)) / 2**h
    assert abs(lhs - acc/R) < 1e-9, (h, q, seed, lhs, acc/R)
    return len(U)
for (h, q) in [(3, 1), (3, 2), (3, 3), (4, 4), (3, 5), (2, 7)]:
    for seed in range(5):
        m = check(h, q, seed)
print("Identity (1) agrees numerically (tolerance 1e-9) on 30 random instances (h<=4, q<=7).")
