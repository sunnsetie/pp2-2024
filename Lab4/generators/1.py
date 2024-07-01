def generator(N):
    for i in range(N + 1):
        yield i ** 2

N = 10
for square in generator(N):
    print(square)