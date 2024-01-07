
def f(n):
    print(f"f({n})")
    if n == 1 or n ==0:
        return 1
    t1 = f(n-1)
    t2 = f(n-2)
    t = t1 + t2
    print(f"f({n}) = {t} = {t1} + {t2}")
    return t

print(f(4))
