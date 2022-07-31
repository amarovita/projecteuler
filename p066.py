def isQ(x):
    return round(x ** .5) ** 2 == x

mx = 0
    
for D in range(2, 1001):
    print(f"\r...{D}    ", end='', flush=True)
    if isQ(D):
        continue
    y = 1
    while True:
        try:
            x = D * y * y + 1
            if isQ(x):
                x = round(x ** .5)
                if x > mx:
                    print(f" >>> {x}")
                    mx = x
                break
        except:
            ...
        y += 1

