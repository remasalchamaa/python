def p(x,n):
    print(f"p({x}, {n})")
    if n == 1:
        return x
    t = x * p(x, n-1)
    print(f"p({x}, {n}) = {t}")
    return t

print(p(2,4))
