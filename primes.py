_ptable = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
    173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
    367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
    433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
    499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
    577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
    643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
    719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
    797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
    863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
    947, 953, 967, 971, 977, 983, 991, 997
]


def get_primes(m):
    t = [2, 3]
    p, n, q, r = 5, 3, 9, 1
    while (p < m):
        if  all(p % x for x in t[:r]):
            t.append(p)
        p += 2
        while p>q:
            q += n
            n += 1
            q += n
        while t[r-1]<n:
            r += 1
    return t

def gen_primes(m=0):
    t = [2, 3]
    yield 2
    yield 3
    p, n, q, r = 5, 3, 9, 1
    while not(m) or (p < m):
        if  all(p % x for x in t[:r]):
            t.append(p)
            yield p
        p += 2
        while p>q:
            q += n
            n += 1
            q += n
        while t[r-1]<n:
            r += 1
    return t

def prime(m=0):
    if m > 2:
        yield 2
    if m > 3:
        yield 3
    p, n, q = 5, 3, 9
    while (not m) or (p < m):
        if  all(p % x for x in range(3, n+1, 2)):
            yield p
        p += 2
        while p>q:
            q += n
            n += 1
            q += n

# _ptable = get_primes(1000)

def isprime(n, ptable=_ptable):
    if n <= ptable[-1]:
        return n in ptable
    q = int(n ** 0.5) + 1
    for x in ptable:
        if n % x == 0:
            return False
        if x > q:
            return True
    if q>ptable[-1]:
        for x in range(ptable[-1],q,2):
            if n % x == 0:
                return False
    return True
