import sys
from math import gcd
from fractions import Fraction
from primes import get_primes

pr = get_primes(10000000)
print('generated')

def factor(d):
    q = d ** 0.5
    if d in pr:
        yield d
    else:
        for x in pr:
            if x > q:
                break
            if d % x == 0:
                yield x

def phi(d):
    num, den = d, 1
    for x in factor(d):
        num *= x - 1
        den *= x
    return num // den

for x in range(1,11):
    print(phi(x))
    
print(phi(87109))

res = ratio = float('inf')
for x in range(9580000, 1, -1):
    z = phi(x)
    if x/z < ratio:
        if sorted(str(x))==sorted(str(z)):
            ratio = Fraction(x,z)
            res = x
    if x % 10000 == 0:
        sys.stdout.flush()
        print(f'>>>{x:10} {res:10}', end='\r')
print()
print('Res: ', res)
