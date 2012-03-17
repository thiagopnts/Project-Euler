a, b, c, fib = 0, 1, 1, []
for i in range(10000):
    c = a + b
    a, b = b, c
    if c > 4000000:
        break
    fib.append(c)
print sum([i for i in fib if i%2==0])
