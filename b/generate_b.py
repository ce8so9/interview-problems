from random import randint
n = 10000
x = [randint(-500, 500) for _ in range(n)]

with open("b.in", "w") as f:
    print(200, file=f)
    print(*x, file=f)
