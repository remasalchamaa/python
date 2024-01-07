def f(n):
    print(f'f({n})')
    if n==1:
        return 1
    t = n * f(n-1)
    print(f'f({n}) = {t}')
    return t

print(f(4))
