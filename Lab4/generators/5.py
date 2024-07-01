def generator(n):
    for i in range(n, -1, -1):
        yield i

n = 10
for number in generator(n):
    print(number)
