import time

numbers = {}
numbers[1] = 1
numbers[0] = 1

def f(n):
    if n in numbers:
        return numbers[n]
    else:
        numbers[n] = f(n-1) + f(n-2)
        return numbers[n]
start_time = time.time()
print(f(40))
end_time = time.time()
print(end_time - start_time)
